# param_data

[Folder overview](index.md)

## Signature

```{py:function} param_data(data, labels=None)
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.param_data
```

## Behavior and usage

Returns `(dataset, count)` with six float32 features in fixed order: displacement, straightness, circular_variance, bb_area, mean_speed, mean_acceleration. A labels Excel file adds string labels, excludes idk, and keeps the first UUID label. Without labels, every summary UUID is emitted in group ordering. No feature scaling is applied. Requires TensorFlow, which is not declared in pyproject dependencies.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **str**. path to h5 file primary analysis data |
| `labels` | `None` | **str**. opt, path to xlsx file bead classifications |

## Returns and side effects

Returns `(dataset, count)` with six float32 features in fixed order: displacement, straightness, circular_variance, bb_area, mean_speed, mean_acceleration.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)

## Source

`hilllab/beads/tf_data.py`, lines 26–94 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L26-L94)
