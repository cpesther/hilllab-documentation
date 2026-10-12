# create_identifiers

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The docstring refers to identifier_split and identifier_name arguments that are not in the signature. Actual extraction uses split1/split2 and writes the fixed identifier column.
:::

## Signature

```{py:function} create_identifiers(h5_path, split1, split2, name_only=False, numeric_only=False)
:module: hilllab.dynamics.create_identifiers
:canonical: hilllab.dynamics.create_identifiers.create_identifiers
```

## Behavior and usage

Returns None after writing a copied sibling `<stem>.identify.h5` with an updated summary table. It prints extracted identifiers and asks for confirmation; the source HDF stays unchanged. Even when confirmation is declined, a copy is still made, but its summary has no newly added identifier column. Test extraction with test_create_identifiers first.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the file path to the h5 file to test identifier extraction |
| `split1` | `required` | **string**. the string where the path should be split first |
| `split2` | `required` | **string**. the string where the last fragment of the previous path split should be split again. |
| `name_only` | `False` | **bool**. if true, the identifier extraction will be performed only on the file name, not the entire path |
| `numeric_only` | `False` | **bool**. if true, only numerical characters in the  identifier will be included |

## Returns and side effects

Returns None after writing a copied sibling `<stem>.identify.h5` with an updated summary table.

## Source

`hilllab/dynamics/create_identifiers.py`, lines 11–67 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/create_identifiers.py#L11-L67)
