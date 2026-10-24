Help my family fill college recruiting questionnaires using this app's
computer-use tool on macOS or Windows. Handle setup yourself; I never need a
terminal. My flow: paste this prompt, grant permissions, answer five question
groups, approve one summary, watch forms fill, give one fresh Yes per Submit.

Quietly use the package folder the app is opened in. If it is missing, the
PUBLIC package source is:
https://github.com/reichenbach/recruiting-questionnaire-helper
Use an existing local/bundled copy first, without overwriting saved work.
Otherwise use git clone or ZIP (Git is optional) with a bounded timeout and
handled errors. For EVERY runtime repo/file fetch, try once only. If private,
404, offline or blocked, say:
"I couldn't open the online package, so I'll use a local copy or ask you to share it."
No retry loops, alternate download methods/endpoints or sign-in attempts after
failure. Use the open folder, bundled copy or supplied ZIP/folder without more
network attempts after failure. If none is usable, ask me to paste or share the
package and explain what's missing; never crash or stall. Do not invent rules.

Unzip if needed, quietly check file access and actual folder path. No folder
picker or "where should I save it" questions unless you cannot read the files;
then guide that small step. Only if inside iCloud Drive, Dropbox, OneDrive or
Google Drive, say so in one sentence and ask permission to use a local folder
instead before saving data. Otherwise do not ask about sync. Work only inside
the package folder. Read AGENTS.md, README.md, prompts/ and the whole read-only
reference/recruiting-intake-tree.md; AGENTS.md overrides its suggestions to
guess/default/substitute. Never edit the reference/template or use fixture data
for my family. Do not commit, change remotes or publish.

Before intake run prompts/first-run-check.md quietly, handling necessary free
setup from official sources within app permissions. Use the actual computer-use
tool at https://example.com and inspect the browser: displayed page text must
contain "Example Domain". A search, HTTP fetch or shell cannot pass. On success
say at most "Browser check passed." Explain setup/permissions, Intel Mac support
or Windows foreground details only on failure or a permission prompt. I grant
system permissions and handle sign-in; never bypass prompts or type, request
or save passwords. Pause intake until the real check passes.

Send FIVE plain-language question groups, one short message and one reply each.
I can say "skip" or "not sure"; unknown stays blank, never guessed. Save quietly
after each group to ./profile.json from profile.template.json. No "reply yes to
continue" gates. Reuse supplied answers; keep every reference section 4 field
reachable through optional additions or actual required form questions.

1. Schools: school, sport, men's/women's team for each, graduation year, target
   levels. Never infer team from gender; clarify vague school/division/team
   before searching.
2. Athlete and parents: full/preferred names, contacts, address, DOB, guardian
   relationships/names/contacts and different addresses.
3. High school and academics: school/address, coach/counselor, GPA/scale, test
   scores/dates, major, entry/transfer plans, NCAA Eligibility Center registration/
   ID where applicable; NAIA PlayNAIA ID only for NAIA targets.
4. Athletics: height/weight with units, positions, club team/coach, high school
   and club jersey numbers, videos, events, honors; ONLY the named sport's block
   and relevant level/school follow-ups, reusing common answers.
5. Optional extras: anything else, such as social accounts, family/education,
   academic extras, hobbies or files. Sensitive optional answers can be skipped.

Public discovery may start after group 1. A questionnaire link followed from the
school's official athletics page counts as verified even if the vendor shows no
school name. Record the link chain in target_schools. Stop if no official
athletics source, redirects leave allowed vendors/school forms, or the page
visibly shows a different school/sport/team. Tell me "Found on [school]'s official
athletics page". Stay on official athletics pages and linked vendor forms;
never visit supplied social/video/profile links or marketplaces.

Before entering family data show ONE summary: full profile (all values, units,
files, unanswered items, consent records), final school list with sport/team,
form type and official form link for each, and exact one-time actions requested.
For ARMS name "continue without signing in, which creates a profile on the
school's side" plus Visitor Details/Create Profile disclosure; uploads name the
exact file, school and form. Account creation and Personal Contacts Save must
also be listed specifically or approved later. Ask once: "Does this look right?
Reply 'Yes, fill these forms' to approve." One Yes approves profile and list
and only listed actions; never ask separate profile/list approvals. Save local
reports/ copies and record the same quote/date with separate SHA-256 values in
approvals.full_profile and approvals.final_school_list; record listed actions
as school_actions. This is never permission to Submit.

While filling, ask new required/previously blank answers in ONE short batch per
school, save and log locally, and fold them into that school's pre-Submit review;
its Submit Yes covers additions without repeating the whole summary. Confirm
just the change before changing/removing approved answers, adding a school or
changing a form link. Retain original approvals/copies; log additions/changes.
Show each consent/attestation/signature/terms item verbatim with every option
and needed linked disclosures when it appears; enter only my own answer, once
per item unless wording changes, and show it again in the final review. Show
implicit SMS/AI-contact notices and get approval BEFORE the triggering action.
Opt-ins default off; required choices need my answer. Propose No thanks for
NCSA/IMG Academy, but never choose for me.

Fill only through computer-use; review every field and validation error. Never
guess, calculate, convert units or invent digits. Preserve values and units;
phone punctuation may change, never the number. Follow AGENTS.md's platform
rules: high-school typeahead matches must be correct (JumpForward uses school
name only and has no not-listed option); never choose a different school or
bypass disabled controls. Confirm every preset; unknown means stop and ask,
even without a blank option: "Site preset Yes - NOT the family's answer; needs
your answer". For FrontRush Ryzer opt-ins unseen or uncleared through normal
visible UI, stop and explain; never change via code/JavaScript/DOM. Recheck
Coalinga School Name after ticking not listed. No coach contact or payments.

Before EACH Submit give about one screen per school: school/team/link, EVERY
visible field and value or blank, presets/final answers, unanswered labels,
Needs-your-answer blockers, new answers, consents and uploads. Leave hidden/technical
fields untouched and omit them (including anti-spam traps, tokens,
hidden IDs); explain hidden consent blockers plainly. Resolve blockers and
confirm changes, then ask "Approve submitting this reviewed questionnaire to
[school/team] at [URL] now?" Wait for my fresh explicit per-form Submit Yes.
One school never covers another, a retry or resubmission. FrontRush order:
family Yes first, then family solves CAPTCHA themselves, then Submit. Never
solve/bypass CAPTCHA. Never submit fake data or a dry run, even if later asked.
Never send via Enter/Next/Finish early or retry uncertain submissions
automatically. Save local per-school logs/reports; show Sent (confirmed only) /
Not sent: why / Needs your answer: what with links. On resume verify local
copies, logs and page state and ask again before Submit; never resend confirmed
forms.

For Codex / ChatGPT desktop, only if setup is needed: Plugins > Computer Use >
Install plugin or Enable, both server and skill toggles, Try now, browser access
in Settings > Computer use. Respect system prompts and check actual access.
Usage limits may change; see https://help.openai.com and the app usage display.
Do not promise message counts or buy extra usage.

## Dated form example and privacy rules for every app

University of South Dakota (D1), women's volleyball example, seen 2026-10-23:
PRIMARY (ARMS): https://questionnaires.armssoftware.com/eafc4e7429b0
Linked as "Recruiting Questionnaire" from the goyotes.com women's volleyball
page. Visitor Details / Create Profile requires approval of the profile, school
list and that specific profile-creation action; all may be in the one summary.
FALLBACK (JumpForward, older link, still loads on that date):
https://college.jumpforward.com/questionnaire.aspx?iid=453&sportid=13
On the fallback, typeahead-search school name only, verify city; close the
date picker covering email/mobile before typing. Block/approach touches are
free text; height is a dropdown. Recheck official links live before use; dated
notes grant no approval. See reference/verified-forms.md for the other examples.

Keep saved family data only in local profile.json and ignored reports/ (and
screenshots/ only if needed). Do not create cloud documents or extra remote
profiles. Explain that chat and the computer-use tool are not an
offline-processing promise and an approved form may save data before Submit. If
usage runs out, save local progress and explain how to resume. Start now by
getting or checking the package, before family intake.
