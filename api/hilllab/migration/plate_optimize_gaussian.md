# plate_optimize_gaussian

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Optimizer success is not checked before reporting values. Zero elapsed time forces D and viscosity to zero, which should not be treated as measured transport. Positive probe radius and valid nonnegative timing are not enforced. In bundle mode loading offset uses position among cleaned columns, which can differ from the original instrument column after exclusions.
:::

## Signature

```{py:function} plate_optimize_gaussian(bundle=None, column=None, read=None, curve=None, end_index=6, interval_minutes=15, load_rate_minutes=1.5, delay_minutes=0, radius_nm=1, temperature_K=297, plot_fit=False)
:module: hilllab.migration.plate_optimize_gaussian
:canonical: hilllab.migration.plate_optimize_gaussian.plate_optimize_gaussian
```

## Behavior and usage

Returns a dictionary with eta (mPa·s), Dt (m²), D (m²/s), NRMSE, and Peak (fitted amplitude). L-BFGS-B fits amplitude within ±5% of curve sample 1 and Dt from 1e-9 to 0.1 m². Bundle mode uses per-column fit range, radius, timing, and temperature; manual curve mode still requires a numeric read. Time includes read interval plus column-loading offset plus delay. Optional plotting draws data and fitted curve.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `None` | **migration.Bunlde**. the data bundle |
| `column` | `None` | **string**. the name of the column to process |
| `read` | `None` | **int**. the number of the read to process |
| `curve` | `None` | Optional numeric spatial profile for manual fitting; otherwise uses bundle/read/column. |
| `end_index` | `6` | Exclusive fit-range end, beginning at sample index 1. Bundle mode uses ranges_final. |
| `interval_minutes` | `15` | Minutes between sequential reads. Bundle mode uses its stored value. |
| `load_rate_minutes` | `1.5` | Minutes of loading offset per preceding processed column; bundle mode uses its stored value. |
| `delay_minutes` | `0` | Additional elapsed time in minutes before the nominal read-time origin. |
| `radius_nm` | `1` | Probe radius in nanometers, not diameter. Bundle mode reads the column-specific radius. |
| `temperature_K` | `297` | Temperature in Kelvin. In bundle mode the stored bundle value takes precedence. |
| `plot_fit` | `False` | When True, add the observed and fitted curve to a Matplotlib plot. |

## Returns and side effects

Returns a dictionary with eta (mPa·s), Dt (m²), D (m²/s), NRMSE, and Peak (fitted amplitude).

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration._plate_calculate_gaussian._plate_calculate_gaussian`](_plate_calculate_gaussian.md)

## Source

`hilllab/migration/plate_optimize_gaussian.py`, lines 10–128 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_optimize_gaussian.py#L10-L128)
