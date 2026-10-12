# classify_review

[Folder overview](index.md)

## Signature

```{py:function} classify_review(path, file, label='idk', start=0)
:module: hilllab.beads.classify_review
:canonical: hilllab.beads.classify_review.classify_review
```

## Behavior and usage

Reads an existing labels workbook, selects rows whose classification equals `label`, and revisits their beads from `start`. Valid responses update all matching UUID rows and rewrite the workbook after each bead; an unrecognized response leaves labels unchanged. Returns `None`. `start` is an index in the filtered list, not the complete HDF bead list.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. path to a .h5 file with bead trajectory data and uuid |
| `file` | `required` | **str**. path to a .xlsx file with classifications and uuid |
| `label` | `'idk'` | **str**. bead class to review (default to 'idk') |
| `start` | `0` | **int**. index of bead to start from (default to 0) |

## Returns and side effects

Returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)
- [`hilllab.beads.plot_bead.plot_bead`](plot_bead.md)

## Source

`hilllab/beads/classify_review.py`, lines 10–80 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/classify_review.py#L10-L80)
