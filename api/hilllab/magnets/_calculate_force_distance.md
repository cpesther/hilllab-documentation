# _calculate_force_distance

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Frame differences are used directly as time and XY remains in input units. The parent passes pixel coordinates and a meter-scale diameter without converting displacement or frame time, so coefficients are not established as physically calibrated SI forces/distances. Zero force/distance is not guarded before logarithms.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _calculate_force_distance(data, viscosity, origin, diameter)
:module: hilllab.magnets._calculate_force_distance
:canonical: hilllab.magnets._calculate_force_distance._calculate_force_distance
```

## Behavior and usage

Returns a list of `(voltage, m, c)` fits using natural logs: `log(force)=m*log(distance)+c`. It computes displacement between first/last frame rows per voltage, divides by their frame-number difference, and applies Stokes drag `3π*viscosity*diameter*velocity`. Only particles present at both endpoints are used, and fewer than two estimates skips that voltage.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | DataFrame with columns ['t', 'x', 'y', 'PID', 'voltages'] |
| `viscosity` | `required` | fluid viscosity (Pa*s) |
| `origin` | `required` | tuple (x0, y0) for magnetic field origin |
| `diameter` | `required` | particle diameter (meters) |

## Returns and side effects

Returns a list of `(voltage, m, c)` fits using natural logs: `log(force)=m*log(distance)+c`.

## Source

`hilllab/magnets/_calculate_force_distance.py`, lines 4–92 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/_calculate_force_distance.py#L4-L92)
