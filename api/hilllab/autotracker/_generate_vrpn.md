# _generate_vrpn

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Only frames present in `data` are visited; absent frames are not generated. The legacy `np.NAN` spelling depends on NumPy <2, as specified by the package.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _generate_vrpn(data, path, file_name, nframes, nparticles)
:module: hilllab.autotracker._generate_vrpn
:canonical: hilllab.autotracker._generate_vrpn._generate_vrpn
```

## Behavior and usage

Writes a MATLAB file at `path`; returns `None`. `data` must contain `frame`, `particle`, `x`, and `y`, with unique frame/particle pairs. The ten-column tracking array uses frame number as time, reindexes particle IDs by enumeration, and fills missing particle positions with NaN. `nframes * nparticles` preallocates the array; supply counts consistent with the data or rows can overflow or remain zero-filled. Position values are pixels. `os.getlogin()` requires a login-capable environment.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **pandas.DataFrame**. the dataframe containing the particle trajectories. |
| `path` | `required` | **string**. the path where the VRPN should be saved. |
| `file_name` | `required` | **string**. the name of the file being processed |
| `nframes` | `required` | **int**. the number of frames in the video that produced this VRPN. |
| `nparticles` | `required` | **int**. the number of particles to be saved in this VRPN. |

## Returns and side effects

Writes a MATLAB file at `path`; returns `None`.

## Source

`hilllab/autotracker/_generate_vrpn.py`, lines 11–117 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/autotracker/_generate_vrpn.py#L11-L117)
