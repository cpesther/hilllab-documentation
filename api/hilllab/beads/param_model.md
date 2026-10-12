# param_model

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} param_model()
:module: hilllab.beads.tf_train
:canonical: hilllab.beads.tf_train.param_model
```

## Behavior and usage

Returns an uncompiled Keras Sequential classifier for six features: two 32-unit ReLU dense layers, dropout 0.5, and four-way softmax. Inputs should match `param_data`; outputs are four class probabilities in the downstream vocabulary order.

## Inputs

No explicit input arguments.

## Returns and side effects

Returns an uncompiled Keras Sequential classifier for six features: two 32-unit ReLU dense layers, dropout 0.5, and four-way softmax.

## Source

`hilllab/beads/tf_train.py`, lines 30–41 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_train.py#L30-L41)
