# classify_bead

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} classify_bead(path, file, start=0)
:module: hilllab.beads.classify_bead
:canonical: hilllab.beads.classify_bead.classify_bead
```

## Behavior and usage

Interactively plots each bead starting at the zero-based `start` index and accumulates classification rows. `s/t/o/d/i` mean stuck/transiting/oscillating/discard/idk; other responses also become idk. A second prompt advances or saves/exits. Appends to Excel and returns `None`; keep the printed index to resume. A plotting error ends the loop and saves labels already collected.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. path to a .h5 file with bead data new (str): path to a .xlsx file to record classifications |
| `file` | `required` | Destination Excel labels workbook; prior rows are retained and newly collected rows appended. |
| `start` | `0` | **int**. index of bead to start from (default to 0) |

## Returns and side effects

Appends to Excel and returns `None`; keep the printed index to resume.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)
- [`hilllab.beads.plot_bead.plot_bead`](plot_bead.md)

## Source

`hilllab/beads/classify_bead.py`, lines 10–100 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/classify_bead.py#L10-L100)
