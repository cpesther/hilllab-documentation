# classify_batch

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} classify_batch(path, file, bead_class)
:module: hilllab.beads.classify_batch
:canonical: hilllab.beads.classify_batch.classify_batch
```

## Behavior and usage

Labels every UUID loaded from a bead HDF file as `s`→stuck, `t`→transiting, or `o`→oscillating. Appends rows with index, UUID, label, local timestamp, and username to the destination Excel workbook; returns `None`. Existing UUIDs are not replaced or deduplicated, so repeated calls can create multiple classifications for a bead.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. path to a .h5 file with bead data new (str): path to a .xlsx file to record classifications classification (str): classification, must be one of: 's': stuck 't': transiting 'o': oscillating |
| `file` | `required` | Destination Excel workbook filename. Existing rows are loaded and new labels appended. |
| `bead_class` | `required` | One of s, t, o for stuck, transiting, oscillating. Other values raise an exception. |

## Returns and side effects

Appends rows with index, UUID, label, local timestamp, and username to the destination Excel workbook; returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.beads.load_hdf.load_hdf`](load_hdf.md)

## Source

`hilllab/beads/classify_batch.py`, lines 10–77 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/classify_batch.py#L10-L77)
