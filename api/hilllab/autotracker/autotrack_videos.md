# autotrack_videos

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The module imports `._generate_new_VRPN`, but the supplied file is `_generate_new_vrpn.py`; it then calls `_generate_vrpn` without importing that name. These prevent the current workflow from running. Single-file input computes its output path relative to the file rather than its parent, which can escape the intended save folder. Safe mode computes CPU count minus two without a positive lower bound.
:::

## Signature

```{py:function} autotrack_videos(video_path=None, save_path=None, bead_size_pixels=21, trajectory_fraction=1.0, max_travel_pixels=5, memory=0, invert=False, performance_mode='safe', skip_existing=True, return_file_details=False, bypass_confirmation=False)
:module: hilllab.autotracker.autotrack_videos
:canonical: hilllab.autotracker.autotrack_videos.autotrack_videos
```

## Behavior and usage

Recursively finds AVI/MP4 files, takes each frame's green channel, locates and links spots with TrackPy, and filters trajectory length, mass, size, and eccentricity before MATLAB export. Directory inputs mirror subfolders below `save_path`. `trajectory_fraction` sets the minimum retained frame count; `skip_existing=True` skips existing `.vrpn.mat` outputs. Returns a file-keyed details dictionary only when `return_file_details=True`, otherwise `None`; skipped entries contain fewer fields. `bypass_confirmation=True` avoids console input. All frames are loaded into memory.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `None` | **str**. path to the folder with videos or to a single video. |
| `save_path` | `None` | **str**. path to the folder where VRPNs should be saved |
| `bead_size_pixels` | `21` | **int, optional**. Estimated diameter of the  particles in pixels. Default is 21. |
| `trajectory_fraction` | `1.0` | **float, optional**. Minimum fraction of frames a  particle must appear in to be retained after filtering. Default is 1.0. |
| `max_travel_pixels` | `5` | **int, optional**. Maximum number of pixels a particle  can travel between frames for TrackPy to consider it to be the same particle. Default is 5. |
| `memory` | `0` | **int, optional**. Memory parameter for TrackPy's linking,  specifying how long particles are remembered between frames. Default is 0. |
| `invert` | `False` | **bool, optional**. when false, bright spots on a dark background will be tracked. When true, dark spots on a bright background will be tracked. |
| `performance_mode` | `'safe'` | **string, 'safe', 'slow', or 'fast'**. Controls  how many processes are used by TrackPy to allow this task to be run safely in the background or sped up on demand. |
| `skip_existing` | `True` | When True, skip a file whose expected destination already exists; this checks existence, not whether its parameters match the current run. |
| `return_file_details` | `False` | **bool, optional**. allows the function to  return a dict containing file details useful for higher level functions. Defaults to false. |
| `bypass_confirmation` | `False` | **bool, optional**. when True, the function will not ask for user confirmation of parameters before running autotracking. Mostly used when nested in other functions, defaults to false. |

## Returns and side effects

Returns a file-keyed details dictionary only when `return_file_details=True`, otherwise `None`; skipped entries contain fewer fields.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.autotracker._validate_size._validate_size`](_validate_size.md)
- [`hilllab.utilities.current_timestamp.current_timestamp`](../utilities/current_timestamp.md)
- [`hilllab.utilities.format_duration.format_duration`](../utilities/format_duration.md)
- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.widgets.button_open_path.button_open_path`](../widgets/button_open_path.md)

## Source

`hilllab/autotracker/autotrack_videos.py`, lines 28–333 · Local working-tree version; differs from the recorded repository revision.
