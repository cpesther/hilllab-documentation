# data_preprocess.encode

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} data_preprocess.encode(features, label_str)
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.data_preprocess.encode
```

## Behavior and usage

Closure-local TensorFlow mapping callback returning `(features, integer_label)` from a feature object and classification string via the parent StringLookup layer. No out-of-vocabulary bucket is configured; unexpected labels are not silently accepted.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `features` | `required` | Feature tensor passed through unchanged. |
| `label_str` | `required` | String classification mapped through the parent vocabulary to an integer class ID. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/beads/tf_data.py`, lines 284–285 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L284-L285)
