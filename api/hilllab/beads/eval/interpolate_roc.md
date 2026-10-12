# interpolate_roc

[Folder overview](index.md)

## Signature

```{py:function} interpolate_roc(models, vocab, test_ds, name=None, colors=None)
:module: hilllab.beads.eval.interpolate_roc
:canonical: hilllab.beads.eval.interpolate_roc.interpolate_roc
```

## Behavior and usage

Displays one-vs-rest ROC curves interpolated onto 100 false-positive-rate values and returns `None`. The displayed mean AUC is the area under the mean curve; its ± value is standard deviation of individual model AUCs. `colors` is an optional callable colormap. Each class needs positive and negative examples, and model/dataset ordering must be stable.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `models` | `required` | **list**. list of models |
| `vocab` | `required` | **list**. list of classifications (['stuck','transiting','oscillating','discard']) |
| `test_ds` | `required` | **tf.data.Dataset**. test dataset |
| `name` | `None` | **str**. opt, label for model name |
| `colors` | `None` | **cmap**. opt, colormap for aesthetics |

## Returns and side effects

Displays one-vs-rest ROC curves interpolated onto 100 false-positive-rate values and returns `None`.

## Source

`hilllab/beads/eval/interpolate_roc.py`, lines 9–77 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/interpolate_roc.py#L9-L77)
