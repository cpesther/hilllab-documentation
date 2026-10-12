# batch_subtract_drift

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Calls `_format_vrpn(data, fps)` without its required camera/magnification arguments, so active processing fails. The MATLAB export branch is a pass statement. Default drift bounds are stored back into loop variables and would persist from the first file. The shared drift helper also has unresolved implementation defects.
:::

## Signature

```{py:function} batch_subtract_drift(files, fps, method='linear', drift_start_time=None, drift_end_time=None, skip_existing=True, pipeline='python')
:module: hilllab.ptmr.batch_subtract_drift
:canonical: hilllab.ptmr.batch_subtract_drift.batch_subtract_drift
```

## Behavior and usage

Loops over explicit file paths and is intended to write sibling `.drift.track.csv` files for the Python pipeline. Existing targets may be skipped. Only linear subtraction is selected; normal completion returns None.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `files` | `required` | Explicit iterable of tracking file paths, not a starting folder. |
| `fps` | `required` | Acquisition frame rate in frames per second, used to convert frame indices to seconds where implemented. |
| `method` | `'linear'` | Algorithm selector; see supported literal values in the usage notes. Unsupported values are rejected where the body implements selection. |
| `drift_start_time` | `None` | Absolute starting timestamp in seconds for fitting drift, or intended per-file minimum when None. |
| `drift_end_time` | `None` | Absolute ending timestamp in seconds for fitting drift, or intended per-file maximum when None. |
| `skip_existing` | `True` | When True, skip a file whose expected destination already exists; this checks existence, not whether its parameters match the current run. |
| `pipeline` | `'python'` | python for CSV tracking or matlab for VRPN MAT input; current implementation is incomplete. |

## Returns and side effects

Only linear subtraction is selected; normal completion returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.ptmr._format_vrpn._format_vrpn`](_format_vrpn.md)
- [`hilllab.ptmr.drift._subtract_linear_drift._subtract_linear_drift`](drift/_subtract_linear_drift.md)
- [`hilllab.utilities.load_vrpn.load_vrpn`](../utilities/load_vrpn.md)

## Source

`hilllab/ptmr/batch_subtract_drift.py`, lines 9–65 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/batch_subtract_drift.py#L9-L65)
