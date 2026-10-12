# bead_traj

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Imports `.load_hdf` from `beads.eval`, where no such module exists; the actual helper is in the parent beads folder.
:::

## Signature

```{py:function} bead_traj(bead_uuid, path, ax=None, color=None)
:module: hilllab.beads.eval.bead_traj
:canonical: hilllab.beads.eval.bead_traj.bead_traj
```

## Behavior and usage

Plots one bead's XY trajectory and returns a Matplotlib Axes. UUIDs or integer group indices are accepted, coordinates are pixels, and an existing axes may be reused. It also reconstructs time only to verify lengths, although time is not plotted.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bead_uuid` | `required` | **str or int**. uuid or index of the bead to be plotted |
| `path` | `required` | **str**. path to h5 file for plate with bead |
| `ax` | `None` | **matplotlib.axes.Axes**. opt, specify to plot in subplots |
| `color` | `None` | **cmap**. opt, aesthetics good beads: plate 3, bead 499: stuck plate 3, bead 365: transiting plate 3, bead 339: oscillating plate 1, bead 313: discard |

## Returns and side effects

Plots one bead's XY trajectory and returns a Matplotlib Axes.

## Source

`hilllab/beads/eval/bead_traj.py`, lines 8–66 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/bead_traj.py#L8-L66)
