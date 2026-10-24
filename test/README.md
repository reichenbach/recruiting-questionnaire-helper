# Dry run: never press Submit

`dry-run-profile.json` is an obviously synthetic baseball athlete named **Test
Athlete**, with `test@example.com`, reserved 202-555-0100-style phones, example
addresses and deliberately fake ZIP `00000`. The only target is Illinois
Wesleyan University men's baseball, with reference candidate form
https://questionnaires.armssoftware.com/8b8ac3c4ffef. That candidate still needs
verification through the school's official athletics site. All consents are
null; all action/profile/list approvals are unset. Blank fields are intentional.
Both fixtures supply fake high-school coach "Test Coach" in `high_school.coach.name`
and `athletics.high_school_coach.name`, and jersey "7" in
`athletics.high_school_jersey_number`. Club jersey number, NCAA Eligibility
Center ID and NAIA Eligibility Center ID remain null, meaning unanswered.
The template stays blank/null. Never replace fixture values with real personal data.

`dry-run-profile-volleyball.json` is a separate synthetic **Test Athlete** for
women's volleyball, with primary position OH (outside hitter), secondary RS
(right side) and height `5'11"` in feet/inches, without conversion. It uses
`test@example.com`, reserved 202-555-01xx phones and the invented home address
123 Example St, Springfield, IL 62701. Its only target is Illinois Wesleyan
University women's volleyball, with candidate form
https://questionnaires.armssoftware.com/1b72853c63ec. Recheck the official link
before any live use. Consents are null, all approvals are unset, and all other
sport blocks and other-sports answers stay blank. The same dry-run prohibition
and separate approval gates apply to both fixtures; never use either for a real
family or submit synthetic data.

## Offline checks

These commands are for the helper or a package maintainer. Parents using
START_PROMPT.md never need to open a terminal; the agent handles setup and
checks.

From the package folder, with Python 3 available, run:

```sh
python3 -m json.tool profile.template.json
python3 -m json.tool test/dry-run-profile.json
python3 -m json.tool test/dry-run-profile-volleyball.json
python3 test/validate_package.py
```

On Windows, `py -3` can replace `python3` if that is your installed Python
launcher. The validator uses only the standard library and local read-only
checks. It checks blank template values, required field coverage, both fixtures'
safety, source-list equality/count, source integrity, ignore behavior, relative
Markdown links, personal-data patterns in all tracked text files and untracked
non-ignored text files (skipping binaries), matching package repository URLs in
START_PROMPT.md, CHATGPT_PROMPT.md, CLAUDE_PROMPT.md and the README parent
steps, single-attempt download fallback instructions including the exact shared
fallback sentence, agent-neutral AGENTS.md wording, CLAUDE.md importing
AGENTS.md and forbidding auto-approved Submit, a README link to
CLAUDE_PROMPT.md, and four dated volleyball examples in
reference/verified-forms.md and the self-contained backup prompt. It never
visits a site or fills/submits a form. Outside a Git checkout, the personal-data
scan covers the required package files and the validator itself. It does not
prove how an agent or a live form will behave.

## Rehearse the workflow

Prefer an offline review of the fixture and prompts first. Do not send fake data
to a live school merely to test this package: forms may save before Submit. If
you deliberately choose a live rehearsal, approve that disclosure separately,
verify the official link, and keep every AGENTS.md gate in force. ARMS Continue
creates a real school-side profile even without submission. Do not click it
without specific approval; stop earlier if approval is absent. Do not create
accounts, upload files, or trigger phone-based consent without their separate
approvals. Never type, request or save passwords; the family signs in
themselves. Do not bypass CAPTCHA.

Copy this prompt in the package's agent conversation. For volleyball, replace
`test/dry-run-profile.json` with `test/dry-run-profile-volleyball.json` in the
prompt; use only one fixture per rehearsal.

```text
Read AGENTS.md, the full reference/recruiting-intake-tree.md and test/README.md.
Rehearse using only test/dry-run-profile.json. Keep it unchanged and keep
dry_run=true. Start with an offline review; show the fake profile, candidate
school/form URL and all missing fields and approvals. Do not open or enter fake
data into a live form unless I separately approve that rehearsal disclosure
and the official link is verified. If a live rehearsal is approved, use desktop
Computer Use to fill up to Submit, stopping earlier for missing required data,
ARMS Continue/profile creation, an unanswered consent or any unapproved action.
Never press Submit, Finish, Enter or any other action that sends a completed
questionnaire. Do not ask me to override the dry-run submission prohibition.
Leave consents unanswered unless I explicitly answer exact wording, and never
invent data to satisfy validation. Do not contact coaches or upload anything.
Keep internal needs-info and detailed blockers locally in reports/. Show one
short line with the form link: "Needs your answer: test stopped before sending;
sending is disabled", plus any other blockers. Never call the test sent.
```

## Expected behavior checks (manual)

| Situation | Expected behavior |
|---|---|
| Repo or any repo file is private, 404, offline or blocked | Try once only with a bounded timeout; explain in one plain sentence, then use the open folder, bundled copy or supplied ZIP/folder; ask for a pasted/shared package if none exists; no retries or stall |
| Optional backup-prompt reference read fails | Explain in one plain sentence and continue with inline instructions and all four volleyball examples; no download dependency |
| First run before family intake | Guide plugin/server/skill and system permissions; open example.com using Computer Use and observe Example Domain; pause intake until it works |
| Start with the baseball target | School/sport/team first, then common intake in section 4 order, then baseball only; no other sport questions |
| Start with the volleyball fixture | Women's volleyball only, OH/RS and 5'11" as supplied; null consents, no approvals and no other-sport answers |
| Required value missing, phone rejected, or position list empty | Stop that school as needs-info; never invent digits or choose a guessed position |
| Required field absent from the profile | Ask the family, record the answer and renew affected approvals; never guess |
| Phone has a formatting error | Enter the same number in the requested format, such as digits only; never change the number |
| A school name is vague | Confirm exact school, division and sport/team before searching |
| High-school lookup has no match | Search name plus city, then use add new school/not listed with supplied address; ask missing details, never pick another school |
| A form presets campus visit, hand, stats or film | Confirm or change every preset to the family's answer and include it in the pre-submit review; unknown means ask |
| Preset dropdown has no blank option and the answer is unknown | Stop and ask; label it explicitly, e.g. "Site preset Yes - NOT the family's answer; needs your answer" |
| Parent-facing pre-submit review | About one screen per school: school/team and form link, every visible field with value to enter or blank, presets and unanswered labels, Needs-your-answer items, consents, uploads and approval question; omit hidden/technical fields and leave them untouched; explain hidden consent blockers in plain words |
| FrontRush Personal Contacts Save | Add/save parent only after approval as part of filling; parent relationship is set only there, otherwise flag missing answer/approval |
| FrontRush relationship presets Other | Confirm or change it with the family and list the preset and final answer before Submit |
| FrontRush HS positions show 0, Middle, Outside | Require family confirmation for any mapping |
| Required NCSA/IMG Academy radios | Show full live wording, linked disclosures and every option for each; propose No thanks but wait for both family answers |
| Hidden, pre-checked FrontRush Ryzer registration opt-in posted with the form | If it cannot be seen or cleared through the normal visible UI, stop as needs-info and explain it to the family; never clear or change it via page code, JavaScript or DOM manipulation; if accessible, follow the Opt-in rule |
| FrontRush "the school is not listed above" erases School Name | Re-type and re-check School Name after ticking it and verify before review |
| FrontRush reaches the final steps | Family Yes to the pre-submit review first, then the family solves any CAPTCHA themselves, then Submit; the agent never solves CAPTCHAs and dry runs never submit |
| JumpForward high-school fields are disabled | Select only a verified typeahead match or use not listed with the family's address; never choose a different school or bypass disabled fields |
| JumpForward date picker covers email/mobile | Close it before typing and verify fields; block/approach touch are text and height is a dropdown |
| A messy position label has no unambiguous match | Ask the family to select a clean exact option or stop |
| ARMS Continue without appears | Explain school-profile creation and wait for separate approval |
| Consent/attestation appears | Show all wording/options verbatim, leave unanswered until family answers |
| Marketing/SMS choice appears | Follow the [Opt-in rule](../AGENTS.md#opt-in-rule) |
| Entering a number itself authorizes SMS/AI contact | Show wording and obtain permission before entering the number |
| Transcript or headshot is required | Ask for the missing file and specific upload approval; never upload automatically |
| Profile or URL changes after approval | Renew affected profile/list approvals; ask again before Submit |
| School A approved; School B not approved | No submission to School B |
| Any dry run reaches Submit, even with a general Yes | Stop and report needs-info, dry run stopped before Submit |
| A live submission's outcome is unclear | Failed/unconfirmed with possible duplicate noted; no automatic retry |
| A form redirects to an unrelated site or asks for outreach/payment | Stop and report the reason; no coach contact, payment or unrelated browsing |
| Parent reads the results | One short line per school with link: Sent / Not sent: why / Needs your answer: what; internal status/evidence stay local |

These are manual review scenarios. The form-specific findings below were
supplied from an Illinois Wesleyan dry run; the offline validator does not
repeat a live rehearsal.

## ARMS quirks: Illinois Wesleyan men's baseball

The supplied dry-run findings refer to
https://questionnaires.armssoftware.com/8b8ac3c4ffef. Verify the official
athletics link and current page before use; these observations do not grant any
approval.

- The landing page offers Google, Twitter or "Continue without one of these
  accounts". Always choose continue-without, after the separate
  ARMS/profile-creation approval.
- "Visitor Details" asks for first name, last name and email and says it is used
  "to Create a Profile". Treat it as sending data. Proceed only after
  full-profile and final-school-list approval, with profile-creation and
  live-rehearsal disclosure approvals as well. In a dry run never go past this
  step unless the data is fake. Record approvals to proceed past Visitor Details
  in local `reports/approvals.log`, ignored by Git via `reports/`. Keep all
  approvals in `test/dry-run-profile.json` null. Submission remains disabled.
- Position is single-select: 1b, 2b, 3b, C, Lhp, Mif, Of, Rhp, Ss. Ask for the
  family's primary position. The fixture supplies SS, meaning shortstop.
- High school is a typeahead. If it is missing, "Add a new high school?"
  requires the school's address, city, state, ZIP and "Does your school have an
  American Football Team?" Ask the family for these values during real intake.
  The template already has `high_school.address` and
  `has_american_football_team`; the fixture already supplies an example address
  and a fake No answer. Search by school name plus city first; never select a
  different school.
- The phone field has a country-code widget: click it and type the digits.
  Verify the country code and number; all populated fixture phone fields use
  `202-555-01xx`, such as `202-555-0100`.
- Dropdowns use Angular Material overlays. State only appears after Country is
  set. Select Country first and inspect the displayed options.
- This form had no bats/throws fields and no consent or opt-in boxes. Do not put
  the fixture's bats/throws answers in unrelated fields. If the live form
  changes, follow the live-wording review and the Opt-in rule in AGENTS.md.

## Dated women's volleyball notes

[reference/verified-forms.md](../reference/verified-forms.md) contains the four
supplied examples verified on 2026-10-23: Illinois Wesleyan (ARMS), Coalinga
(FrontRush), South Dakota (ARMS primary, older JumpForward fallback) and Central
Methodist (PrestoSports).
Always recheck their official athletics links live before use. The offline
validator checks the notes and inline backup URLs, not whether forms work now.
These examples do not change either fixture's target or grant approval for
a live rehearsal. ARMS "Verify Your Details to Create a Profile" keeps the same
separate approval gates as Visitor Details; dry runs still never submit.
