# _remove_wide_angles

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _remove_wide_angles(df, origin, pole_tip, angle_threshold)
:module: hilllab.magnets._remove_wide_angles
:canonical: hilllab.magnets._remove_wide_angles._remove_wide_angles
```

## Behavior and usage

Returns a filtered DataFrame copy of rows within `angle_threshold` degrees of the origin-to-pole-tip direction. This filters points, not necessarily whole particle trajectories. Coincident origin/pole-tip raises ValueError; points exactly at origin yield undefined angles and are excluded. Use coordinate units consistently.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `df` | `required` | **DataFrame**. DataFrame containing 'x', 'y', and 'frame' columns. |
| `origin` | `required` | Two-coordinate reference point in the same units as dataframe x/y. |
| `pole_tip` | `required` | Two-coordinate tip point defining the accepted axis direction from origin. |
| `angle_threshold` | `required` | **float**. Angle threshold in degrees. Points with angles |

## Returns and side effects

Returns a filtered DataFrame copy of rows within `angle_threshold` degrees of the origin-to-pole-tip direction. Coincident origin/pole-tip raises ValueError; points exactly at origin yield undefined angles and are excluded.

## Source

`hilllab/magnets/_remove_wide_angles.py`, lines 4–42 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/_remove_wide_angles.py#L4-L42)
