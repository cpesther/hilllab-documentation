# plate_generate_report.write_metric_formulas

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} plate_generate_report.write_metric_formulas(ws, start_col_num, num_cols, data_start_row, mean_row, median_row, stdev_row)
:module: hilllab.migration.plate_generate_report
:canonical: hilllab.migration.plate_generate_report.plate_generate_report.write_metric_formulas
```

## Behavior and usage

Closure-local helper modifying an openpyxl worksheet in place and returning None. Writes mean/median/sample-standard-deviation formulas across a fixed row-count range, plus labels/fonts/alignment. num_rows and right_align are captured from the parent. Formula caches remain unset until a spreadsheet engine recalculates the workbook.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `ws` | `required` | Openpyxl Worksheet modified in place. |
| `start_col_num` | `required` | One-based first data column; metric labels are put in the preceding column. |
| `num_cols` | `required` | Number of metric columns. |
| `data_start_row` | `required` | One-based first observation row. |
| `mean_row` | `required` | One-based row receiving AVERAGE formulas and the Mean label. |
| `median_row` | `required` | One-based row receiving MEDIAN formulas. |
| `stdev_row` | `required` | One-based row receiving STDEV formulas. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/migration/plate_generate_report.py`, lines 256–284 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_generate_report.py#L256-L284)
