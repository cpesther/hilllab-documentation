# position_data.generator

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} position_data.generator()
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.position_data.generator
```

Two branch-specific definitions share this name; both implementations are recorded below. The parent selects the labeled or unlabeled variant.

## Behavior and usage

Branch-specific local generator yielding centered XY trajectories, optionally paired with their classification strings. It takes no explicit arguments; groupby objects and selected UUIDs are closed over from `position_data`.

## Inputs

No explicit input arguments.

## Returns and side effects

Branch-specific local generator yielding centered XY trajectories, optionally paired with their classification strings.

## Source

`hilllab/beads/tf_data.py`, lines 127–145 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L127-L145)
