# Prompt: technical documentation

```text
READER
{developer | administrator | end user} who wants to {task}. They know {stack/basics}; they do not know {our system}.

VERIFIED MATERIAL (copied from the real system; do not alter commands, paths, flags, field names or output)
- Commands: {paste, as run}
- Configuration keys: {paste from the source}
- API request/response: {paste a real example}
- Versions tested: {versions}
- Known limitations: {list}

TASK
Write a {how-to | reference | troubleshooting} page that gets the reader from {start state} to {end state}.

RULES
- Start with prerequisites and versions, then the shortest working path.
- Use commands and names exactly as given. Never invent a flag, endpoint, setting or default.
- One complete example rather than several partial ones.
- Same term for the same thing throughout.
- State limitations and what is not supported.
- Mark anything you could not confirm from the material as [UNVERIFIED: …].

OUTPUT
The page in Markdown, then a list of every command and setting used, each pointing to the VERIFIED MATERIAL line it came from.
```
