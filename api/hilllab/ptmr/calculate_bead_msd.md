# calculate_bead_msd

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The default Python loader route uses an undefined raw_data variable. The MSD table is indexed by bead_id but assigned using bead_index, so noncontiguous IDs create/misalign rows. units is not forwarded to the loader and mainly labels the plot; MSD units are squared coordinate units. Missing frame intervals are not accounted for.
:::

## Signature

```{py:function} calculate_bead_msd(path, fps, camera, magnification, units='um', lag_frames=None, plot=False, save_plot=False, pipeline='python')
:module: hilllab.ptmr.calculate_bead_msd
:canonical: hilllab.ptmr.calculate_bead_msd.calculate_bead_msd
```

## Behavior and usage

Intended return is `(ensemble_msd, msd)`: a per-lag ensemble mean/std/time table and a transposed individual-bead MSD table indexed by lag time seconds. Calculates XY squared displacement by row-offset lag; lags longer than a trajectory are left missing. `lag_frames` must be positive integer offsets. Plot saving only occurs within plot=True.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. Tracking file path passed to load_tracking_data: CSV for pipeline=python or VRPN MAT for pipeline=matlab. The default loader route currently needs review. |
| `fps` | `required` | **int**. the frame rate of the VRPN used for converting frame  numbers to timestamps. |
| `camera` | `required` | **str**. the three charcter code used for pulling the  pixel width of the camera for converting the coordiantes into um from pixels. |
| `magnification` | `required` | **float**. the factor of magnification applied when this video was recorded. |
| `units` | `'um'` | **string**. Text used to label the plot; it is not forwarded to load_tracking_data. Coordinates are loaded using the default um conversion, so calculated MSD units are µm², not whatever string is supplied here. |
| `lag_frames` | `None` | **list**. Positive integer row-offset lags. None uses [1,2,5,10,20,50,100,200,500,1000,1001]. These are differences between samples, not absolute frame indices. |
| `plot` | `False` | **bool**. whether a plot of the MSD over time should be created |
| `save_plot` | `False` | **bool**. whether the MSD plot created should be saved  as a PNG to the same directory as the VRPN |
| `pipeline` | `'python'` | **string**. Selects the input loader route: python for CSV and matlab for VRPN MAT. It does not select an output file format in this function. |

## Returns and side effects

Intended return is `(ensemble_msd, msd)`: a per-lag ensemble mean/std/time table and a transposed individual-bead MSD table indexed by lag time seconds.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.ptmr.load_tracking_data.load_tracking_data`](load_tracking_data.md)
- [`hilllab.utilities.custom_axes.custom_axes`](../utilities/custom_axes.md)

## Source

`hilllab/ptmr/calculate_bead_msd.py`, lines 10–141 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/calculate_bead_msd.py#L10-L141)
