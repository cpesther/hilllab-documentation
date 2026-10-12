# generate_safe_name

[Folder overview](index.md)

## Signature

```{py:function} generate_safe_name(name, folder)
:module: hilllab.utilities.generate_safe_name
:canonical: hilllab.utilities.generate_safe_name.generate_safe_name
```

## Behavior and usage

Returns `(new_file_name, new_file_path)` strings, trying the original name then numbered alternatives while preserving all filename suffixes. `folder` must exist because it is listed immediately. It only checks names already present; it does not reserve a filename atomically, so another process can still create it. More than 100 attempted iterations raises `ValueError`.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `name` | `required` | **string**. the desired name for the file (including any file extensions) |
| `folder` | `required` | **string**. the path to the folder where this file will eventually be saved. |

## Returns and side effects

Returns `(new_file_name, new_file_path)` strings, trying the original name then numbered alternatives while preserving all filename suffixes.

## Source

`hilllab/utilities/generate_safe_name.py`, lines 5–51 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/generate_safe_name.py#L5-L51)
