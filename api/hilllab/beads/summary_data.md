# summary_data

[Folder overview](index.md)

## Signature

```{py:function} summary_data(data, labels=None)
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.summary_data
```

## Behavior and usage

Returns `(dataset, count)` of 27 float32 summary values selected by positional slice `iloc[:, 28:55]`, optionally paired with string classifications. Column order is therefore part of the input contract; renaming alone does not make another HDF schema compatible. No scaling is applied.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **str**. path to h5 file primary analysis data |
| `labels` | `None` | **str**. opt, path to xlsx file bead classifications |

## Returns and side effects

Returns `(dataset, count)` of 27 float32 summary values selected by positional slice `iloc[:, 28:55]`, optionally paired with string classifications.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)

## Source

`hilllab/beads/tf_data.py`, lines 181–248 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L181-L248)
