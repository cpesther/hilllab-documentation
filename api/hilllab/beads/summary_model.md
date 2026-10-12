# summary_model

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} summary_model()
:module: hilllab.beads.tf_train
:canonical: hilllab.beads.tf_train.summary_model
```

## Behavior and usage

Returns an uncompiled classifier for 27 summary features with four 128-unit ReLU dense layers, dropout 0.5, and four-way softmax. Match the positional feature ordering from `summary_data`.

## Inputs

No explicit input arguments.

## Returns and side effects

Returns an uncompiled classifier for 27 summary features with four 128-unit ReLU dense layers, dropout 0.5, and four-way softmax.

## Source

`hilllab/beads/tf_train.py`, lines 58–71 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_train.py#L58-L71)
