# Recruiting questionnaire helper for families

1. **Get ChatGPT Plus** using your personal account. If you already have it,
   keep using it; this guide does not ask the helper to buy a subscription.
2. **Install the ChatGPT desktop app** from
   [OpenAI's download page](https://openai.com/chatgpt/download/).
3. **Paste all of [START_PROMPT.md](START_PROMPT.md) into Codex** in the desktop
   app. Codex gets the repo, sets it up, checks Computer Use, then asks questions.
   You never need a terminal or commands.

Share this GitHub repo together with the single copy-paste prompt in
[START_PROMPT.md](START_PROMPT.md). Before sharing, replace its
`https://github.com/reichenbach/<repo>` placeholder with the actual repo URL in
the copy you send. The checked-in prompt deliberately keeps that placeholder.
Codex can clone the repo or download its ZIP if git is missing; it does not
require the parent to download, unpack or install developer tools themselves.

This folder helps a parent and athlete prepare one local profile, find official
college recruiting questionnaires, and fill them using Codex and Computer Use
in the ChatGPT desktop app. It is intended for families using ChatGPT Plus.
You stay involved: review the answers, school list, consent wording and each
completed form before approving a submission.

It fills forms only. It never contacts coaches, sends emails or messages, makes
calls, pays fees, or buys services. It cannot promise admission, eligibility,
recruiting interest or a scholarship. It asks before creating an account or
school profile, entering passwords, or uploading any file. It stops a school
when required information is missing rather than making up an answer.

## Set up on Mac or Windows

1. Download the ChatGPT desktop app from [OpenAI's official
   site](https://openai.com/chatgpt/download/). See the [OpenAI Help
   Center](https://help.openai.com) for installation help. Use your personal account.
2. Computer Use is available in supported regions on macOS and Windows. In the
   app choose **Codex** (or ChatGPT **Work**). Open **Plugins > Computer Use**,
   choose **Install plugin** or **Enable**, turn on the **Computer Use server**
   and **skill** toggles, then choose **Try now**.
3. **Settings > Computer use** shows app access and **Always-allowed apps**.
   ChatGPT asks permission before using an app; review the request.
4. **Mac:** this package's workflow requires Apple Silicon (M1 or newer). When prompted,
   grant **Screen Recording** and **Accessibility** in **System Settings >
   Privacy & Security**.
5. **Windows:** Computer Use takes over the active desktop's pointer, keyboard
   and foreground. Keep the PC unlocked and do not use it while the task runs.
   A Windows virtual machine is an option.

Before intake, Codex follows [the first-run check](prompts/first-run-check.md),
opens `https://example.com` using Computer Use and reads back **Example Domain**
from the page. If the test fails, it helps fix the setup in plain words and
pauses intake until the test works. Availability depends on the account, region,
device and permissions; Plus alone is not a guarantee that the tool is enabled.

These setup instructions use [OpenAI's Computer Use
guide](https://learn.chatgpt.com/docs/computer-use). Apple Silicon is this
package's Mac requirement; see the current [desktop app requirements](https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app)
for the app's broader hardware support.

## Let Codex get the folder and start

Paste [START_PROMPT.md](START_PROMPT.md) into Codex. It chooses a private local
folder, retrieves the repo and handles any necessary free installs. It explains
where the files are and walks you through any folder-access or system permission
prompts that need your clicks. Keep the folder outside cloud sync and shared
storage. No terminal work is required from the parent.

If you already have the folder, Codex can reuse it without replacing saved work.
If the app asks you to choose a project folder, select the folder containing
`AGENTS.md`, `profile.template.json`, `prompts/`, and `reference/`, rather than
opening an individual file. If you need help locating the folder-opening
controls in your app version, see the [OpenAI Help Center](https://help.openai.com).
Ask Codex to confirm that it can read `AGENTS.md` and the reference before
sharing family information. No command-line setup is needed to use the prompts.

For an already-open package, this shorter stage prompt is also available
(the full first-time setup prompt remains START_PROMPT.md):

```text
Read AGENTS.md and the entire reference/recruiting-intake-tree.md in this folder.
Before intake, run prompts/first-run-check.md and pass the Computer Use browser
test. Walk me through setup in plain words; I never need to use a terminal.
Start intake by asking my target schools: school name, sport, and men's/women's
team for each. Ask in small batches. Follow section 4's common-question order,
then ask ONLY the named sport's section 2 questions. Save my actual answers to
./profile.json using profile.template.json. Never guess or round any answer.
Keep saved files local and never contact coaches. Ask before creating a profile
or account, entering passwords, uploading files, or entering information that
itself authorizes contact. Show exact consent/attestation/signature wording and
enter only my answer. Default marketing/SMS opt-ins to No/unchecked unless I
explicitly say Yes. Have me approve the full profile and final school list with
each form URL before filling. Use Computer Use in the ChatGPT desktop app for
form entry. Ask again immediately before each school's Submit. Report each
school's result with its form link in chat and in local reports/.
```

You can also copy the stage prompts from [prompts/start.md](prompts/start.md),
[find-forms.md](prompts/find-forms.md), [fill-forms.md](prompts/fill-forms.md), and
[report.md](prompts/report.md). They all follow [AGENTS.md](AGENTS.md).

## Backup option (no Codex, no repo)

Copy all of [CHATGPT_PROMPT.md](CHATGPT_PROMPT.md) into the ChatGPT desktop app's
**Work** mode with **Computer Use**. This is one self-contained prompt: no repo,
local package or terminal is required. It contains the common intake, every sport
branch and the same form-verification and approval boundaries. It checks Computer
Use before intake, too; without working Computer Use it pauses form entry.

At the end of intake it prints a **SAVED PROFILE SUMMARY** for you to copy and
keep privately. Paste it into a later Work conversation with the backup prompt
to resume. The helper confirms saved answers and asks for missing items; it
rechecks live wording, links and approvals before acting. This path keeps its
working record in the conversation rather than maintaining profile.json or
local reports. It does not create files or additional remote copies. Information
shared in chat is still processed by ChatGPT; it is not offline storage.

## What the family does

The Codex path saves local records; the backup path prints records in chat for
you to copy into your private saved summary.

1. Name the schools, sports and men's/women's teams. Then answer the common
   questions and the selected sport's questions. Say "unknown" or "skip" when
   needed; the helper leaves those answers empty and asks again if a form
   requires them. It asks for NAIA IDs only for NAIA targets.
2. Review the complete saved profile. Check every number, unit, test score,
   graduation year and contact detail. Review the final school list with each
   verified questionnaire URL. Approve the profile and school list explicitly.
3. Stay available for form-specific questions. Read each exact consent,
   attestation, certification or signature request and provide your own answer.
   Unanswered required requests stop that school's form. Opt-ins stay off unless
   you say Yes; required Yes/No consent choices still need your answer.
4. Review each filled form and give a separate Yes immediately before Submit.
   Profile/list approval does not authorize all submissions at once. Changes to
   reviewed answers or URLs require renewed approval. Handle any CAPTCHA yourself.
5. Read the result table in chat and the local `reports/` folder: **submitted**
   means confirmed success; **failed** includes the reason; **needs-info** lists
   missing fields or approvals. An uncertain submission is not retried on its own.

Some actions happen before Submit: ARMS "Continue without" creates a school
profile and needs separate permission. Some forms say that entering a cell
number authorizes SMS/AI contact; the helper must show the wording and ask
before entering it. A separate No checkbox may not remove that authorization.

Plus has usage limits over a rolling window, often described as about 5 hours;
other limits may apply. Long sessions may pause until allowance resets. Check the
[OpenAI Help Center](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
and the app's Usage display for current limits and reset times; no fixed message
count is promised. After a pause, ask the helper
to resume from the local profile and reports, verify the current form, and get
a fresh confirmation before Submit.

## Privacy and sharing the package

`profile.json` stays local as the saved working file. Never commit or share it.
The same applies to `profile*.local.json`, reports, documents and screenshots.
Keep this folder outside cloud-synced or shared folders. The `.gitignore` helps
prevent accidental Git inclusion; it does not encrypt files or prevent sharing.

In the Codex path, saved profile and report files stay local. Information you provide in
chat or display while using Computer Use is not a promise of offline processing.
Entering data into a school's form discloses it to that school and its form
provider; the site may save entries before Submit. Review the approved site
before entering family data. Never put passwords in the profile or conversation.

To share this package, send only the instructions, blank template, prompts,
references and synthetic `test/` files. Inspect the folder first: exclude all
private profiles, reports, PDFs, screenshots and other family documents.
The template is blank; `test/dry-run-profile.json` contains only invented data
and must never be submitted.

## Package contents and dry run

- `AGENTS.md`: the workflow and approval rules.
- `START_PROMPT.md`: the single prompt for the recommended Codex path, including
  repo retrieval, setup, the first-run check and intake.
- `CHATGPT_PROMPT.md`: the self-contained Work mode backup with a copyable summary.
- `profile.template.json`: blank common fields and all sport blocks; the helper
  asks only the selected sport and leaves the others empty.
- `prompts/`: first-run check and copy-paste prompts for each stage.
- `reference/recruiting-intake-tree.md`: the original read-only field research.
- `reference/sample-forms.md`: section 5 copied exactly, retaining every source
  row and coverage note. Historical links may be expired or blocked.
- `test/`: an obviously fake baseball profile, offline checks and dry-run guide.

Follow [test/README.md](test/README.md) to rehearse. A dry run fills only as far as
the permitted pre-Submit stage and **never presses Submit**. Missing information
or a separate approval gate can stop it earlier.
