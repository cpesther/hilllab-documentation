# _plate_format_extended

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _plate_format_extended(input_data, num_reads)
:module: hilllab.migration._plate_format_extended
:canonical: hilllab.migration._plate_format_extended._plate_format_extended
```

## Behavior and usage

Returns 32 columns per 16-row read by preserving the first 12 rows of 24 columns, padding them, and converting original rows M–P into eight 12-value pseudo-columns. Right halves are reversed. Original repeated A–P row labels are restored. Requires the expected 16×24 input layout and at least one read.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_data` | `required` | **pandas.DataFrame**. the dataframe containing the  raw data. |
| `num_reads` | `required` | Number of complete 16-row read blocks expected in the input table. |

## Returns and side effects

Returns 32 columns per 16-row read by preserving the first 12 rows of 24 columns, padding them, and converting original rows M–P into eight 12-value pseudo-columns.

## Source

`hilllab/migration/_plate_format_extended.py`, lines 5–69 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_format_extended.py#L5-L69)
