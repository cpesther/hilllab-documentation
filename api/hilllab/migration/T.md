# T

[Folder overview](index.md)

## Signature

```{py:function} T(D_m2s, eta_mPas, radius_nm)
:module: hilllab.migration.stokes_einstein
:canonical: hilllab.migration.stokes_einstein.T
```

## Behavior and usage

Returns temperature in Kelvin from diffusion in m²/s, viscosity in mPa·s, and radius in nm. This is a direct algebraic inversion; no Celsius conversion or validity check is applied.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `D_m2s` | `required` | **float**. diffusion coefficient in units of m^2/s |
| `eta_mPas` | `required` | **float**. solvent viscosity in units of mPa * s |
| `radius_nm` | `required` | **float**. radius of the probe in nanometers |

## Returns and side effects

Returns temperature in Kelvin from diffusion in m²/s, viscosity in mPa·s, and radius in nm.

## Source

`hilllab/migration/stokes_einstein.py`, lines 85–103 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/stokes_einstein.py#L85-L103)
