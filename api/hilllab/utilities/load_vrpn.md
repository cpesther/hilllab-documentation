# load_vrpn

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} load_vrpn(path)
:module: hilllab.utilities.load_vrpn
:canonical: hilllab.utilities.load_vrpn.load_vrpn
```

## Behavior and usage

Returns a DataFrame extracted from `tracking.spot3DSecUsecIndexFramenumXYZRPY`. `.vrpn.mat` produces ten named columns, and `.vrpn.evt.evt.mat` produces nine. Empty data still returns those columns. Other full suffixes raise `ValueError`. This uses SciPy loadmat and does not handle MATLAB v7.3 HDF5 files.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | MATLAB file with standard .vrpn.mat or .vrpn.evt.evt.mat full suffix and a tracking structure. |

## Returns and side effects

Returns a DataFrame extracted from `tracking.spot3DSecUsecIndexFramenumXYZRPY`. Empty data still returns those columns.

## Source

`hilllab/utilities/load_vrpn.py`, lines 8–43 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/load_vrpn.py#L8-L43)
