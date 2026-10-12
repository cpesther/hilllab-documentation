# custom_axes

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} custom_axes(figsize=(8, 6), xlabel='', ylabel='', title='', subtitle='', log=False, grid=False, grid_ticks='both')
:module: hilllab.utilities.custom_axes
:canonical: hilllab.utilities.custom_axes.custom_axes
```

## Behavior and usage

Returns `(fig, ax)` after applying HillLab plotting styles. `figsize` is in inches; labels and title/subtitle are strings. `log` accepts False, True, `x`, `y`, `xy`, or `yx`; log axes require positive data. `grid` accepts False, True, `x`, or `y`, and `grid_ticks` is passed as Matplotlib's `which`. This changes global `rcParams` to use Arial, so later plots inherit that font choice.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `figsize` | `(8, 6)` | (width, height) in inches passed to Matplotlib subplots. |
| `xlabel` | `''` | X-axis label string. |
| `ylabel` | `''` | Y-axis label string. |
| `title` | `''` | Text shown as a heading or title. |
| `subtitle` | `''` | Axes title below the figure-wide title. |
| `log` | `False` | False for linear axes; True/xy/yx for both log axes, or x/y for one. |
| `grid` | `False` | False, True, x, or y selecting disabled/both/single-axis grid. |
| `grid_ticks` | `'both'` | Matplotlib grid which setting, typically both, major, or minor. |

## Returns and side effects

Returns `(fig, ax)` after applying HillLab plotting styles.

## Source

`hilllab/utilities/custom_axes.py`, lines 4–55 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/custom_axes.py#L4-L55)
