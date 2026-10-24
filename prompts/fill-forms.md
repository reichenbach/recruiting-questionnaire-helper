Read AGENTS.md and the entire read-only reference/recruiting-intake-tree.md. Use
./profile.json and the app's computer-use tool on macOS or Windows to fill only
verified forms for the approved school/sport/team list. Use the ONE summary approval for the full
profile and final school list with form URLs and exact listed one-time actions
(see AGENTS.md). Ask once for "Yes, fill these forms" if not already approved;
never request separate profile/list approvals. Verify saved copies and logs.

Tool-permission or app-access clicks (granting computer-use, screen recording
or browser access) are NOT family approval for any form action, Submit, consent,
upload or account creation.

Use the family's exact answers only. Never guess, round, calculate missing
answers, or fill unknown required values with placeholders.
Stop that school as needs-info if a required answer or unambiguous option is
missing. Never accept a preset as an unknown answer.
Ask missing required or previously blank answers in ONE short batch per school;
include high school and club jersey numbers, high school coach and NCAA/NAIA
eligibility IDs when the form requires them, even if skipped in the five groups
(NAIA IDs only for NAIA targets). Never guess or accept presets. Save locally
with school/sport and log additions in `reports/`.

Small additions are NON-SENSITIVE fields only: extra stats, awards/honors,
hobbies, and a coach email or phone number already shown in the approved profile
or on the school's own form. Only these fold into that school's pre-Submit
review without extra confirmation; its fresh Submit Yes covers them.

For later additions or changes, always re-ask a specific question about just the
item before proceeding: a new or changed school, sport or team (and any change
to a form link or form type); any consent/attestation answer (exact live wording,
linked disclosures and all options); any file upload (exact file/school/form);
any contact or phone number that could trigger SMS/AI-contact authorization
(before entry); and anything that touches an ARMS profile (continue-without-sign-in,
Visitor Details/Create Profile). These gates override the small-additions rule.
Show each answer/action again in that school's per-Submit review. Other additions or changing/removing approved answers need
confirmation of just the change; the specific follow-up answer can provide it,
without whole profile/list re-approval. Keep original approval copies/hashes
intact. Log additions/changes, family words/date and reviewed copies/hashes as
applicable, linked to original approvals. Keep the approvals schema unchanged;
record additions in reports, not profile approvals.

Enter the same phone number in the format requested, such as digits only after a
format error (CMU requires digits-only cell numbers); never change the number
itself. Ask if it still fails. For high-school search, use name
plus city. If absent, use add new school/not listed with the family's school
address; ask if missing and never pick a different school.

Confirm or change every preset dropdown, radio and checkbox to the family's
answer. Unknown means ask. Clear preselected opt-ins under the Opt-in rule;
required choices still need the family's answer. If a dropdown has no blank
option and the answer is unknown, stop and ask; mark it in the review, for
example: "Site preset Yes - NOT the family's answer; needs your answer".
Include every visible preset choice and confirmed final answer in the
pre-submit review, including CMU campus visit,
hand, stats and film defaults and FrontRush relationship "Other". Confirm or
change "Other" with the family.

Show every consent, attestation, certification and signature request verbatim
with all options and linked disclosures; enter only the family's answer.
Leave unanswered requests blank. Follow the Opt-in rule in AGENTS.md section 4. Before entering a phone
number that itself grants SMS/AI-contact authorization, show that wording and
get approval for the action. ARMS Continue/profile creation, account creation
and uploads need specific approval, either exactly listed in the one summary
or requested later for that exact action/file/school/form.

NCSA/IMG Academy radios are required on Coalinga FrontRush: show complete live
wording and all options for each, propose No thanks and enter only the family's
confirmed answers. The form cannot be sent while either answer is missing.

Check for pre-checked FrontRush opt-ins, including Ryzer registration
(`name=ryzer_registration`) inside the hidden Recruit Spot widget, posted with
the form. If an opt-in cannot be seen or cleared through the normal visible UI,
stop that school as needs-info and tell the family what it is. Never clear or
change it via page code, JavaScript or DOM manipulation. If accessible through
the visible UI, clear it, show complete live wording, linked disclosures and
every option, and record only the family's answer in `consents.records`.
An unanswered item stays unchecked with a null answer; checking requires
explicit Yes. Include the preset and confirmed final answer in the review, or
explain an inaccessible opt-in as a Needs-your-answer blocker in plain words.

On Coalinga FrontRush, ticking "the school is not listed above" erases School
Name. Re-type and re-check School Name after ticking it; verify it before review.

FrontRush Personal Contacts has its own Save and is the only place to set the
parent relationship. Add/save a parent only after the family approves it as part
of filling; otherwise record that the relationship needs their answer and Save
needs approval. Map odd HS positions (0, Middle, Outside) only with their
confirmation.

On JumpForward, set Country first, before typing anything else. Country
defaults to United States; changing it reloads the page through a server
postback, so recheck every field after. High-school fields stay disabled until
a typeahead suggestion is selected. Search the school name only (name plus city
or ZIP finds nothing) and verify the city/state in the suggestion. It has no
not-listed option for high schools; if none matches, stop that school as
needs-info. Never pick another school or bypass disabled fields. Close the date
picker if it covers email/mobile before typing. Block/approach touch are free
text; height is a dropdown. ARMS "Verify Your Details to Create a Profile" and Visitor
Details keep every profile-creation approval gate.

Never type, request or save passwords; the family signs in themselves.

Before each Submit, give a parent-facing review of about one screen per school:
school/team and final form link; each visible field and its value to enter (or
blank); visible presets with confirmed answers or explicit unanswered labels;
Needs-your-answer items; consent answers; uploads; and the school-specific
approval question. Leave hidden/technical fields untouched and omit them from
the review, including PrestoSports fs_email1/fs_email2 anti-spam traps, tokens
and hidden IDs. Explain hidden consent blockers in plain words, not as technical
fields. Keep it compact without omitting visible fields or blockers. Resolve
blockers and confirm changes under AGENTS.md before asking: "Approve submitting this
reviewed questionnaire to [school/team] at [URL] now?" Wait for a fresh explicit
Yes for that school/attempt; one school's approval never covers another, a retry
or resubmission. On FrontRush, obtain that Yes first, then the family solves any CAPTCHA
themselves, then Submit. Never solve or bypass CAPTCHAs. Never submit a dry run or
the fake test fixture. No payments or coach contact.

Log each school with internal status and evidence/time locally in reports/. Show
one short line per school with its link: "Sent" only after confirmation, "Not
sent: why", or "Needs your answer: what". If sending is uncertain, say it may
already have gone through and do not automatically try again.

## If you use Codex / the ChatGPT desktop app:

Use its enabled Computer Use tool. If no successful browser check has been
observed in this session, follow prompts/first-run-check.md before proceeding.
