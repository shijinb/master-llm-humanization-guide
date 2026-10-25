# Case 04: Technical doc with a guessed command flag

## Brief
How-to for exporting a backup. Verified material: `app-cli backup create --output ./backup.tar.gz` (tested on v2.3); no `--compress` flag exists; backups over 2 GB need `--split 500M`.

## Draft under review
> To create a backup, simply run `app-cli backup create --compress --output ./backup.tar.gz`. This will seamlessly back up all your data.

## Expected findings
| Criterion | Score | Why |
|---|---|---|
| Accuracy | 0 | `--compress` does not exist; the command will fail |
| Information gain | 0 | Omits the 2 GB limit and `--split`, the one thing the reader needs to know |
| Cliché-free | 1 | "seamlessly", "simply" |
| Honesty | 1 | "All your data" overstates; the limitation is missing |

**Verdict:** fails the accuracy gate. Commands must be copied from the verified material, never written from memory.
