# plate_define_radii

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Declining the multi confirmation recursively calls the function without required arguments. Multi inputs remain strings, and blank/repeat on the first selected column can lack a prior value. Lists/scalars assign all their own columns rather than respecting the selected-column list, and positivity is not checked.
:::

## Signature

```{py:function} plate_define_radii(bundle, radius_nm, columns_include, columns_exclude, extended)
:module: hilllab.migration.plate_define_radii
:canonical: hilllab.migration.plate_define_radii.plate_define_radii
```

## Behavior and usage

Returns a `Column N`→radius mapping. radius_nm may be scalar, a list assigned consecutively from column 1, or multi for interactive entry. At least one of columns_include/columns_exclude must be supplied to determine selected columns. Multi supports blank=previous, sNN=repeat through column NN, and e=finish. extended is accepted but unused.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `required` | **migration.Bundle**. the bundle object to which these  radii values should be saved. |
| `radius_nm` | `required` | **string or float**. a value for the radius or the string 'multi' to define multiple different radii. |
| `columns_include` | `required` | One-based column numbers to include. Do not combine with columns_exclude. |
| `columns_exclude` | `required` | One-based column numbers to omit. Do not combine with columns_include. |
| `extended` | `required` | Accepted for interface compatibility but unused in this function. |

## Returns and side effects

Returns a `Column N`→radius mapping. radius_nm may be scalar, a list assigned consecutively from column 1, or multi for interactive entry.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)

## Source

`hilllab/migration/plate_define_radii.py`, lines 7–124 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_define_radii.py#L7-L124)
