# _generate_new_vrpn

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
This is a local untracked source file. Its lowercase filename does not match the `_generate_new_VRPN` import in `autotrack_videos`; the new writer is not wired into that caller. Missing whole frames are not populated.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _generate_new_vrpn(data, path, file_name, nframes, nparticles)
:module: hilllab.autotracker._generate_new_vrpn
:canonical: hilllab.autotracker._generate_new_vrpn._generate_new_vrpn
```

## Behavior and usage

The supplied implementation is functionally the same VRPN export loop as `_generate_vrpn`, with an explicit bare return. It writes `tracking.info` and `tracking.spot3DSecUsecIndexFramenumXYZRPY` to `path`, returns `None`, and expects TrackPy columns plus counts matching the data. Particle IDs are reindexed, coordinates are pixels, and timestamps are zero.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **pandas.DataFrame**. the dataframe containing the particle trajectories. |
| `path` | `required` | **string**. the path where the VRPN should be saved. |
| `file_name` | `required` | **string**. the name of the file being processed |
| `nframes` | `required` | **int**. the number of frames in the video that produced this VRPN. |
| `nparticles` | `required` | **int**. the number of particles to be saved in this VRPN. |

## Returns and side effects

The supplied implementation is functionally the same VRPN export loop as `_generate_vrpn`, with an explicit bare return. It writes `tracking.info` and `tracking.spot3DSecUsecIndexFramenumXYZRPY` to `path`, returns `None`, and expects TrackPy columns plus counts matching the data.

## Source

`hilllab/autotracker/_generate_new_vrpn.py`, lines 9–116 · Local working-tree version; differs from the recorded repository revision.
