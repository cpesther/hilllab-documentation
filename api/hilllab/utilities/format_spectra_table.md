# format_spectra_table

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} format_spectra_table(t)
:module: hilllab.utilities.format_spectra_table
:canonical: hilllab.utilities.format_spectra_table.format_spectra_table
```

## Behavior and usage

Fills missing values with zero in the original DataFrame, removes every 17th row, requires exactly 24 remaining columns, and returns a table indexed with repeated A–P row labels and columns `Column 1`–`Column 24`. Use only plate-reader blocks containing 16 well rows plus a separator; arbitrary table lengths are not supported.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `t` | `required` | 24-column plate-reader DataFrame with 16 data rows plus separator per read. Missing values are filled in place. |

## Returns and side effects

Fills missing values with zero in the original DataFrame, removes every 17th row, requires exactly 24 remaining columns, and returns a table indexed with repeated A–P row labels and columns `Column 1`–`Column 24`.

## Source

`hilllab/utilities/format_spectra_table.py`, lines 4–27 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/format_spectra_table.py#L4-L27)
