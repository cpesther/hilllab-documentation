# _plate_profile_curve.gaussian

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} _plate_profile_curve.gaussian(x, a, mu, sigma)
:module: hilllab.migration._plate_profile_curve
:canonical: hilllab.migration._plate_profile_curve._plate_profile_curve.gaussian
```

## Behavior and usage

Closure-local model returning `a*exp(-(x-mu)^2/(2*sigma^2))` for array x and scalar amplitude/center/width. Width is in sample-index units here, not meters. Called by SciPy curve_fit and not exported as a standalone function.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `x` | `required` | Numeric sample-index array. |
| `a` | `required` | Gaussian amplitude. |
| `mu` | `required` | Center in sample-index coordinates. |
| `sigma` | `required` | Gaussian width in sample-index units. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/migration/_plate_profile_curve.py`, lines 28–29 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_profile_curve.py#L28-L29)
