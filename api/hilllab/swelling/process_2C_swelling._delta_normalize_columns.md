# process_2C_swelling._delta_normalize_columns

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} process_2C_swelling._delta_normalize_columns(data)
:module: hilllab.swelling.process_2C_swelling
:canonical: hilllab.swelling.process_2C_swelling.process_2C_swelling._delta_normalize_columns
```

## Behavior and usage

Closure-local function returning a new DataFrame with each column divided by its first integral value. It preserves column names, performs ratio normalization rather than subtraction/percent change, and has no zero-baseline guard.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | Per-read integral DataFrame, one column per well; each column is divided by row 0. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/swelling/process_2C_swelling.py`, lines 41–48 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/swelling/process_2C_swelling.py#L41-L48)
