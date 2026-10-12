# r

[Folder overview](index.md)

## Signature

```{py:function} r(temperature_K, D_m2s, eta_mPas)
:module: hilllab.migration.stokes_einstein
:canonical: hilllab.migration.stokes_einstein.r
```

## Behavior and usage

Returns radius in nm from Kelvin temperature, diffusion in m²/s, and viscosity in mPa·s. Zero diffusion or viscosity returns infinity. Inputs are not fitted or checked for physical consistency.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `temperature_K` | `required` | **int**. temperature of the experiment in Kelvin |
| `D_m2s` | `required` | **float**. diffusion coefficient in units of m^2/s |
| `eta_mPas` | `required` | **float**. solvent viscosity in units of mPa * s |

## Returns and side effects

Returns radius in nm from Kelvin temperature, diffusion in m²/s, and viscosity in mPa·s. Zero diffusion or viscosity returns infinity.

## Source

`hilllab/migration/stokes_einstein.py`, lines 58–82 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/stokes_einstein.py#L58-L82)
