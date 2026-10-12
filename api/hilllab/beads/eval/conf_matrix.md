# conf_matrix

[Folder overview](index.md)

## Signature

```{py:function} conf_matrix(models, vocab, test_ds)
:module: hilllab.beads.eval.confusion_matrix
:canonical: hilllab.beads.eval.confusion_matrix.conf_matrix
```

## Behavior and usage

Displays averaged count and row-normalized confusion matrices across models; returns `None`. `vocab` defines class-index ordering, test labels must be integer IDs, and predictions must remain aligned with the unbatched labels. Missing row counts become zeros in normalization. Keep evaluation iteration deterministic.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `models` | `required` | **list**. list of models |
| `vocab` | `required` | **list**. list of classifications (['stuck','transiting','oscillating','discard']) |
| `test_ds` | `required` | **tf.data.Dataset**. test dataset |

## Returns and side effects

Displays averaged count and row-normalized confusion matrices across models; returns `None`.

## Source

`hilllab/beads/eval/confusion_matrix.py`, lines 8–58 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/confusion_matrix.py#L8-L58)
