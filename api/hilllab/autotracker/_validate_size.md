# _validate_size

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _validate_size(bead_size_pixels)
:module: hilllab.autotracker._validate_size
:canonical: hilllab.autotracker._validate_size._validate_size
```

## Behavior and usage

Returns the provided `bead_size_pixels`, increased by one when it is even, and emits a warning on adjustment. Supply a positive integer diameter for TrackPy; this helper does not reject negatives or nonintegral values.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bead_size_pixels` | `required` | Requested TrackPy feature diameter in pixels. Even values are increased by one; positivity/integer validation is not performed. |

## Returns and side effects

Returns the provided `bead_size_pixels`, increased by one when it is even, and emits a warning on adjustment.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/autotracker/_validate_size.py`, lines 4–19 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/autotracker/_validate_size.py#L4-L19)
