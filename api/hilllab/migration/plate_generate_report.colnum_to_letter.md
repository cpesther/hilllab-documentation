# plate_generate_report.colnum_to_letter

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} plate_generate_report.colnum_to_letter(n)
:module: hilllab.migration.plate_generate_report
:canonical: hilllab.migration.plate_generate_report.plate_generate_report.colnum_to_letter
```

## Behavior and usage

Closure-local helper returning Excel letters for a one-based integer column index: 1→A, 26→Z, 27→AA. Zero/negative values return an empty string instead of raising. Used to build report cell references.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `n` | `required` | One-based Excel column number. |

## Returns and side effects

Zero/negative values return an empty string instead of raising.

## Source

`hilllab/migration/plate_generate_report.py`, lines 184–190 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_generate_report.py#L184-L190)
