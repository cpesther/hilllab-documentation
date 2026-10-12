# plate_relative_kinetic_calculation

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Conversion always uses 297 K rather than the bundle's temperature. The extra factor 2 differs from the direct Dt/time conversion; equivalence between the two reported diffusion definitions is not established. Pairwise entries include both read orderings and are not independent replicates.
:::

## Signature

```{py:function} plate_relative_kinetic_calculation(path=None, bundle=None, data_type='SPE', read_gap=30, **kwargs)
:module: hilllab.migration.plate_relative_kinetic_calculation
:canonical: hilllab.migration.plate_relative_kinetic_calculation.plate_relative_kinetic_calculation
```

## Behavior and usage

First performs kinetic fitting, then derives pairwise D from `(Dt2-Dt1)/(2*(t2-t1))` for read separations strictly greater than read_gap. Converts positive values to viscosity, removes outliers, and returns `(eta_results, all_eta_values)` with a one-row mean table and one n_reads×n_reads matrix per column. Insufficient separated reads yield empty subsets/NaNs.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `None` | **str**. path to the file to be loaded |
| `bundle` | `None` | **migration.Bundle**. The data bundle to be used if not loading from a path. |
| `data_type` | `'SPE'` | **string**. Specifies the type model used to collect the  data. Options include 'SPE' (default), 'TEC', and 'PRE'. |
| `read_gap` | `30` | **int**. the minimum number of reads by which two set of data must be separated to be included in the relative calculations. |
| `kwargs` | `extra keyword arguments` | Additional keyword arguments; forwarding or ignored behavior is described in the usage notes. |

## Returns and side effects

Converts positive values to viscosity, removes outliers, and returns `(eta_results, all_eta_values)` with a one-row mean table and one n_reads×n_reads matrix per column. Insufficient separated reads yield empty subsets/NaNs.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration.plate_kinetic_calculation.plate_kinetic_calculation`](plate_kinetic_calculation.md)
- [`hilllab.migration.stokes_einstein.eta`](eta.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.remove_outliers.remove_outliers`](../utilities/remove_outliers.md)

## Source

`hilllab/migration/plate_relative_kinetic_calculation.py`, lines 10–98 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_relative_kinetic_calculation.py#L10-L98)
