# position_data

[Folder overview](index.md)

## Signature

```{py:function} position_data(data, labels=None)
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.position_data
```

## Behavior and usage

Returns `(dataset, count)` of variable-length `(frames, 2)` float32 trajectories, centered by summary mean_x/mean_y. With a labels file, each trajectory is paired with a string class and idk beads are removed. Centering does not normalize scale or time. Use padded batching when combining lengths; TensorFlow is an additional dependency.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **str**. path to h5 file primary analysis data |
| `labels` | `None` | **str**. opt, path to xlsx file bead classifications |

## Returns and side effects

Returns `(dataset, count)` of variable-length `(frames, 2)` float32 trajectories, centered by summary mean_x/mean_y.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)

## Source

`hilllab/beads/tf_data.py`, lines 97–178 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L97-L178)
