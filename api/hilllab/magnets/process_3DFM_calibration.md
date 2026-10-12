# process_3DFM_calibration

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Its input-error text says XLSX/CSV despite using only loadmat. Velocity/drag fitting does not convert pixel displacement and frame intervals into SI units. Empty/short tracks, zero motion, missing peaks, and short smoothing windows are unguarded. Treat the exported coefficients as provisional rather than calibrated forces.
:::

## Signature

```{py:function} process_3DFM_calibration(video_path, voltage_path, bead_size_pixels=23, trajectory_fraction=0.05, max_travel_pixels=5, memory=0, invert=True, performance_mode='safe', manual_lag=-10, displacement_threshold=50, angle_threshold=30)
:module: hilllab.magnets.process_3DFM_calibration
:canonical: hilllab.magnets.process_3DFM_calibration.process_3DFM_calibration
```

## Behavior and usage

Tracks beads, filters by trajectory lifetime and displacement, aligns repeated voltage segments against motion by cross-correlation plus manual_lag frames, estimates an origin, applies angle filtering, and exports trajectory/coefficient Excel sheets beside the video. Returns `None`; also overwrites `vals.pkl` in the current working directory. Voltage input is actually MATLAB data requiring voltages, pulse_widths, NRepeats, calibrator_viscosity, bead_radius, and fps keys.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. the path to the video to be processed. |
| `voltage_path` | `required` | **str**. the path to the matlab file containing the voltages and durations. |
| `bead_size_pixels` | `23` | **int, optional**. Estimated diameter of the  particles in pixels. Default is 23. |
| `trajectory_fraction` | `0.05` | **float, optional**. Minimum fraction of frames a  particle must appear in to be retained after filtering. Default is 1.0. |
| `max_travel_pixels` | `5` | **int, optional**. Maximum number of pixels a particle  can travel between frames for TrackPy to consider it to be the same particle. Default is 5. |
| `memory` | `0` | **int, optional**. Memory parameter for TrackPy's linking,  specifying how long particles are remembered between frames. Default is 0. |
| `invert` | `True` | **bool, optional**. when false, bright spots on a dark background will be tracked. When true, dark spots on a bright background will be tracked. |
| `performance_mode` | `'safe'` | **string, 'safe', 'slow', or 'fast'**. Controls  how many processes are used by TrackPy to allow this task to be run safely in the background or sped up on demand. |
| `manual_lag` | `-10` | **int, optional**. the number of frames the voltage signal should be shifted in addition to that calculated by the correlation. |
| `displacement_threshold` | `50` | **int, optional**. the minimum displacement a  particle must exhibit to be considered "in-motion" and therefore be included in the force calculations. |
| `angle_threshold` | `30` | **int, optional**. the maximum angle at which a particles vector may intersect with the pole tip/origin axis before being excluded as an "off angle" particle. |

## Returns and side effects

Returns `None`; also overwrites `vals.pkl` in the current working directory.

## Source

`hilllab/magnets/process_3DFM_calibration.py`, lines 44–325 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/process_3DFM_calibration.py#L44-L325)
