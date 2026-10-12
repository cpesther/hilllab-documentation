# plate_generate_report.excel_row_cells

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} plate_generate_report.excel_row_cells(start_col_num, num_cols, row_num)
:module: hilllab.migration.plate_generate_report
:canonical: hilllab.migration.plate_generate_report.plate_generate_report.excel_row_cells
```

## Behavior and usage

Closure-local helper returning a list of cell-address strings for num_cols consecutive columns at row_num, starting with one-based start_col_num. Uses the parent's column-letter converter and does not validate Excel limits.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `start_col_num` | `required` | One-based first Excel column. |
| `num_cols` | `required` | Number of consecutive columns. |
| `row_num` | `required` | One-based Excel row number. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/migration/plate_generate_report.py`, lines 252–254 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_generate_report.py#L252-L254)
