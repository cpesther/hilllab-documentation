# D

[Folder overview](index.md)

## Signature

```{py:function} D(temperature_K, eta_mPas, radius_nm)
:module: hilllab.migration.stokes_einstein
:canonical: hilllab.migration.stokes_einstein.D
```

## Behavior and usage

Returns diffusion coefficient in m²/s from temperature_K, viscosity eta_mPas in mPa·s, and radius_nm in nm using the Stokes–Einstein formula. Zero viscosity returns infinity. Radius and temperature are not validated; zero radius can still divide by zero and negative values produce algebraic but nonphysical results.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `temperature_K` | `required` | **int**. temperature of the experiment in Kelvin |
| `eta_mPas` | `required` | **float**. solvent viscosity in units of mPa * s |
| `radius_nm` | `required` | **float**. radius of the probe in nanometers |

## Returns and side effects

Returns diffusion coefficient in m²/s from temperature_K, viscosity eta_mPas in mPa·s, and radius_nm in nm using the Stokes–Einstein formula. Zero viscosity returns infinity.

## Source

`hilllab/migration/stokes_einstein.py`, lines 4–28 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/stokes_einstein.py#L4-L28)
