# Dry run: never press Submit

`dry-run-profile.json` is an obviously synthetic baseball athlete named **Test
Athlete**, with `test@example.com`, reserved 202-555-0100-style phones, example
addresses and deliberately fake ZIP `00000`. The only target is Illinois
Wesleyan University men's baseball, with reference candidate form
https://questionnaires.armssoftware.com/8b8ac3c4ffef. That candidate still needs
verification through the school's official athletics site. All consents are
null; all action/profile/list approvals are unset. Blank fields are intentional.
Do not replace fake values with anyone's real personal data in this file.

## Offline checks

These commands are for the helper or a package maintainer. Parents using
START_PROMPT.md never need to open a terminal; Codex handles setup and checks.

From the package folder, with Python 3 available, run:

```sh
python3 -m json.tool profile.template.json
python3 -m json.tool test/dry-run-profile.json
python3 test/validate_package.py
```

On Windows, `py -3` can replace `python3` if that is your installed Python
launcher. The validator uses only the standard library and local read-only
checks. It checks blank template values, required field coverage, fixture
safety, source-list equality/count, source integrity, ignore behavior,
relative Markdown links, personal-data patterns in all Markdown files, and
matching repository URLs in README.md and START_PROMPT.md. It never visits a
site or fills/submits a form.
It does not prove how an agent or a live form will behave.

## Rehearse the workflow

Prefer an offline review of the fixture and prompts first. Do not send fake
data to a live school merely to test this package: forms may save before Submit.
If you deliberately choose a live rehearsal, approve that disclosure separately,
verify the official link, and keep every AGENTS.md gate in force. ARMS Continue
creates a real school-side profile even without submission. Do not click it
without specific approval; stop earlier if approval is absent. Do not create
accounts, upload files, or trigger phone-based consent without their separate
approvals.
Never type, request or save passwords; the family signs in themselves.
Do not bypass CAPTCHA.

Copy this prompt in the package's Codex conversation:

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
Report needs-info with the form link and exact blockers; say explicitly that
this was a dry run and nothing was submitted. Save results only in reports/.
```

## Expected behavior checks (manual)

| Situation | Expected behavior |
|---|---|
| First run before family intake | Guide plugin/server/skill and system permissions; open example.com using Computer Use and observe Example Domain; pause intake until it works |
| Start with the baseball target | School/sport/team first, then common intake in section 4 order, then baseball only; no other sport questions |
| Required value missing, phone rejected, or position list empty | Stop that school as needs-info; never invent digits or choose a guessed position |
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

These are manual review scenarios. The form-specific findings below were
supplied from an Illinois Wesleyan dry run; the offline validator does not
repeat a live rehearsal.

## ARMS quirks: Illinois Wesleyan men's baseball

The supplied dry-run findings refer to
https://questionnaires.armssoftware.com/8b8ac3c4ffef. Verify the official athletics
link and current page before use; these observations do not grant any approval.

- The landing page offers Google, Twitter or "Continue without one of these accounts".
  Always choose continue-without, after the separate ARMS/profile-creation approval.
- "Visitor Details" asks for first name, last name and email and says it is used
  "to Create a Profile". Treat it as sending data. Proceed only after full-profile
  and final-school-list approval, with profile-creation and live-rehearsal
  disclosure approvals as well. In a dry run never go past this step unless
  the data is fake. Submission remains disabled.
- Position is single-select: 1b, 2b, 3b, C, Lhp, Mif, Of, Rhp, Ss. Ask for the
  family's primary position. The fixture supplies SS, meaning shortstop.
- High school is a typeahead. If it is missing, "Add a new high school?" requires
  the school's address, city, state, ZIP and "Does your school have an American
  Football Team?" Ask the family for these values during real intake. The
  template already has `high_school.address` and `has_american_football_team`;
  the fixture already supplies an example address and a fake No answer.
- The phone field has a country-code widget: click it and type the digits.
  Verify the country code and number; all populated fixture phone fields use
  `202-555-01xx`, such as `202-555-0100`.
- Dropdowns use Angular Material overlays. State only appears after Country
  is set. Select Country first and inspect the displayed options.
- This form had no bats/throws fields and no consent or opt-in boxes. Do not
  put the fixture's bats/throws answers in unrelated fields. If the live form
  changes, follow the live-wording review and the Opt-in rule in AGENTS.md.
