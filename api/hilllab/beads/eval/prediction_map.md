# prediction_map

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The relative imports `.tf_data` and `.load_hdf` point to nonexistent modules under beads.eval; the actual files are in the parent beads package.
:::

## Signature

```{py:function} prediction_map(model, data, key, vocab, interval=None, colors=None)
:module: hilllab.beads.eval.prediction_map
:canonical: hilllab.beads.eval.prediction_map.prediction_map
```

## Behavior and usage

Predicts bead classes using param/position/summary features and displays pixel XY trajectories colored by `vocab`; returns `None`. `interval=(start, end)` is a half-open bead-index range. Predictions and selected grouped UUID ordering must match.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `model` | `required` | **tf.keras.Model**. a model |
| `data` | `required` | **str**. path to h5 file primary analysis data for some plate |
| `key` | `required` | **str**. model type ('position', 'param,' 'summary') |
| `vocab` | `required` | Ordered class-name list matching the model output indices. |
| `interval` | `None` | **tuple**. opt, to plot less beads at a time |
| `colors` | `None` | Callable Matplotlib colormap taking a class/series index and returning a color. |

## Returns and side effects

Predicts bead classes using param/position/summary features and displays pixel XY trajectories colored by `vocab`; returns `None`.

## Source

`hilllab/beads/eval/prediction_map.py`, lines 10–84 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/prediction_map.py#L10-L84)
