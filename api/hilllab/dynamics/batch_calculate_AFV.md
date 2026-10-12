# batch_calculate_AFV

[Folder overview](index.md)

## Signature

```{py:function} batch_calculate_AFV(path)
:module: hilllab.dynamics.batch_calculate_AFV
:canonical: hilllab.dynamics.batch_calculate_AFV.batch_calculate_AFV
```

## Behavior and usage

For every summary UUID, loads instantaneous rows, looks up its source fps, computes AFV metrics, and writes `<stem>.afv.h5` with key afv. Returns the output Path. Requires queryable uuid data columns and matching metadata path rows. Empty input lists fail concatenation; existing output is replaced.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. the path to the H5 file with primary analysis data |

## Returns and side effects

Returns the output Path.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.dynamics.calculate_AFV.calculate_AFV`](calculate_AFV.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)

## Source

`hilllab/dynamics/batch_calculate_AFV.py`, lines 11–62 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/batch_calculate_AFV.py#L11-L62)
