# position_model

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} position_model()
:module: hilllab.beads.tf_train
:canonical: hilllab.beads.tf_train.position_model
```

## Behavior and usage

Returns an uncompiled variable-length XY classifier with zero masking, a 64-unit LSTM, two 32-unit ReLU dense layers, dropout 0.5, and four-way softmax. Zero-valued whole timesteps are masked, so genuinely centered `(0, 0)` positions can also be ignored.

## Inputs

No explicit input arguments.

## Returns and side effects

Returns an uncompiled variable-length XY classifier with zero masking, a 64-unit LSTM, two 32-unit ReLU dense layers, dropout 0.5, and four-way softmax.

## Source

`hilllab/beads/tf_train.py`, lines 43–56 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_train.py#L43-L56)
