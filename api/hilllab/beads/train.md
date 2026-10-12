# train

[Folder overview](index.md)

## Signature

```{py:function} train(model, train_ds, val_ds, epochs)
:module: hilllab.beads.tf_train
:canonical: hilllab.beads.tf_train.train
```

## Behavior and usage

Compiles the supplied model in place with Adam, sparse categorical cross-entropy, and sparse categorical accuracy, trains on the two datasets, and returns `(model, history)`. Labels must be integer class IDs, not one-hot vectors. Early stopping monitors training accuracy with patience 3, not validation accuracy, and does not restore best weights.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `model` | `required` | **tf.keras.Model**. the model to be trained |
| `train_ds` | `required` | **tf.data.Dataset**. training dataset |
| `val_ds` | `required` | **tf.data.Dataset**. validation dataset |
| `epochs` | `required` | **int**. max epochs to train for (earlystop callback is on, so model training stops automatically when improvement stalls) |

## Returns and side effects

Compiles the supplied model in place with Adam, sparse categorical cross-entropy, and sparse categorical accuracy, trains on the two datasets, and returns `(model, history)`.

## Source

`hilllab/beads/tf_train.py`, lines 76–110 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_train.py#L76-L110)
