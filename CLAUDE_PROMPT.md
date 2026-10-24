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

For an agent-created package folder (download/clone/unzip), silently create a
NEW folder directly in the home directory, such as `~/RecruitingHelper`, adding
a number if the name exists; never overwrite an existing folder. Never create it
on Desktop, in Documents, or in a synced location. Say nothing about sync.

When reusing an already-open folder, quietly check the actual folder path.
On macOS, treat it as possibly synced if inside iCloud Drive, Dropbox, OneDrive
or Google Drive, or if under `~/Desktop` or `~/Documents` AND either iCloud
Desktop & Documents sync folder exists:
`~/Library/Mobile Documents/com~apple~CloudDocs/Desktop` or
`~/Library/Mobile Documents/com~apple~CloudDocs/Documents`.
On Windows, treat it as possibly synced if the path contains OneDrive, Dropbox
or Google Drive. If it is or might be synced, do NOT ask: silently copy the
package into a NEW non-synced folder directly in the home directory, using the
same naming rule; never overwrite. Preserve saved work in the copy. Work there;
save no family data in the synced location. Say one plain line only:
"I'm keeping your family's information in a private folder on this computer,
not in cloud storage." If the path is not synced, say nothing about sync.
Never ask the parent to select, confirm or describe a folder or sync status;
never ask "is it outside cloud sync". Only if the agent cannot create or open
the home folder, guide the small folder-access step in plain words.

Keep the entire pre-intake message to at most two short sentences:
"Browser check passed." plus the first question group. If the relocation line
is needed, omit the optional browser-success sentence to keep that same limit.
No privacy/processing essays, setup reports or offers to save setup reports.
Save setup notes quietly in reports/.
Read CLAUDE.md, AGENTS.md, README.md, prompts/ and all of reference/recruiting-
intake-tree.md; AGENTS.md wins. The ChatGPT/Codex menu steps do not apply to
Claude. Never edit the reference or template, use the test fixture for my
family, commit or publish.

Use the real computer-use tool to open https://example.com and inspect the
actual browser. Pass if the tab title OR displayed page text contains
"Example Domain", OR displayed page text contains "This domain is for use in"
(the documentation examples notice). No heading element is needed. Record what
the tool actually saw quietly in reports/. Expected text, web search, HTTP fetch
or shell commands cannot pass. Never ask the parent to accept a variant,
approve a changed test or choose how to pass. Troubleshoot with the parent only
if the page fails to load or the tool cannot read anything. On success say at
most "Browser check passed." Pause intake until the real check passes.

Use the same tool for forms (computer use or Claude in Chrome). Playwright or
other scripts never count. Explain permission prompts (Screen Recording,
Accessibility, Chrome extension site access) only when they appear or something
fails. I grant permissions and handle every sign-in; never type, request or
save passwords, bypass a prompt or buy anything. If it cannot work, explain and
pause. Collect no family information until the check passes.

For real-family runs: five groups -> one summary -> one Yes -> fill -> one
fresh Yes per Submit. The summary lists what will be entered into which
official form, including any specific ARMS profile-creation action. Do not add
a separate disclosure approval step, profile versions such as "v1" or "v2", or
whole-profile re-approvals. Separate live-rehearsal disclosure approval applies
only to deliberate dry-run tests on live forms, with fake data and no Submit.
Required consent, file, contact and other item-specific safety gates still apply.

Then ask five short question groups, one reply each: schools; athlete and
parents; high school and academics; athletics (only the named sport's
questions); optional extras. "Skip" or "not sure" is fine; unknown stays blank.
Save quietly to profile.json (from profile.template.json) after each group; no
"reply yes" between groups. Never infer team from gender.

The official athletics page link chain is enough when JumpForward shows no
school name. Missing branding alone never blocks verification or needs a
parent question; still stop for a visible mismatch or a blocked official site.

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
Submit. Ask missing or blank answers in one short batch per school. Ask each
blank once; after "not sure" or no answer, keep it as Needs-your-answer and do
not repeat it in later replies. Small additions are non-sensitive fields only:
extra stats, awards/honors, hobbies, and a coach email or phone number already
shown in the approved profile or on the school's own form. Only these fold into
that school's pre-Submit review without extra confirmation; its fresh Submit
Yes covers them. No whole-summary re-approval. Always ask
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
