# autotrack_videos_parameter_test

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
If TrackPy linking fails, a warning is printed but `particle_positions` remains undefined and is subsequently used. The first-frame title adds one to the displayed bead count.
:::

## Signature

```{py:function} autotrack_videos_parameter_test(video_path, n_frames=1, bead_size_pixels=21, max_travel_pixels=5, memory=0, invert=False, **kwargs)
:module: hilllab.autotracker.autotrack_videos_parameter_test
:canonical: hilllab.autotracker.autotrack_videos_parameter_test.autotrack_videos_parameter_test
```

## Behavior and usage

Selects the given video or the first AVI/MP4 discovered in a folder, reads up to `n_frames`, and displays detected spots and linked trajectories. Returns `None`; its outputs are a Matplotlib figure and a printed tracking summary. `n_frames` actually defaults to 1, although the docstring says 5. Extra keywords are accepted and ignored. Use more than one frame to inspect linking.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. path to the video to use for testing |
| `n_frames` | `1` | **int, optional**. number of frames to use during the test track. Defaults to 5. |
| `bead_size_pixels` | `21` | **int, optional**. Estimated diameter of the  particles in pixels. Default is 21. |
| `max_travel_pixels` | `5` | **int, optional**. Maximum number of pixels a particle  can travel between frames for TrackPy to consider it to be the same particle. Default is 5. |
| `memory` | `0` | **int, optional**. Memory parameter for TrackPy's linking,  specifying how long particles are remembered between frames. Default is 0. |
| `invert` | `False` | **bool, optional**. when false, bright spots on a dark background will be tracked. When true, dark spots on a bright background will be tracked. |
| `kwargs` | `extra keyword arguments` | Accepted for compatibility with autotrack_videos, but all extra keywords are ignored. |

## Returns and side effects

Returns `None`; its outputs are a Matplotlib figure and a printed tracking summary.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.autotracker._validate_size._validate_size`](_validate_size.md)
- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/autotracker/autotrack_videos_parameter_test.py`, lines 16–148 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/autotracker/autotrack_videos_parameter_test.py#L16-L148)
