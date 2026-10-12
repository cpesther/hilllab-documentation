# verify_name

[Folder overview](index.md)

## Signature

```{py:function} verify_name(name, valid_names, cutoff=0.8, print_output=True)
:module: hilllab.utilities.verify_name
:canonical: hilllab.utilities.verify_name.verify_name
```

## Behavior and usage

Returns True for an exact valid name and False otherwise. Optional warnings include up to five fuzzy matches with the given `cutoff`. It never replaces the input with a suggested name; handle False explicitly in calling code.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `name` | `required` | **string**. the user-provided name to be verified |
| `valid_names` | `required` | **list**. a list of valid strings |
| `cutoff` | `0.8` | **float**. the matching cutoff used in fuzzy search |
| `print_output` | `True` | **bool**. if true, function will throw warnings suggesting other possible valid names in the case of a mismatch |

## Returns and side effects

Returns True for an exact valid name and False otherwise.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.warning.warn`](warn.md)

## Source

`hilllab/utilities/verify_name.py`, lines 5–48 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/verify_name.py#L5-L48)
