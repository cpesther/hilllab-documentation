# test_create_identifiers

[Folder overview](index.md)

## Signature

```{py:function} test_create_identifiers(h5_path, split1, split2, name_only=True, numeric_only=False)
:module: hilllab.dynamics.test_create_identifiers
:canonical: hilllab.dynamics.test_create_identifiers.test_create_identifiers
```

## Behavior and usage

Samples seven summary paths, previews identifiers, and asks whether to extract/print all unique identifiers. Returns None and does not modify the HDF file. The input must contain at least seven summary rows because pandas sample(7) does not use replacement. This is an interactive diagnostic rather than a unit test.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the file path to the h5 file to test identifier extraction |
| `split1` | `required` | **string**. the string where the path should be split first |
| `split2` | `required` | **string**. the string where the last fragment of the previous path split should be split again. |
| `name_only` | `True` | **bool**. if true, the identifier extraction will be performed only on the file name, not the entire path |
| `numeric_only` | `False` | **bool**. if true, only numerical characters in the  identifier will be included |

## Returns and side effects

Returns None and does not modify the HDF file.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.dynamics._identifier_from_path._identifier_from_path`](_identifier_from_path.md)

## Source

`hilllab/dynamics/test_create_identifiers.py`, lines 8–63 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/test_create_identifiers.py#L8-L63)
