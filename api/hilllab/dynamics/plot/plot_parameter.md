# plot_parameter

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Several registered values are strings/metadata and are not meaningful numeric boxplot targets. Save mode inherits the neighbor-path extension-loss issue. This Seaborn call uses newer options not backed by a declared Seaborn dependency.
:::

## Signature

```{py:function} plot_parameter(h5_path, parameter, use_groups=True, save=False, ymax=None, ymin=None)
:module: hilllab.dynamics.plot.plot_parameter
:canonical: hilllab.dynamics.plot.plot_parameter.plot_parameter
```

## Behavior and usage

Checks the parameter against the PARAMETERS registry, loads group assignments, and displays a boxplot by group or identifier. Returns None; invalid names warn and return before plotting. Units and display labels are metadata from the registry, not recalculated.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the path to the h5 file to be plotted |
| `parameter` | `required` | Exact key in dynamics.plot.parameters.PARAMETERS; use a numeric analysis field for a boxplot. |
| `use_groups` | `True` | **bool**. if True, data will be categorized using the  groups defined in the provided JSON file, if False, data will instead be plotted by the identifier column. |
| `save` | `False` | **bool**. if true, figure will be saved to same folder as h5 file |
| `ymax` | `None` | **int**. the maximum value for the y-axis |
| `ymin` | `None` | **int**. the minimum value for the y-axis |

## Returns and side effects

Returns None; invalid names warn and return before plotting.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.dynamics._load_with_groups._load_with_groups`](../_load_with_groups.md)
- [`hilllab.utilities.custom_axes.custom_axes`](../../utilities/custom_axes.md)
- [`hilllab.utilities.generate_neighbor_path.generate_neighbor_path`](../../utilities/generate_neighbor_path.md)
- [`hilllab.utilities.verify_name.verify_name`](../../utilities/verify_name.md)

## Source

`hilllab/dynamics/plot/plot_parameter.py`, lines 11–72 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/plot/plot_parameter.py#L11-L72)
