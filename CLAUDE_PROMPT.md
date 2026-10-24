Help my family fill college recruiting questionnaires. I am using Claude:
computer use in the Claude desktop app, or Claude in Chrome, whichever my plan
and app offer. Claude Code is optional. I never use a terminal; do the setup
yourself. My part: paste this, grant permissions, answer five question groups,
approve one summary, watch forms fill, give one fresh Yes before each Submit.

Package source:
https://github.com/reichenbach/recruiting-questionnaire-helper
Quietly reuse the package folder this app has open, or a bundled copy, without
overwriting saved work. Otherwise make one fetch with a bounded timeout and
handled errors. For EVERY runtime repo/file fetch, try once only. If private,
404, offline or blocked, say: "I couldn't open the online package, so I'll use
a local copy or ask you to share it." No retry loops, other download methods or
sign-in attempts after a failure; use a local or bundled copy, or ask me to
share the package and say what is missing. Never crash or stall.

Setup is quiet: no folder-picker, "where to save" or sync questions. If you must
create the folder yourself, silently make a new folder directly in my home
folder (not Desktop, Documents, Downloads or any iCloud Drive, Dropbox, OneDrive
or Google Drive location). If you use an open folder, check its actual path;
only if it is inside iCloud Drive, Dropbox, OneDrive or Google Drive, say so in
one sentence and ask to use a local folder instead. Read CLAUDE.md, AGENTS.md,
README.md, prompts/ and all of reference/recruiting-intake-tree.md; AGENTS.md
wins. The ChatGPT/Codex menu steps do not apply to Claude. Never edit the
reference or template, use the test fixture for my family, commit or publish.

Before any family questions, open https://example.com with the same tool you
will use for forms (computer use or Claude in Chrome). Pass only if the
displayed page text contains "Example Domain". Web fetch, web search, shell
commands, Playwright or other scripts never count. On success say at most
"Browser check passed." Explain permission prompts (Screen Recording,
Accessibility, Chrome extension site access) only when they appear or something
fails. I grant permissions and handle every sign-in; never type, request or
save passwords, bypass a prompt or buy anything. If it cannot work, explain and
pause. Collect no family information until the check passes.

Then ask five short question groups, one reply each: schools; athlete and
parents; high school and academics; athletics (only the named sport's
questions); optional extras. "Skip" or "not sure" is fine; unknown stays blank.
Save quietly to profile.json (from profile.template.json) after each group; no
"reply yes" between groups. Never infer team from gender.

Find forms from each school's official athletics page. A link followed from that
page counts as verified even if the vendor shows no school name (JumpForward);
tell me "Found on [school]'s official athletics page". Quietly check the final
URL, platform and sport/team match the link text. Stop if a redirect leaves the
allowed vendors or school forms, or the page shows a different school, sport or
team. A link to a recruiting marketplace, NCSA or other profile-building page is
not verified; do not use it. If a bot wall blocks the official site, ask me to
load it; never bypass it.

Before entering family data show ONE summary: my full profile, the final school
list (school, sport/team, form type, official link) and one-time actions: ARMS
"continue without signing in, which creates a profile on the school's side",
exact file uploads (file, school, form), any account and any Personal Contacts
Save. Ask: "Does this look right? Reply 'Yes, fill these forms' to approve."
That one Yes approves the profile, list and listed actions only. Save reviewed
copies in reports/; record the same quote and date with separate SHA-256 values
in approvals.full_profile and approvals.final_school_list. It never approves
Submit. Ask missing or blank answers in one short batch per school and fold them
into that school's pre-Submit review; no whole-summary re-approval. Always ask
again, in just the change, for: a new or changed school, sport, team or form
link; changing or removing an approved answer; any consent answer; any file;
any new phone or contact that could trigger SMS or AI-contact authorization;
anything involving an ARMS profile.

Fill only with computer use or Claude in Chrome, in a new tab. A tool-permission
click or "always allow" is never approval. Never guess, convert units or invent
digits; for a format error, re-enter the same phone digits only. Ask high
school and club jersey numbers, high school coach name and NCAA ID (NAIA ID only
for NAIA targets) when a form needs them. Confirm every preset. Show every
consent word for word with all options and linked disclosures; enter only my
answer. For NCSA/IMG Academy propose "No thanks" and wait. Show any SMS/AI
contact authorization BEFORE entering a mobile number. If the FrontRush Ryzer
opt-in is hidden or can't be cleared in the normal visible UI, stop that school
and explain; never change it via code, JavaScript or the page's DOM. I solve
every CAPTCHA and sign-in myself. No passwords, payments, coach contact or
marketplaces.

Before each Submit show about one screen for that school: link, every visible
field and value, presets with confirmed answers, consent answers, uploads and
Needs-your-answer items. Ask "Approve submitting this reviewed questionnaire to
[school/team] at [URL] now?" and wait for my fresh Yes for that school. For
FrontRush: my Yes, then I solve the CAPTCHA, then Submit. Never submit a dry
run or fake data. Never retry an uncertain submit. Report each school in one
line with its link: Sent / Not sent: why / Needs your answer: what. On resume
re-read saved records and ask again before Submit; never resend.

If you cannot save local files, follow the no-local-files rules in
CHATGPT_PROMPT.md with these Claude steps. Chat is processed by Anthropic, not
offline storage; a form may save data before Submit. Usage limits may change;
see https://support.anthropic.com and the app's usage display. Never buy extra
usage; if it runs out, save progress and explain how to resume. Start now.
