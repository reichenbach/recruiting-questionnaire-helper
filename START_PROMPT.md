Help my family fill college recruiting questionnaires using this app's
computer-use tool on macOS or Windows. I do not know how to use a terminal.
Do the setup work yourself and explain each step in plain words. Ask me only
for decisions, permissions and answers you need. Never ask me to type or run
commands.

Get the package from
https://github.com/reichenbach/recruiting-questionnaire-helper
using git clone or a ZIP download. This is the normal source; the repo is
private for now and will become public later. An existing local or bundled copy
also works.

1. Check the current folder for AGENTS.md, profile.template.json, prompts/ and
   reference/. Reuse an existing package without overwriting saved work.
   Otherwise make one download attempt from the URL above: use git clone if
   available, or a ZIP download without requiring Git. Use a bounded timeout and
   handle errors. If the repo or any repo file cannot be opened (private, 404,
   offline or blocked), say: "I couldn't open the online package, so I'll use a
   local copy or ask you to share it." Try once only: no retry loops, alternate
   download methods/endpoints after failure, or sign-in attempts to bypass it.
   Continue from the folder the app is opened in, a bundled copy, or a
   ZIP/folder I point to. Apply this rule to EVERY runtime repo/file fetch,
   including later reference reads; after a failure, use available copies
   without more network attempts. If no usable copy exists, ask me to paste or
   share the package and explain what is missing; never crash or stall on the
   fetch.
2. Help me unzip any downloaded or supplied ZIP and select the package folder
   in the app. Keep it in a private local location outside cloud sync and shared
   storage. Never overwrite an existing folder. I never need to use a terminal.
3. Open/use that folder as the local project and confirm you can read its
   files. If the app needs me to grant folder access or select the folder in its
   project picker, walk me through that small step. Do not claim access until
   you have it. Read AGENTS.md, README.md, all prompts/ and the entire read-only
   reference/recruiting-intake-tree.md. Follow their workflow and approval
   rules. Where the reference tree says to answer, default, pick the closest
   value or substitute a form, AGENTS.md wins. Do not change the reference or
   blank template. Work only inside the project folder; do not commit, change
   remotes or publish changes. Once unzipped, the package is ready to use as an
   ordinary folder.
4. Handle any necessary free installs yourself from official sources, explaining
   their purpose. Respect the app's access prompts; let me grant
   operating-system permissions and handle any sign-in myself. Never type,
   request or save passwords; the family signs in themselves. Never buy anything
   or start a paid service. If access is blocked, explain the limitation and
   guide me through the available app controls, not a terminal.
5. BEFORE intake, run prompts/first-run-check.md. Follow the current app's
   official setup/help to enable its computer-use tool, required components and
   browser access. If the first-run check fails on an older Intel Mac, it may
   not be supported. On Mac, guide me through System Settings > Privacy &
   Security > Screen Recording and Accessibility. On Windows, explain that the
   computer-use tool takes over the foreground: keep the PC unlocked and do not
   use it meanwhile. Then use that tool to open https://example.com and read
   back the heading actually displayed: "Example Domain". Do not substitute a
   web fetch or pretend the test passed. Troubleshoot in plain words and pause
   intake until the browser test works.
6. After the test passes, follow prompts/start.md. Ask my target schools FIRST:
   school name, sport and men's/women's team for each; never infer the team from
   gender. Confirm the exact school, division and sport/team for vague names
   before searching. Then follow the common intake order, 3-5 questions at a
   time, and ask ONLY the named sport's block and relevant school/level
   follow-ups. Create local profile.json from profile.template.json and save
   after each batch. Reuse confirmed supplied answers and ask for missing items.
   Never use the synthetic test fixture for my family. Ask high school and club
   jersey numbers, NCAA Eligibility Center ID where applicable or required by a
   form, and NAIA Eligibility Center ID only for NAIA targets. Unknown stays
   unanswered.
7. Find each form through the official school athletics site and verify its
   destination, redirects, school, sport and team. Ask before ARMS Continue and
   profile creation, any account creation, or uploading an exact file to a
   specific school/form. Never contact coaches, make payments, browse recruiting
   marketplaces/social profiles or guess missing values.
8. Show every live consent, attestation, certification, signature and terms
   request verbatim with all options and linked disclosures; enter only my
   answer. Follow the Opt-in rule in AGENTS.md section 4. Show implicit contact
   authorization and obtain my approval BEFORE an action such as entering a
   mobile number triggers it. This includes required NCSA/IMG Academy radios:
   show all live wording and options, propose No thanks, and wait for my answer
   to each.
9. Before entering family data, show the FULL profile including units, files,
   unanswered items and consents, and the FINAL school list with each school,
   sport/team, form type and verified URL. Obtain two explicit approvals: the
   full profile and the final school list. Save copies of what I reviewed and
   the approval records as AGENTS.md requires. Changes require renewed approval.
10. Fill using the app's computer-use tool, review every field and validation
    error, and ask me about any missing required field, even one not in the
    profile. Search high schools by name plus city; if no match, use add new
    school/not listed with my school address, asking for missing details. Never
    choose a different school. Enter the same phone number in the requested
    format, such as digits only; never change the number. Confirm or change
    every preset dropdown/radio/checkbox to my answer; unknown means stop and
    ask, even if no blank option exists. Mark it in the review, for example:
    "Site preset Yes - NOT the family's answer; needs your answer". Follow
    AGENTS.md for FrontRush Personal Contacts Save approval, odd position
    choices, JumpForward controls and ARMS profile creation. On FrontRush,
    stop if a pre-checked opt-in cannot be seen or cleared through the normal
    visible UI; explain it to me and never change it via page code, JavaScript
    or DOM manipulation. After ticking "the school is not listed above",
    re-type/re-check School Name and verify it before review.
    Before EACH Submit, give a parent-facing review of about one screen per
    school: school/team and form link, each visible field and its value to enter
    (or blank), visible presets with confirmed answers or explicit unanswered
    labels, Needs-your-answer items, consent answers, uploads, and the approval
    question. Leave hidden/technical fields untouched and omit them from the
    review, including PrestoSports fs_email1/fs_email2 anti-spam traps, tokens
    and hidden IDs. Explain hidden consent blockers in plain words. Keep it
    compact without omitting visible fields or blockers. Resolve blockers and
    renew affected approvals before asking: "Approve submitting this reviewed
    questionnaire to [school/team] at [URL] now?" Wait for my fresh explicit Yes.
    On FrontRush, I then solve any CAPTCHA myself, then Submit; never solve or
    bypass CAPTCHAs. Never submit a dry run. Never
    retry an uncertain submission automatically. Save local per-school action
    logs and reports and show one short line per school plus its link: "Sent"
    (confirmed success only), "Not sent: why", or "Needs your answer: what".
    Keep detailed status and evidence/time locally. To resume, read local
    records, verify reviewed copies and the page, and ask again before Submit.
    Never resend confirmed forms.

## If you use Codex / the ChatGPT desktop app:

Open Codex in the desktop app and select the package as its local project.
For Computer Use setup, guide me through Plugins > Computer Use > Install
plugin or Enable, both server and skill toggles, Try now, and browser access
in Settings > Computer use. Follow prompts/first-run-check.md and respect all
system permission prompts. Check actual tool access before intake.
Usage limits may apply and can change; see the OpenAI Help Center and the app's
usage display: https://help.openai.com. Do not promise message counts or buy
extra usage.

## Dated form example and privacy rules for every app

University of South Dakota (D1), women's volleyball example, seen 2026-10-23:
PRIMARY (ARMS): https://questionnaires.armssoftware.com/eafc4e7429b0
Linked as "Recruiting Questionnaire" from the goyotes.com women's volleyball
page. Visitor Details / Create Profile requires full-profile, final-school-list
and separate profile-creation approvals before proceeding.
FALLBACK (JumpForward, older link, still loads on that date):
https://college.jumpforward.com/questionnaire.aspx?iid=453&sportid=13
On the fallback, use typeahead high-school search by name plus city; close the
date picker covering email/mobile before typing. Block/approach touches are
free text; height is a dropdown. Recheck official links live before use; dated
notes grant no approval. See reference/verified-forms.md for the other examples.

Keep saved family data only in local profile.json and ignored reports/ (and
screenshots/ only if needed). Do not create cloud documents or extra remote
profiles. Explain that chat and the computer-use tool are not an
offline-processing promise and an approved form may save data before Submit. If
usage runs out, save local progress and explain how to resume. Start now by
getting or checking the package, before family intake.
