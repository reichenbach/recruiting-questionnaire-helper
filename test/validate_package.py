"""Read-only, offline validation of the shareable package (Python 3)."""

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA256 = "6de11778b357115ae19b86a5d521726a7c383055dee11cf0dc9f7bbd9e88abfd"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def leaves(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from leaves(item)
    elif isinstance(value, list):
        for item in value:
            yield from leaves(item)
    else:
        yield value


def at(value, path):
    for key in path.split("."):
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def check_paths(value, paths):
    for path in paths.split():
        try:
            at(value, path)
        except (KeyError, IndexError, TypeError) as error:
            raise AssertionError("Missing template field: " + path) from error


def same_shape(template, fixture, path=""):
    # A wholly unanswered consent block is intentionally null in the fixture.
    if path == "consents" and fixture is None:
        return
    if isinstance(template, dict):
        require(isinstance(fixture, dict), "Expected object: " + path)
        require(template.keys() == fixture.keys(), "Different keys: " + path)
        for key in template:
            same_shape(template[key], fixture[key], (path + "." + key).lstrip("."))
    elif isinstance(template, list):
        require(isinstance(fixture, list), "Expected list: " + path)
        require(len(template) == len(fixture), "Different fixture list length: " + path)
        for index, (left, right) in enumerate(zip(template, fixture)):
            same_shape(left, right, path + "." + str(index))
    else:
        require(fixture is None or isinstance(fixture, (str, bool)), "Invalid value type: " + path)


def personal_data_issues(text, *, reference=False):
    """Return pattern categories, without echoing potentially private values."""
    issues = set()
    for match in re.finditer(r"[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})", text, re.I):
        if match.group(1).lower() not in {"example.com", "example.org"}:
            issues.add("non-example email")
    phone_pattern = re.compile(
        r"(?<![\w])(?:\+?1[-. \t]?)?"
        r"(?:\(\d{3}\)[-. \t]*|\d{3}[-. \t]?)?"
        r"\d{3}[-. \t]?\d{4}(?![\w])"
    )
    for match in phone_pattern.finditer(text):
        digits = re.sub(r"\D", "", match.group())
        # Split sensitive pattern literals so the validator can scan its own source.
        # Only the exact opt-out number quoted in the read-only reference is exempt.
        if reference and match.group() == "1-" "877-" "845-" "6272":
            continue
        local_digits = digits[1:] if len(digits) == 11 and digits.startswith("1") else digits
        if local_digits[-7:-4] != "555":
            issues.add("non-555 phone")
    if re.search(r"/(?:Users|home)/|[A-Z]:[\\/]Users(?:[\\/]|\b)", text, re.I):
        issues.add("home path")
    if re.search(r"\b[\w-]+\.local\b|omar" r"chy|Double" r"Secret", text, re.I):
        issues.add("hostname")
    return issues


def phone_fields(value, path=""):
    """Inspect every phone/fax field, including populated fields in nested contacts."""
    if isinstance(value, dict):
        for key, item in value.items():
            field_path = (path + "." + key).lstrip(".")
            if key in {"phone", "fax"} or key.endswith("_phone"):
                yield field_path, item
            else:
                yield from phone_fields(item, field_path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from phone_fields(item, path + "." + str(index))


def check_fixture(template, fixture, *, sport, city, postal_code, form_url):
    same_shape(template, fixture)
    require(fixture["intake"]["dry_run"] is True, "Fixture must be a dry run")
    team = "women's" if sport == "volleyball" else "men's"
    require(fixture["intake"]["sport"] == sport and
            fixture["intake"]["team"] == team, "Wrong fixture sport/team")
    require(fixture["athlete"]["first_name"] + " " +
            fixture["athlete"]["last_name"] == "Test Athlete", "Wrong synthetic name")
    require(fixture["athlete"]["email"] == "test@example.com", "Wrong synthetic email")
    address = fixture["athlete"]["address"]
    require(address["street_line_1"] == "123 Example St", "Wrong example address")
    require(address["city"] == city and address["state_province"] == "IL" and
            address["postal_code"] == postal_code and address["country"] == "US",
            "Wrong example city/state/ZIP/country")
    require(fixture["consents"] is None, "Fixture must not answer consents")
    require(fixture["high_school"]["coach"]["name"] == "Test Coach" and
            fixture["athletics"]["high_school_coach"]["name"] == "Test Coach",
            "Fixture must supply the synthetic high-school coach")
    require(fixture["athletics"]["high_school_jersey_number"] == "7",
            "Fixture must supply the synthetic high-school jersey number")
    for path in (
        "athletics.club_teams.0.jersey_number",
        "eligibility.ncaa_id",
        "eligibility.naia_playnaia_id",
    ):
        require(at(fixture, path) is None, "Fixture must leave field null: " + path)
    require(all(value is None or value == "" for value in leaves(fixture["approvals"])),
            "Fixture must not grant approvals")
    require(len(fixture["target_schools"]) == 1, "Expected one test target")
    target = fixture["target_schools"][0]
    require(target["school"] == "Illinois Wesleyan University" and
            target["sport"] == sport and target["team"] == team, "Wrong test target")
    require(target["form_url"] == form_url, "Wrong test form URL")
    for other_sport in template["sports"].keys() - {sport}:
        require(fixture["sports"][other_sport] == template["sports"][other_sport],
                "Unrelated sport data in fixture: " + other_sport)
    require(fixture["athletics"]["other_sports_played"] ==
            template["athletics"]["other_sports_played"], "Other-sport answers in fixture")
    for value in leaves(fixture):
        if isinstance(value, str) and "@" in value:
            require(value.endswith("@example.com"), "Non-example email in fixture")
    for path, value in phone_fields(fixture):
        require(value in (None, "") or (isinstance(value, str) and
                re.fullmatch(r"202-555-01\d{2}", value)),
                "Fixture phone must use 202-555-01xx: " + path)
    for field in ("street_line_1", "city", "state_province", "postal_code", "country"):
        require(bool(fixture["high_school"]["address"][field]),
                "Missing fake high-school address: " + field)
    require(fixture["high_school"]["has_american_football_team"] is False,
            "Expected explicit synthetic high-school football answer")
    if sport == "volleyball":
        volleyball = fixture["sports"][sport]
        require(volleyball["primary_position"] == "OH" and
                volleyball["secondary_position"] == "RS", "Wrong volleyball positions")
        require(fixture["athletics"]["height"]["value"] == "5'11\"" and
                fixture["athletics"]["height"]["unit"] == "feet/inches",
                "Volleyball fixture must preserve 5'11\" without conversion")


def main():
    required = [
        ".gitignore", "AGENTS.md", "README.md", "START_PROMPT.md",
        "CHATGPT_PROMPT.md", "profile.template.json", "prompts/first-run-check.md",
        "prompts/start.md", "prompts/find-forms.md", "prompts/fill-forms.md",
        "prompts/report.md", "reference/recruiting-intake-tree.md",
        "reference/sample-forms.md", "reference/verified-forms.md",
        "test/dry-run-profile.json", "test/dry-run-profile-volleyball.json", "test/README.md",
    ]
    for name in required:
        require((ROOT / name).is_file(), "Missing package file: " + name)
    print("PASS: required package files")

    # read_text uses universal newlines: CRLF and CR become LF before hashing.
    source = (ROOT / "reference/recruiting-intake-tree.md").read_text(encoding="utf-8")
    require(hashlib.sha256(source.encode("utf-8")).hexdigest() == SOURCE_SHA256, "Read-only reference changed")
    section = source[source.index("## 5. Sources (all read-only)"):]
    sample = (ROOT / "reference/sample-forms.md").read_text(encoding="utf-8")
    require(sample == section, "Sample sources must copy section 5 exactly")
    rows = [line for line in sample.splitlines() if line.startswith("| ")][1:]
    require(len(rows) == 61, "Expected all 61 original source rows")
    print("PASS: unchanged reference and exact section-5 copy (61 source rows)")

    template = json.loads((ROOT / "profile.template.json").read_text(encoding="utf-8"))
    require(all(value is None or value == "" for value in leaves(template)), "Template contains prefilled answers")
    expected_sports = {
        "baseball", "softball", "football", "basketball", "soccer", "volleyball",
        "track_field_cross_country", "wrestling", "swimming_diving", "golf",
        "tennis", "lacrosse", "ice_hockey", "generic_any_sport",
    }
    require(set(template["sports"]) == expected_sports, "Sport coverage differs from section 2")
    check_paths(template, """
        intake.sport intake.team intake.graduation_year intake.target_levels
        athlete.first_name athlete.middle_name athlete.last_name athlete.preferred_name
        athlete.email athlete.secondary_email athlete.mobile_phone athlete.home_phone
        athlete.address.street_line_1 athlete.address.city athlete.address.state_province
        athlete.address.postal_code athlete.address.country athlete.date_of_birth
        athlete.gender athlete.sex athlete.citizenship athlete.ethnicity
        athlete.hispanic_latino athlete.headshot_file athlete.social.x_twitter
        athlete.social.instagram athlete.social.facebook
        family.parent_guardian_1.name family.parent_guardian_1.email
        family.parent_guardian_1.mobile_phone family.parent_guardian_1.occupation
        family.parent_guardian_1.college_attended family.parent_guardian_1.address
        family.parent_guardian_1.highest_education
        family.parent_guardian_1.attended_four_year_college
        family.parent_guardian_2.name family.parent_guardian_2.email
        family.parent_guardian_2.mobile_phone family.parent_guardian_2.occupation
        family.parent_guardian_2.college_attended family.parent_guardian_2.address
        family.parent_guardian_2.highest_education
        family.parent_guardian_2.attended_four_year_college
        family.lives_with family.parents_marital_status family.siblings.0.name
        family.siblings.0.age family.school_connections.0.family_alumni_ties
        high_school.name high_school.ceeb_ets_code high_school.address.street_line_1
        high_school.address.city high_school.address.state_province
        high_school.address.postal_code high_school.address.country
        high_school.has_american_football_team high_school.coach.email high_school.counselor.email
        academics.graduation_year academics.gpa.weighted academics.gpa.unweighted
        academics.gpa.core academics.class_rank academics.sat.math academics.sat.reading_ebrw
        academics.sat.writing academics.sat.total academics.sat.superscore academics.psat.total
        academics.act.composite academics.act.english academics.act.math academics.act.reading
        academics.act.science academics.act.writing academics.sat.test_dates academics.act.test_dates
        academics.sat.planned_test_dates academics.act.planned_test_dates
        academics.transcript_file academics.test_score_files academics.intended_major
        academics.academic_honors academics.ap_courses_scores.0.course
        academics.ap_courses_scores.0.score academics.other_schools_considering
        academics.entry_term academics.admit_term academics.projected_enrollment_year
        academics.application_status academics.early_decision_interest academics.financial_aid_interest
        academics.student_type academics.previous_colleges.0.name
        academics.previous_colleges.0.credits_hours academics.previous_colleges.0.gpa
        eligibility.ncaa_eligibility_center_registered eligibility.ncaa_id
        eligibility.naia_playnaia_id eligibility.qualifier
        athletics.height.unit athletics.weight.unit athletics.recruiting_video_links
        athletics.high_school_jersey_number
        athletics.club_teams.0.name athletics.club_teams.0.jersey_number
        athletics.club_teams.0.position athletics.club_teams.0.coach.email
        athletics.tournaments_showcases_events athletics.high_school_coach.email
        athletics.other_sports_played athletics.athletic_honors athletics.hobbies
        athletics.recruiting_profile_url consents.records.0.verbatim_wording
        consents.records.0.verbatim_options consents.records.0.family_answer
        target_schools.0.school target_schools.0.sport target_schools.0.team
        target_schools.0.form_url target_schools.0.official_source_page_url
        approvals.full_profile.approved approvals.final_school_list.approved
        approvals.school_actions.0.approved
    """)
    check_paths(template["sports"], """
        baseball.primary_position baseball.bats baseball.throws baseball.summer_jersey_number
        baseball.sixty_yard_time baseball.exit_velocity baseball.pitching_velocity
        softball.batting.at_bats softball.batting.fielding_average softball.pitching.earned_runs
        softball.pitching.earned_run_average softball.sixty_yard_time softball.strengths
        softball.weaknesses softball.film_available softball.favorite_snack_foods
        football.forty_yard_time football.hundred_meter_time football.bench football.squat
        football.power_clean football.max_clean football.vertical_jump football.broad_jump
        football.shuttle football.offers football.camps_attended football.juco_graduation_year
        football.college_choice_factor_ratings.0.rating_1_to_10 football.favorite_nfl_team
        football.favorite_artist basketball.stats_current_year.points_per_game
        basketball.stats_last_year.points_per_game basketball.stats_current_year.steals_per_game
        basketball.stats_current_year.blocks_per_game basketball.july_tournaments
        basketball.years_lettered basketball.game_film_available soccer.dominant_foot
        volleyball.approach_jump_touch volleyball.block_jump_touch volleyball.standing_reach
        volleyball.vertical_jump volleyball.t_shirt_size track_field_cross_country.event_group
        track_field_cross_country.events.3.best_mark track_field_cross_country.events.3.date
        track_field_cross_country.milesplit_link track_field_cross_country.years_trained_year_round
        wrestling.state_finish_by_grade.grade_9 wrestling.state_finish_by_grade.grade_12
        wrestling.records_by_year.0.weight_class wrestling.freestyle_accomplishments
        wrestling.greco_accomplishments wrestling.juco_accomplishments wrestling.state_champion
        wrestling.state_placer wrestling.state_qualifier wrestling.one_hundred_plus_wins
        wrestling.all_american wrestling.national_qualifier swimming_diving.swim_events.3.course
        swimming_diving.swim_events.3.time swimming_diving.dive_events.2.score
        swimming_diving.amherst_dive_scores.list_of_dives
        swimming_diving.amherst_best_times.0.time swimming_diving.best_primary_event_time_yards
        swimming_diving.secondary_event swimming_diving.diving golf.usga_ghin_number
        golf.home_course_slope golf.home_course_rating golf.head_pro.email golf.swing_instructor.email
        golf.driving_distance_carry golf.ball_speed golf.clubhead_speed golf.swing_video_url
        golf.five_best_tournament_results.4.score golf.top_three_recent_finishes.2.place
        golf.anticipated_major_tournaments tennis.utr_rating tennis.usta_u18_national_ranking
        tennis.world_tennis_number tennis.usta_itf_events.2.results tennis.private_coach.phone
        tennis.dominant_hand tennis.strongest_strokes tennis.why_play_tennis
        tennis.what_you_want_from_team tennis.sport_goals_next_two_years
        tennis.most_influential_person tennis.religion
        tennis.high_school_position_grid.singles.5.position
        tennis.high_school_position_grid.doubles.2.partner
        tennis.prior_college_position_grid.singles.5.position
        tennis.prior_college_position_grid.doubles.2.partner lacrosse.strong_hand
        lacrosse.current_class_schedule lacrosse.currently_enrolled_at_aacc
        lacrosse.high_school_level_played lacrosse.college_level_played
        lacrosse.video_uniform_number lacrosse.video_uniform_color ice_hockey.shoots
        ice_hockey.league_website ice_hockey.goalie_goals_against_average
        ice_hockey.goalie_save_percentage ice_hockey.goalie_record
        ice_hockey.team_stats_by_year.0.points ice_hockey.goalie_stats_by_year.0.saves
        ice_hockey.goalie_stats_by_year.0.goals_against generic_any_sport.sport_being_recruited_for
        generic_any_sport.projected_enrollment_term generic_any_sport.projected_enrollment_year
    """)
    print("PASS: blank template, common field coverage and 14 sport blocks")

    for path in (
        "athletics.high_school_jersey_number",
        "athletics.club_teams.0.jersey_number",
        "eligibility.ncaa_id",
        "eligibility.naia_playnaia_id",
    ):
        require(at(template, path) is None, "Expected unanswered template field: " + path)
    for name, sport, city, postal_code, form_hash in (
        ("dry-run-profile.json", "baseball", "Anytown", "00000", "8b8ac3c4ffef"),
        ("dry-run-profile-volleyball.json", "volleyball", "Springfield", "62701", "1b72853c63ec"),
    ):
        fixture = json.loads((ROOT / "test" / name).read_text(encoding="utf-8"))
        check_fixture(template, fixture, sport=sport, city=city, postal_code=postal_code,
                      form_url="https://questionnaires.armssoftware.com/" + form_hash)
        print("PASS: synthetic " + sport + " dry-run fixture, null consents, "
              "no approvals or other-sport answers")

    patterns = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    expected_patterns = {"profile.json", "profile*.local.json", "reports/", "*.pdf", "screenshots/", ".DS_Store"}
    require(expected_patterns <= set(patterns), "Missing privacy ignore pattern")
    if shutil.which("git") and (ROOT / ".git").exists():
        ignored = ["profile.json", "profile.family." "local.json", "reports/run.md", "reports/approvals.log", "transcript.pdf", "screenshots/form.png", ".DS_Store"]
        visible = ["profile.template.json", "test/dry-run-profile.json",
                   "test/dry-run-profile-volleyball.json", "test/README.md", "test/validate_package.py"]
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "--stdin"], cwd=ROOT,
            input="\n".join(ignored + visible) + "\n", capture_output=True, text=True, check=False,
        )
        require(result.returncode in (0, 1), "git check-ignore failed")
        require(set(result.stdout.splitlines()) == set(ignored), "Ignore behavior hides package files or exposes private files")
        print("PASS: Git ignores private artifacts and keeps template/test files visible")
    else:
        print("PASS: required ignore patterns (Git behavior check skipped outside a Git checkout)")

    if shutil.which("git") and (ROOT / ".git").exists():
        names = set()
        for options in ([], ["--others", "--exclude-standard"]):
            result = subprocess.run(
                ["git", "ls-files", "-z", *options], cwd=ROOT,
                capture_output=True, check=True,
            )
            names.update(result.stdout.decode("utf-8").rstrip("\0").split("\0"))
        names.discard("")
    else:
        names = set(required + ["test/validate_package.py"])

    markdown_pages = []
    for name in sorted(names):
        page = ROOT / name
        if not page.is_file():
            continue
        data = page.read_bytes()
        if b"\0" in data:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        issues = personal_data_issues(text, reference=name.startswith("reference/"))
        require(not issues, "Personal-data pattern in " + name + ": " + ", ".join(sorted(issues)))
        if page.suffix == ".md":
            markdown_pages.append(page)
    print("PASS: all tracked and untracked non-ignored text personal-data scan (binaries skipped; exact reference opt-out number exempt)")

    repo_url = "https://github.com/reichenbach/recruiting-questionnaire-helper"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    sharer_heading = "## Notes for someone sharing this package"
    require(sharer_heading in readme, "Missing README sharer notes")
    parent_notes, sharer_notes = readme.split(sharer_heading, 1)
    repo_pattern = r"https://github\.com/[^\s)]+"
    require(set(re.findall(repo_pattern, parent_notes)) == {repo_url},
            "README parent steps must contain the package repository URL")
    require(re.findall(repo_pattern, sharer_notes) == [repo_url],
            "README sharer notes must contain only the package repository URL")
    for name in ("START_PROMPT.md", "CHATGPT_PROMPT.md"):
        prompt = (ROOT / name).read_text(encoding="utf-8")
        require(set(re.findall(repo_pattern, prompt)) == {repo_url},
                name + " must contain the same package repository URL as README")
    for name in ("AGENTS.md", "START_PROMPT.md", "CHATGPT_PROMPT.md", "README.md",
                 "prompts/first-run-check.md"):
        instructions = " ".join((ROOT / name).read_text(encoding="utf-8").split())
        fallback_sentence = (
            "I couldn't open the online package, so I'll use a local copy or ask you to share it."
        )
        require(fallback_sentence in instructions,
                name + " must include the exact package-fetch fallback sentence")
        instructions = instructions.lower()
        for phrase in ("try once only", "no retry loops", "bounded timeout", "private",
                       "404", "offline", "blocked", "local", "bundled", "never crash or stall"):
            require(phrase in instructions, name + " must cover fetch fallback: " + phrase)
    agent_rules = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    require(not re.search(r"codex|chatgpt", agent_rules, re.I),
            "AGENTS.md must use agent-neutral wording")
    print("PASS: matching repository URLs, single-attempt fetch fallbacks and agent-neutral rules")

    verified = (ROOT / "reference/verified-forms.md").read_text(encoding="utf-8")
    backup = (ROOT / "CHATGPT_PROMPT.md").read_text(encoding="utf-8")
    south_dakota_primary = "https://questionnaires.armssoftware.com/eafc4e7429b0"
    south_dakota_fallback = "https://college.jumpforward.com/questionnaire.aspx?iid=453&sportid=13"
    form_urls = {
        "https://questionnaires.armssoftware.com/1b72853c63ec",
        "https://www.frontrush.com/FR_Web_App/Player/PlayerSubmit.aspx?sid=MjAzMDk=-S6n4ygUqgK8=&ptype=recruit",
        south_dakota_primary,
        south_dakota_fallback,
        "https://www.cmueagles.com/sports/wvball/WVB_Recruiting_Questionnaire",
    }
    for url in form_urls:
        require(url in verified and url in backup, "Missing verified volleyball example: " + url)
    for name in ("AGENTS.md", "prompts/find-forms.md", "README.md"):
        require("reference/verified-forms.md" in (ROOT / name).read_text(encoding="utf-8"),
                name + " must point to the dated verified forms")
    require("2026-10-23" in verified and "2026-10-23" in backup,
            "Verified examples must carry their verification date")
    for name in ("reference/verified-forms.md", "CHATGPT_PROMPT.md", "START_PROMPT.md"):
        page_text = (ROOT / name).read_text(encoding="utf-8")
        section = re.search(
            r"University of South Dakota.*?(?=\n- (?:\*\*)?Central Methodist|\nKeep saved family data)",
            page_text, re.S,
        )
        require(section is not None, name + " must include the South Dakota example")
        text = " ".join(section.group().lower().split())
        for label, url in (("primary", south_dakota_primary), ("fallback", south_dakota_fallback)):
            require(re.search(label + r"(?: \([^)]*\))?:\s*" + re.escape(url), text),
                    name + " must label the South Dakota " + label + " URL")
        primary_notes, fallback_notes = text.split(south_dakota_fallback, 1)
        require(south_dakota_primary in primary_notes and
                all(phrase in primary_notes for phrase in (
                    "arms", "goyotes.com", '"recruiting questionnaire"', "2026-10-23",
                    "visitor details / create profile", "approval", "jumpforward", "older link", "still loads",
                )), name + " must retain South Dakota sources, platforms and ARMS approval gate")
        require(all(phrase in fallback_notes for phrase in (
                    "typeahead", "email/mobile", "free text", "height", "dropdown",
                )) and ("date-picker" in fallback_notes or "date picker" in fallback_notes),
                name + " must attach JumpForward control notes to the fallback")
    print("PASS: four dated volleyball examples, South Dakota ARMS primary/JumpForward fallback and discovery references")

    for page in markdown_pages:
        name = page.relative_to(ROOT).as_posix()
        for link in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", page.read_text(encoding="utf-8")):
            if "://" in link or link.startswith(("#", "mailto:")):
                continue
            require((page.parent / link.split("#")[0]).exists(), "Broken relative link in " + name)
    print("PASS: local Markdown links")
    print("All offline package checks passed. No live forms were used or submitted.")


if __name__ == "__main__":
    main()
