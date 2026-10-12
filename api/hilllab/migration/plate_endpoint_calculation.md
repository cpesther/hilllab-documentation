# plate_endpoint_calculation

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Default zero hours/minutes selects read -1, which is not a valid assay endpoint. Missing path/bundle is checked only after attempting load. Direct read numbers are floats and are used for label-based range lookup, so confirm compatible integer-like table indexing.
:::

## Signature

```{py:function} plate_endpoint_calculation(hours=0, minutes=0, path=None, bundle=None, data_type='SPE', nested=False, read=0, **kwargs)
:module: hilllab.migration.plate_endpoint_calculation
:canonical: hilllab.migration.plate_endpoint_calculation.plate_endpoint_calculation
```

## Behavior and usage

Returns a DataFrame of eta, Dt, D, NRMSE, and peak amplitude for one read across cleaned columns. Direct calls select read `(hours*60+minutes)/interval_minutes - 1`, so the first read is at one interval, not time zero. Nested mode uses zero-based read explicitly and avoids console output/clipboard copying. Either provide a prepared bundle or loadable path/settings.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `hours` | `0` | **float**. number of hours in the desired timepoint |
| `minutes` | `0` | **int**. number of minutes in the desired timepoint |
| `path` | `None` | **str**. path to the file to be loaded |
| `bundle` | `None` | **migration.Bundle**. The data bundle to be used if not loading from a path. |
| `data_type` | `'SPE'` | **string**. Specifies the type model used to collect the  data. Options include 'SPE' (default), 'TEC', and 'PRE'. |
| `nested` | `False` | **bool**. indicates whether this function is being run from  within the plate_kinetic_calculation() function. This affects some minor data handling decisions. |
| `read` | `0` | **int**. used only when nested in the plate_kinetic_calculation() function to manually provide read numbers instead of calculating them based on given time values. |
| `kwargs` | `extra keyword arguments` | Additional keyword arguments; forwarding or ignored behavior is described in the usage notes. |

## Returns and side effects

Returns a DataFrame of eta, Dt, D, NRMSE, and peak amplitude for one read across cleaned columns.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration._plate_load_wrapper._plate_load_wrapper`](_plate_load_wrapper.md)
- [`hilllab.migration.plate_optimize_gaussian.plate_optimize_gaussian`](plate_optimize_gaussian.md)

## Source

`hilllab/migration/plate_endpoint_calculation.py`, lines 7–91 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_endpoint_calculation.py#L7-L91)
