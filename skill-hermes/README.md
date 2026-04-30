# Hermes Agent skill bundle

This directory is the Hermes Agent publish target for talk-normal. It contains a copy of `prompt.md` and `install.sh` from the repo root, plus the `SKILL.md` manifest.

**Do not edit `prompt.md` or `install.sh` in this directory directly.** The source of truth for both is the repo root. This directory holds synced copies.

## Publishing

Before publishing, re-sync the copies so they match the repo root:

```bash
bash ../scripts/sync-skill.sh
```

Then users can install directly from the GitHub repo:

```bash
hermes skills install --force hexiecs/talk-normal/skill-hermes
```

## Updating the version

When shipping a new release of the ruleset:

1. Edit `prompt.md` at the repo root and commit as usual.
2. Re-run `bash scripts/sync-skill.sh` so this bundle picks up the new `prompt.md`.
3. The version in `skill-hermes/SKILL.md` is bumped automatically by the sync script.
