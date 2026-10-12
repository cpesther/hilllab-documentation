# eta

[Folder overview](index.md)

## Signature

```{py:function} eta(temperature_K, D_m2s, radius_nm)
:module: hilllab.migration.stokes_einstein
:canonical: hilllab.migration.stokes_einstein.eta
```

## Behavior and usage

Returns viscosity in mPa·s from Kelvin temperature, diffusion in m²/s, and radius in nm. Zero diffusion returns infinity. It performs explicit nm→m and Pa·s→mPa·s conversions; use measured positive values and distinguish probe radius from diameter.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `temperature_K` | `required` | **int**. temperature of the experiment in Kelvin |
| `D_m2s` | `required` | **float**. diffusion coefficient in units of m^2/s |
| `radius_nm` | `required` | **float**. radius of the probe in nanometers |

## Returns and side effects

Returns viscosity in mPa·s from Kelvin temperature, diffusion in m²/s, and radius in nm. Zero diffusion returns infinity.

## Source

`hilllab/migration/stokes_einstein.py`, lines 31–55 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/stokes_einstein.py#L31-L55)
