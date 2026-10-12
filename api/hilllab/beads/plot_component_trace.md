# plot_component_trace

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The docstring describes folder traversal and XY maximization, but neither occurs in this implementation. Empty tracking arrays also reach max() when checking a missing bead.
:::

## Signature

```{py:function} plot_component_trace(path, save=False, bead=0)
:module: hilllab.beads.plot_component_trace
:canonical: hilllab.beads.plot_component_trace.plot_component_trace
```

## Behavior and usage

Plots x/y components of one bead against a sequential sample index and returns `None`. Reads a single VRPN MAT file, with bead IDs in column 2 and positions in columns 4/5. `save=True` writes a sibling PNG. The plotted frame axis does not use the actual VRPN frame-number column.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. the path to the file or folder that should be plotted |
| `save` | `False` | **bool**. whether the plots should be saved as PNGs to the  path provided. |
| `bead` | `0` | **int**. the 0-based index of one bead that should be  plotted. |

## Returns and side effects

Plots x/y components of one bead against a sequential sample index and returns `None`.

## Source

`hilllab/beads/plot_component_trace.py`, lines 9–62 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/plot_component_trace.py#L9-L62)
