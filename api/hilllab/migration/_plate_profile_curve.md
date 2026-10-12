# _plate_profile_curve

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The standard-deviation endpoint branch indexes the last fitted 1D parameter vector as though it were a matrix; its failure is silently suppressed. The gradient endpoint is relative to a sliced array without adding its offset. A dominant-value adjustment writes an index into the fluorescence array. Endpoint interpretation needs review before relying on exact fit bounds.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _plate_profile_curve(values, plot=False)
:module: hilllab.migration._plate_profile_curve
:canonical: hilllab.migration._plate_profile_curve._plate_profile_curve
```

## Behavior and usage

Returns `(peak_index, end_index)` for a nominal 16-point curve using candidate peaks 0–4, bounded Gaussian fits over the first eight points, and empirical penalties. End is clamped using at least four points and an upper bound of 11. plot=True draws the chosen curve/markers without returning axes. Supply finite numeric values with a nonzero maximum; penalties are heuristics rather than a statistical confidence interval.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `values` | `required` | **list**. a list of intensity values containing a  Gaussain cuve |
| `plot` | `False` | **bool**. controls whether the data and weights are displayed once the function finishes execution. Defaults to False. |

## Returns and side effects

Returns `(peak_index, end_index)` for a nominal 16-point curve using candidate peaks 0–4, bounded Gaussian fits over the first eight points, and empirical penalties.

## Source

`hilllab/migration/_plate_profile_curve.py`, lines 7–216 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_profile_curve.py#L7-L216)
