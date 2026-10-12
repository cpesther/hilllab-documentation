# load_matlab

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} load_matlab(file_path)
:module: hilllab.utilities.load_matlab
:canonical: hilllab.utilities.load_matlab.load_matlab
```

## Behavior and usage

Returns a dictionary loaded first through h5py and then, only on `OSError`, through SciPy `loadmat`. The HDF5 branch slices top-level objects with `[:]`; it does not recursively decode MATLAB structures, cells, or groups. The returned representations therefore differ between MATLAB file formats.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `file_path` | `required` | Local MATLAB filename; the helper tries HDF5 then SciPy loadmat. |

## Returns and side effects

Returns a dictionary loaded first through h5py and then, only on `OSError`, through SciPy `loadmat`.

## Source

`hilllab/utilities/load_matlab.py`, lines 6–17 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/load_matlab.py#L6-L17)
