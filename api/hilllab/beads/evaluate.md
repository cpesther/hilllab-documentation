# evaluate

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The null predictor is built only from classes observed in test labels, without preserving absent class IDs. Missing/noncontiguous classes can produce an invalid baseline or error; empty test data and zero null loss are not guarded. History legends call validation data test data.
:::

## Signature

```{py:function} evaluate(model, test_ds, history=None)
:module: hilllab.beads.tf_train
:canonical: hilllab.beads.tf_train.evaluate
```

## Behavior and usage

Returns `(loss, accuracy, pseudo_r2)` and optionally plots training/validation history. Pseudo-R² is `1 - model_loss / constant_class_frequency_loss`, not linear-regression R². The model must be compiled with accuracy as its second reported metric.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `model` | `required` | **tf.keras.Model**. the model to be evaluated |
| `test_ds` | `required` | **tf.data.Dataset**. test dataset |
| `history` | `None` | **tf.keras.callbacks.History**. opt, history object |

## Returns and side effects

Returns `(loss, accuracy, pseudo_r2)` and optionally plots training/validation history.

## Source

`hilllab/beads/tf_train.py`, lines 115–178 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_train.py#L115-L178)
