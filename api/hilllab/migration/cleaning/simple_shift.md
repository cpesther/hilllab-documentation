# simple_shift

[Folder overview](index.md)

## Signature

```{py:function} simple_shift(data)
:module: hilllab.migration.cleaning.noise
:canonical: hilllab.migration.cleaning.noise.simple_shift
```

## Behavior and usage

Returns data minus the absolute value of the minimum over indices 7–10. Requires an array-like object supporting numeric subtraction and at least eight entries. The background interval is fixed rather than derived from the curve; a negative background is made more negative by the absolute-value subtraction.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **list**. the list of unshifted data points |

## Returns and side effects

Returns data minus the absolute value of the minimum over indices 7–10.

## Source

`hilllab/migration/cleaning/noise.py`, lines 3–22 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/cleaning/noise.py#L3-L22)
