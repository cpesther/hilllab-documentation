# batch_rename_files

[Folder overview](index.md)

## Signature

```{py:function} batch_rename_files(folder_path, old, new)
:module: hilllab.utilities.batch_rename_files
:canonical: hilllab.utilities.batch_rename_files.batch_rename_files
```

## Behavior and usage

Previews every immediate directory entry with `old` replaced by `new`, then renames entries only after a `Y` response. Returns `None`. It includes directories, not just files, and does not recurse. Inspect the preview before confirming; collisions and partial renames are not recovered.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder_path` | `required` | **string**. the path to the folder with the files to be renamed. |
| `old` | `required` | **string**. the old string in the file name to be replaced |
| `new` | `required` | **string**. the new string used to replace the old string |

## Returns and side effects

Returns `None`.

## Source

`hilllab/utilities/batch_rename_files.py`, lines 4–32 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/batch_rename_files.py#L4-L32)
