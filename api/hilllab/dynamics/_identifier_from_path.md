# _identifier_from_path

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _identifier_from_path(path, split1, split2, name_only=False, numeric_only=False)
:module: hilllab.dynamics._identifier_from_path
:canonical: hilllab.dynamics._identifier_from_path._identifier_from_path
```

## Behavior and usage

Returns the substring after the last occurrence of split1 and before the first following split2. `name_only=True` uses the basename; otherwise the full path must be a string supporting split(). `numeric_only=True` keeps digit characters and converts to int, removing leading zeros. No digit content raises ValueError; absent separators do not automatically raise.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the file path from which the identifier will be dervied. |
| `split1` | `required` | **string**. the string where the path should be split first |
| `split2` | `required` | **string**. the string where the last fragment of the previous path split should be split again. |
| `name_only` | `False` | **bool**. if true, the identifier extraction will be performed only on the file name, not the entire path |
| `numeric_only` | `False` | **bool**. if true, only numerical characters in the  identifier will be included |

## Returns and side effects

Returns the substring after the last occurrence of split1 and before the first following split2.

## Source

`hilllab/dynamics/_identifier_from_path.py`, lines 5–38 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/_identifier_from_path.py#L5-L38)
