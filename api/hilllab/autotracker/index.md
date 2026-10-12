# hilllab.autotracker

Track bead-like features in videos with TrackPy and export MATLAB-compatible VRPN trajectories.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`autotrack_select_paths`](autotrack_select_paths.md) | Opens two desktop directory dialogs and recursively counts lowercase `.avi` files. | documented |
| [`autotrack_videos`](autotrack_videos.md) | Recursively finds AVI/MP4 files, takes each frame's green channel, locates and links spots with TrackPy, and filters trajectory length, mass, size, and eccentricity before MATLAB export. | needs review |
| [`autotrack_videos_parameter_test`](autotrack_videos_parameter_test.md) | Selects the given video or the first AVI/MP4 discovered in a folder, reads up to `n_frames`, and displays detected spots and linked trajectories. | needs review |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_generate_new_vrpn`](_generate_new_vrpn.md) | The supplied implementation is functionally the same VRPN export loop as `_generate_vrpn`, with an explicit bare return. | needs review |
| [`_generate_vrpn`](_generate_vrpn.md) | Writes a MATLAB file at `path`; returns `None`. | needs review |
| [`_validate_size`](_validate_size.md) | Returns the provided `bead_size_pixels`, increased by one when it is even, and emits a warning on adjustment. | documentation in progress |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`autotrack_videos.gray`](autotrack_videos.gray.md) | A nested PIMS pipeline callback taking an H×W×C image and returning `image[:, :, 1]`, the green channel. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

_generate_new_vrpn <_generate_new_vrpn>
_generate_vrpn <_generate_vrpn>
_validate_size <_validate_size>
autotrack_select_paths <autotrack_select_paths>
autotrack_videos <autotrack_videos>
autotrack_videos.gray <autotrack_videos.gray>
autotrack_videos_parameter_test <autotrack_videos_parameter_test>
```
