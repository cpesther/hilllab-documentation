# process_2C_swelling

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Plot x coordinates use sample indices despite a physical-time label; plotted values are ratios rather than percent change despite the y-axis label. Zero first integrals are unguarded. The default empty groups list is not a useful experimental grouping, and no red-channel plots are produced.
:::

## Signature

```{py:function} process_2C_swelling(path, groups=[], time_units='hours', read_sample_interval=12, interval_minutes=15)
:module: hilllab.swelling.process_2C_swelling
:canonical: hilllab.swelling.process_2C_swelling.process_2C_swelling
```

## Behavior and usage

Loads two channels, integrates them, divides each well by its first retained integral, groups selected column numbers, and samples every read_sample_interval rows. groups should be a mapping of group names to one-based column-number lists. Writes a two-sheet RESULT Excel workbook plus two green-channel PNG plots; returns None. Workbook timestamps use interval_minutes, with conversion to hours only for the exact string hours.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the path to the file to be processed |
| `groups` | `[]` | **dict**. a dictionary of group names keyed by the name of the group with values of lists of the constituent column numbers used for average and standard deviation calculations. |
| `time_units` | `'hours'` | **string**. 'hours' or 'minutes' controlling the units in which the swelling data is displayed |
| `read_sample_interval` | `12` | **int**. the interval to be used for sampling the data for export (i.e. save the values every n reads) |
| `interval_minutes` | `15` | **int**. the number of minutes between subsequent reads in the dataset. |

## Returns and side effects

Writes a two-sheet RESULT Excel workbook plus two green-channel PNG plots; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.swelling._load_file._load_file`](_load_file.md)
- [`hilllab.swelling.calculate_NIF.calculate_NIF`](calculate_NIF.md)
- [`hilllab.utilities.custom_axes.custom_axes`](../utilities/custom_axes.md)

## Source

`hilllab/swelling/process_2C_swelling.py`, lines 12–162 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/swelling/process_2C_swelling.py#L12-L162)
