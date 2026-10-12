# plate_kinetic_calculation

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} plate_kinetic_calculation(path=None, bundle=None, data_type='SPE', **kwargs)
:module: hilllab.migration.plate_kinetic_calculation
:canonical: hilllab.migration.plate_kinetic_calculation.plate_kinetic_calculation
```

## Behavior and usage

Resets and fills plate_eta/Dt/D/nrmse/peak result tables for every zero-based read, then returns the mutated Bundle. Provide a prepared bundle or path with preprocessing keywords. It does not itself export calculated result tables or a report. A one-read experiment reaches a zero progress total.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `None` | **str**. path to the file to be loaded |
| `bundle` | `None` | **migration.Bundle**. The data bundle to be used if not loading from a path. |
| `data_type` | `'SPE'` | **string**. Specifies the type model used to collect the  data. Options include 'SPE' (default), 'TEC', and 'PRE'. |
| `kwargs` | `extra keyword arguments` | Additional keyword arguments; forwarding or ignored behavior is described in the usage notes. |

## Returns and side effects

Resets and fills plate_eta/Dt/D/nrmse/peak result tables for every zero-based read, then returns the mutated Bundle.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration._plate_load_wrapper._plate_load_wrapper`](_plate_load_wrapper.md)
- [`hilllab.migration.plate_endpoint_calculation.plate_endpoint_calculation`](plate_endpoint_calculation.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)

## Source

`hilllab/migration/plate_kinetic_calculation.py`, lines 10–63 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_kinetic_calculation.py#L10-L63)
