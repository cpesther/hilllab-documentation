# _plate_prepare_data

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Consensus incorrectly indexes the np.unique function instead of the returned unique-value arrays and fails. temperature_K and method arguments are not stored in bundle metadata here, and export=False still calls plate_export_bundle unconditionally. NumPy-array include/exclude arguments can trigger ambiguous Boolean evaluation.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _plate_prepare_data(bundle, columns_include=None, columns_exclude=None, radius_nm=0, interval_minutes=15, delay_minutes=0, load_rate_minutes=1.5, temperature_K=297, method='individual', export=False, **kwargs)
:module: hilllab.migration._plate_prepare_data
:canonical: hilllab.migration._plate_prepare_data._plate_prepare_data
```

## Behavior and usage

Mutates and returns a bundle after selecting one-based columns, assigning radii/timing, normalizing each curve, localizing peaks/ranges, shifting peaks and background, and saving a preprocessing workbook. Localization methods are individual, average, or consensus. Individual localization failures fall back to peak=1/end=8 with a warning. More than one read is needed for progress totals; zero/empty inputs are not handled.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `required` | **migration.Bundle**. the data bundle |
| `columns_include` | `None` | **list**. indicates which columns should be  included in processing. |
| `columns_exclude` | `None` | **list**. list of columns that should be exluded from processing. |
| `radius_nm` | `0` | **float or list**. radius of the probe in nanometers or list of radius for each selected column. |
| `interval_minutes` | `15` | **int**. number of minutes between each read |
| `delay_minutes` | `0` | **float**. number of minutes after loading was  completed that measurement began. |
| `load_rate_minutes` | `1.5` | **float**. the average number of minutes taken  to load each capillary. Defaults to 1.5. |
| `temperature_K` | `297` | **float**. temperature of the system in Kelvin. |
| `method` | `'individual'` | **string**. the way in which the adjustment(s) for the data should be determined based on the results from the profiling method. Options include 'average', 'consensus', 'individual', and 'manual'. |
| `export` | `False` | **bool**. controls whether the data is exported to an Excel file after pre-processing. |
| `kwargs` | `extra keyword arguments` | Accepted but unused by this preparation body. |

## Returns and side effects

Mutates and returns a bundle after selecting one-based columns, assigning radii/timing, normalizing each curve, localizing peaks/ranges, shifting peaks and background, and saving a preprocessing workbook.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration._plate_profile_curve._plate_profile_curve`](_plate_profile_curve.md)
- [`hilllab.migration.plate_define_radii.plate_define_radii`](plate_define_radii.md)
- [`hilllab.migration.plate_export_bundle.plate_export_bundle`](plate_export_bundle.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/migration/_plate_prepare_data.py`, lines 11–315 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_prepare_data.py#L11-L315)
