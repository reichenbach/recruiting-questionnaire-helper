Read AGENTS.md and follow its section 0 before intake. Use the package obtained
through START_PROMPT.md or an existing local/bundled copy; help the parent unzip
and select the folder if needed. Every runtime repo/file fetch must follow
START_PROMPT.md's single-attempt fallback: use a bounded timeout and handle
errors; if private, 404, offline or blocked, say "I couldn't open the online
package, so I'll use a local copy or ask you to share it." Try once only, with
no retry loops or alternate download methods/endpoints after failure. Continue
from the open folder, bundled copy or a ZIP/folder the parent points to, without
more network attempts after a failure. If none exists, ask the family to paste
or share the package and explain what is missing; never crash or stall on a
fetch. Explain each step in plain words. Do setup yourself where
the available tools and permissions allow; never ask the parent to use a
terminal. Use only free necessary installs from official sources. Let the parent
handle system permissions and sign-in; never create accounts without asking or
pay for anything. Never type, request or save passwords; the family signs in
themselves.

## Set up your app's computer-use tool

Identify the current app and its available computer-use tool. Follow that app's
official setup/help for enabling the tool, required components and browser
access. Explain that the tool can see and operate approved apps. Check actual
capabilities; an app or subscription name is not proof of access. If the app has
no supported computer-use tool, explain the limitation and pause intake.

### If you use Codex / the ChatGPT desktop app:

Guide the parent through Plugins > Computer Use > Install plugin or Enable.
Turn on both the Computer Use server and skill
toggles, then Try now. Review browser access in Settings > Computer use and
explain the app-access prompt before the parent approves it.

## Permissions and browser check for any supported app

If the first-run check fails on an older Intel Mac, it may not be supported. On
Mac, check Apple menu > About This Mac if needed. Guide the parent through
System Settings > Privacy & Security > Screen Recording and Accessibility for
the computer-use component shown in the permission prompt. Explain that these
let it see the browser and click/type. Have the parent grant the permissions and
reopen the app if prompted. Do not bypass a system permission or administrator
prompt.

Windows: explain that the computer-use tool takes over the foreground, pointer
and keyboard. Keep the browser visible, the PC unlocked and connected to the
internet; do not use the PC meanwhile. The parent can stop or take over at any
time.

Now use the computer-use tool to open https://example.com in a browser. Inspect
the page and read back the heading actually observed. Pass only when it reads
"Example Domain". Do not claim success from the expected text, web search, HTTP
fetch or shell command. Do not collect family information or begin intake until
it works.

If it fails, say what happened without jargon. Check the tool's installation,
enablement, required components, browser access, Mac chip/permissions or Windows
visible desktop, and internet access. If you use the app-specific setup above,
also check both toggles. Retry the same page after fixing the issue. If a new
session is necessary, walk the parent through reopening this
project and repeating the check. If the feature is unavailable for this account,
region or device policy, explain the limitation and pause; do not promise an
upgrade fixes it or switch to scripted form entry. Once the test passes, follow
prompts/start.md.
