# performance_dist

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Uses the `tick_labels` Matplotlib boxplot keyword, whereas the package pins Matplotlib 3.8.4, which uses the older labels keyword. The supplied dependency configuration does not match this call.
:::

## Signature

```{py:function} performance_dist(metrics, keys, name=None, colors=None)
:module: hilllab.beads.eval.performance_dist
:canonical: hilllab.beads.eval.performance_dist.performance_dist
```

## Behavior and usage

Displays boxplots for a sequence of metric arrays with corresponding `keys`; returns `None`. An optional callable colormap fills each box.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `metrics` | `required` | **tuple**. performance metric array (loss, accuracy, pseudo r2), returned by batch_evaluate for model types |
| `keys` | `required` | **list**. the model types (['position','param','summary']) |
| `name` | `None` | Optional metric title and y-axis label. |
| `colors` | `None` | Callable Matplotlib colormap taking a class/series index and returning a color. |

## Returns and side effects

Displays boxplots for a sequence of metric arrays with corresponding `keys`; returns `None`.

## Source

`hilllab/beads/eval/performance_dist.py`, lines 6–39 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/performance_dist.py#L6-L39)
