# batch_evaluate

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Its relative import `.tf_train` resolves under `beads.eval`, but `tf_train.py` is in the parent `beads` folder. The current module cannot import that dependency as written.
:::

## Signature

```{py:function} batch_evaluate(models, test_ds)
:module: hilllab.beads.eval.batch_evaluate
:canonical: hilllab.beads.eval.batch_evaluate.batch_evaluate
```

## Behavior and usage

Calls the bead evaluate routine for each model, prints mean/std metrics, and returns three lists `(loss, accuracy, pseudo_r2)` rather than averaged scalars. Supply a nonempty model list and a labeled test dataset.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `models` | `required` | **tuple**. list of models |
| `test_ds` | `required` | **tf.data.Dataset**. test dataset |

## Returns and side effects

Calls the bead evaluate routine for each model, prints mean/std metrics, and returns three lists `(loss, accuracy, pseudo_r2)` rather than averaged scalars.

## Source

`hilllab/beads/eval/batch_evaluate.py`, lines 7–51 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/batch_evaluate.py#L7-L51)
