# plot_xy

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
bead=0 is treated as false and plots all beads instead of bead 0. Invalid paths print an error but leave all_files undefined, and the requested bead variable is reused inside the plotting loop, which can affect later files.
:::

## Signature

```{py:function} plot_xy(path, save=False, label_beads=True, bead=None, ax=None)
:module: hilllab.beads.plot_xy
:canonical: hilllab.beads.plot_xy.plot_xy
```

## Behavior and usage

Returns the Matplotlib Axes after drawing trajectories. A directory input is nonrecursive and all files are drawn on the reused axes. Coordinates remain in pixels; save=True writes sibling PNGs. Only rows with finite x are retained.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. the path to the file or folder that should be plotted |
| `save` | `False` | **bool**. whether the plots should be saved as PNGs to the  path provided. |
| `label_beads` | `True` | **bool**. when true, prints the index of each bead on  the plot next to its trace. Defaults to True. |
| `bead` | `None` | **int**. the 0-based index of one bead that should be  plotted by itself. |
| `ax` | `None` | Existing Matplotlib Axes to draw into, or None to create one. All folder files reuse this axes. |

## Returns and side effects

Returns the Matplotlib Axes after drawing trajectories.

## Source

`hilllab/beads/plot_xy.py`, lines 9–78 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/plot_xy.py#L9-L78)
