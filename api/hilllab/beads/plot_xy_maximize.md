# plot_xy_maximize

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Invalid paths print an error but leave all_files undefined. Empty trajectories or empty files fail during labels and maximum calculations.
:::

## Signature

```{py:function} plot_xy_maximize(path, save=False, label_beads=True)
:module: hilllab.beads.plot_xy_maximize
:canonical: hilllab.beads.plot_xy_maximize.plot_xy_maximize
```

## Behavior and usage

Displays origin-shifted bead trajectories separated into rows of six, using per-trajectory range times 1.3 for spacing; returns None. Processes a single file or immediate VRPN MAT files and optionally saves sibling PNGs. Coordinates are relative pixels rather than their original field positions.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. the path to the file or folder that should be plotted |
| `save` | `False` | **bool**. whether the plots should be saved as PNGs to the  path provided. |
| `label_beads` | `True` | **bool**. when true, prints the index of each bead on  the plot next to its trace. Defaults to True. |

## Returns and side effects

Displays origin-shifted bead trajectories separated into rows of six, using per-trajectory range times 1.3 for spacing; returns None.

## Source

`hilllab/beads/plot_xy_maximize.py`, lines 9–87 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/plot_xy_maximize.py#L9-L87)
