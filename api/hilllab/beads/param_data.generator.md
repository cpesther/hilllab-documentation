# param_data.generator

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} param_data.generator()
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.param_data.generator
```

Two branch-specific definitions share this name; both implementations are recorded below. The parent selects the labeled or unlabeled variant.

## Behavior and usage

Branch-specific closure-local generator. With labels it yields `(six_float32_features, classification_string)`; without labels it yields only the six-feature vector. It reads UUIDs and grouped data captured by `param_data` and is not independently importable.

## Inputs

No explicit input arguments.

## Returns and side effects

With labels it yields `(six_float32_features, classification_string)`; without labels it yields only the six-feature vector.

## Source

`hilllab/beads/tf_data.py`, lines 58–69 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L58-L69)
