# summary_data.generator

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} summary_data.generator()
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.summary_data.generator
```

Two branch-specific definitions share this name; both implementations are recorded below. The parent selects the labeled or unlabeled variant.

## Behavior and usage

Branch-specific local generator yielding the first summary row's columns 28–54, optionally with a classification string. The generated vector must have length 27 to satisfy TensorFlow's output signature.

## Inputs

No explicit input arguments.

## Returns and side effects

Branch-specific local generator yielding the first summary row's columns 28–54, optionally with a classification string.

## Source

`hilllab/beads/tf_data.py`, lines 212–223 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L212-L223)
