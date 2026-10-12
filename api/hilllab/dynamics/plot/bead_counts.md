# bead_counts

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The noncumulative plot is a boxplot despite the average wording. Videos with zero tracked beads do not appear in summary-derived counts. save=True inherits generate_neighbor_path's check_safety extension-loss bug.
:::

## Signature

```{py:function} bead_counts(h5_path, cumulative=False, use_groups=True, save=False, ymin=None, ymax=None)
:module: hilllab.dynamics.plot.plot_bead_counts
:canonical: hilllab.dynamics.plot.plot_bead_counts.bead_counts
```

## Behavior and usage

Counts unique particle_id values per category/source path, then displays cumulative totals or per-video boxplots. Returns None. `use_groups` selects group versus identifier; both require identifier data, with optional automatically loaded groups JSON. `ymin/ymax` control display limits.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the path to the h5 file to be plotted |
| `cumulative` | `False` | **bool**. if true, the cumulative total of beads in each category will be plotted as opposed to the average per video. |
| `use_groups` | `True` | **bool**. if True, data will be categorized using the  groups defined in the provided JSON file, if False, data will instead be plotted by the identifier column. |
| `save` | `False` | **bool**. if true, figure will be saved to same folder as h5 file |
| `ymin` | `None` | **int**. the minimum value for the y-axis |
| `ymax` | `None` | **int**. the maximum value for the y-axis |

## Returns and side effects

Returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.dynamics._load_with_groups._load_with_groups`](../_load_with_groups.md)
- [`hilllab.utilities.custom_axes.custom_axes`](../../utilities/custom_axes.md)
- [`hilllab.utilities.generate_neighbor_path.generate_neighbor_path`](../../utilities/generate_neighbor_path.md)

## Source

`hilllab/dynamics/plot/plot_bead_counts.py`, lines 11–108 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/plot/plot_bead_counts.py#L11-L108)
