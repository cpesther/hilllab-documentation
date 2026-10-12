# plot_bead

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Providing both `path` and `groupby` skips both initialization branches; providing neither fails before the intended validation. The function assumes uniformly sampled, complete trajectories.
:::

## Signature

```{py:function} plot_bead(bead_uuid, groupby=None, path=None, pixel_width=1)
:module: hilllab.beads.plot_bead
:canonical: hilllab.beads.plot_bead.plot_bead
```

## Behavior and usage

Displays a four-view trajectory figure and returns `None`. Provide exactly one of `path` or the tuple returned by `load_hdf`; `bead_uuid` may be a UUID or zero-based index in the grouped summary ordering. `pixel_width` scales pixels into micrometers when not 1. Time is reconstructed from lifetime_seconds/lifetime_frames and must match trajectory length.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bead_uuid` | `required` | the unique identifier assigned to a bead (str) or the index of the bead in the file (int) |
| `groupby` | `None` | **tuple**. tuple containing load_hdf return |
| `path` | `None` | **str**. path to a .h5 file with bead data to run load_hdf |
| `pixel_width` | `1` | **int**. opt micron/pixel conversion (default to 1) |

## Returns and side effects

Displays a four-view trajectory figure and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)

## Source

`hilllab/beads/plot_bead.py`, lines 9–95 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/plot_bead.py#L9-L95)
