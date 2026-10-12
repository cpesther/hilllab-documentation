# hilllab.magnets

Track beads in 3DFM calibration videos, align voltage schedules, and fit provisional force-distance relationships.

## Subfolders

| Group | Purpose |
| --- | --- |
| [gui](gui/index.md) | MATLAB magnet-drive and synchronized-camera tools, including hardware-specific routines and a packaged App Designer project. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`process_3DFM_calibration`](process_3DFM_calibration.md) | Tracks beads, filters by trajectory lifetime and displacement, aligns repeated voltage segments against motion by cross-correlation plus manual_lag frames, estimates an origin, applies angle filtering, and exports trajectory/coefficient Excel sheets beside the video. | needs review |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_calculate_force_distance`](_calculate_force_distance.md) | Returns a list of `(voltage, m, c)` fits using natural logs: `log(force)=m*log(distance)+c`. | needs review |
| [`_calculate_origin_from_lines`](_calculate_origin_from_lines.md) | Accepts at least two lines represented by endpoint pairs and returns a least-squares `(x, y)` origin, or None after a caught linear algebra error. | needs review |
| [`_get_pole_tip`](_get_pole_tip.md) | Shows an OpenCV image window, records the most recent left click, and returns `(x, y)` image coordinates or None if nothing is selected. | documentation in progress |
| [`_remove_wide_angles`](_remove_wide_angles.md) | Returns a filtered DataFrame copy of rows within `angle_threshold` degrees of the origin-to-pole-tip direction. | documentation in progress |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`_get_pole_tip.click_event`](_get_pole_tip.click_event.md) | Closure-local OpenCV mouse callback returning None and updating the parent pole_tip list only for a left-button-down event. x/y are image coordinates; flags and params are accepted but unused. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

gui <gui/index>
_calculate_force_distance <_calculate_force_distance>
_calculate_origin_from_lines <_calculate_origin_from_lines>
_get_pole_tip <_get_pole_tip>
_get_pole_tip.click_event <_get_pole_tip.click_event>
_remove_wide_angles <_remove_wide_angles>
process_3DFM_calibration <process_3DFM_calibration>
```
