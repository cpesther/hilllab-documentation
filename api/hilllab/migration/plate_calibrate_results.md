# plate_calibrate_results

[Folder overview](index.md)

## Signature

```{py:function} plate_calibrate_results(bundle)
:module: hilllab.migration.plate_calibrate_results
:canonical: hilllab.migration.plate_calibrate_results.plate_calibrate_results
```

## Behavior and usage

Mutates and returns a Bundle. Uses calibration columns' mean diffusion over the last eight hours and known viscosities to infer effective radii, removes radius outliers, then recalculates eta/D tables by nominal-radius groups. Requires calibration_columns mapping one-based column numbers to mPa·s values, populated D/eta tables, and experiment duration longer than the selected eight-hour range. Unmatched radii generate warnings. Empty calibration sets fail concatenation.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `required` | **migration.Bundle**. the bundle containing the results  that should be calibrated. |

## Returns and side effects

Mutates and returns a Bundle.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration.plate_extract_result.plate_extract_result`](plate_extract_result.md)
- [`hilllab.migration.stokes_einstein.D`](D.md)
- [`hilllab.migration.stokes_einstein.eta`](eta.md)
- [`hilllab.migration.stokes_einstein.r`](r.md)
- [`hilllab.utilities.remove_outliers.remove_outliers`](../utilities/remove_outliers.md)
- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/migration/plate_calibrate_results.py`, lines 11–129 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_calibrate_results.py#L11-L129)
