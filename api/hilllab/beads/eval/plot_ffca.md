# plot_ffca

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Genotype assignment is a hard-coded list for 17 particular plates rather than derived from `labels`. It is unsuitable for general experiments without confirming that exact ordering.
:::

## Signature

```{py:function} plot_ffca(avg_ffca, std_ffca, labels, colors=None)
:module: hilllab.beads.eval.ffca
:canonical: hilllab.beads.eval.ffca.plot_ffca
```

## Behavior and usage

Displays an FFCA bar chart and returns `None`. `avg_ffca`, standard deviations, and labels must align. `colors` is a callable colormap, not a list of colors.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `avg_ffca` | `required` | Sequence of mean FFCA fractions, one per plotted label. |
| `std_ffca` | `required` | Sequence of FFCA standard deviations used as bar error sizes. |
| `labels` | `required` | Plate/category labels in the same order as the values; the genotype palette is separately hard-coded. |
| `colors` | `None` | **cmap**. opt, aesthetics |

## Returns and side effects

Displays an FFCA bar chart and returns `None`.

## Source

`hilllab/beads/eval/ffca.py`, lines 98–147 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/ffca.py#L98-L147)
