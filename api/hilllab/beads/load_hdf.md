# load_hdf

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} load_hdf(path)
:module: hilllab.beads.load_hdf
:canonical: hilllab.beads.load_hdf.load_hdf
```

## Behavior and usage

Returns `(groupby_summary, groupby_positions, df_metadata, bounds)` from `/summary`, `/positions`, and `/metadata` HDF keys. Both grouped tables use `uuid`, and positions must include x/y. Bounds are the maximum observed x/y values, not image dimensions. These grouped objects can be reused to avoid repeatedly loading the same file. Requires pandas' HDF backend (PyTables).

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Bead HDF filename containing summary, positions, and metadata keys. |

## Returns and side effects

Returns `(groupby_summary, groupby_positions, df_metadata, bounds)` from `/summary`, `/positions`, and `/metadata` HDF keys.

## Source

`hilllab/beads/load_hdf.py`, lines 5–26 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/load_hdf.py#L5-L26)
