# _plate_calculate_gaussian

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _plate_calculate_gaussian(params, curve, end_index, return_fit=False, delta_x_m=0.0045)
:module: hilllab.migration._plate_calculate_gaussian
:canonical: hilllab.migration._plate_calculate_gaussian._plate_calculate_gaussian
```

## Behavior and usage

Accepts `(A, Dt)` and a curve, evaluates `A*exp(-(x-delta_x_m)^2/(2*Dt))`, and returns normalized RMSE, or `(nrmse, fit_curve)` when return_fit=True. x spacing is in meters, Dt in m², and fitting errors use indices 1 through end_index-1. Error normalization is mean absolute observed curve over that range. Need positive Dt and a nonempty fitting interval.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `params` | `required` | **tuple**. (A, Dt) values to optimize. |
| `curve` | `required` | **array-like**. raw data values to compare. |
| `end_index` | `required` | **int**. index up to which to calculate the error. |
| `return_fit` | `False` | **bool**. if True, also return the fitted curve. |
| `delta_x_m` | `0.0045` | **float**. spacing along the x-axis (meters per point). |

## Returns and side effects

Accepts `(A, Dt)` and a curve, evaluates `A*exp(-(x-delta_x_m)^2/(2*Dt))`, and returns normalized RMSE, or `(nrmse, fit_curve)` when return_fit=True. x spacing is in meters, Dt in m², and fitting errors use indices 1 through end_index-1.

## Source

`hilllab/migration/_plate_calculate_gaussian.py`, lines 5–50 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_calculate_gaussian.py#L5-L50)
