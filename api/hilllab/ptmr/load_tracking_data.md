# load_tracking_data

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The default Python branch reads into vrpn_data but then formats undefined raw_data, causing UnboundLocalError. Unknown pipeline values also enter this broken branch. Event VRPNs can fail the formatter's unconditional microseconds drop.
:::

## Signature

```{py:function} load_tracking_data(path, fps, camera, magnification, pipeline='python', units='um')
:module: hilllab.ptmr.load_tracking_data
:canonical: hilllab.ptmr.load_tracking_data.load_tracking_data
```

## Behavior and usage

The MATLAB branch loads a VRPN and intends to return a formatted, physically scaled tracking DataFrame. Inputs include fps, camera, magnification, and unit choice; formatting mutates the loaded table.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Tracking file path: CSV for python or VRPN MAT for matlab. |
| `fps` | `required` | **int**. the frame rate of the VRPN used for converting frame  numbers to timestamps. |
| `camera` | `required` | **str**. the three charcter code used for pulling the  pixel width of the camera for converting the coordiantes into um from pixels. |
| `magnification` | `required` | **float**. the factor of magnification applied when this video was recorded. |
| `pipeline` | `'python'` | matlab selects load_vrpn; other values select the currently broken CSV branch. |
| `units` | `'um'` | **string**. the units that the coordiates should be returned using. Defaults to 'um', but valid values include 'm', 'cm', 'mm', 'um', and 'nm'. |

## Returns and side effects

The MATLAB branch loads a VRPN and intends to return a formatted, physically scaled tracking DataFrame.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.ptmr._format_vrpn._format_vrpn`](_format_vrpn.md)
- [`hilllab.utilities.load_vrpn.load_vrpn`](../utilities/load_vrpn.md)

## Source

`hilllab/ptmr/load_tracking_data.py`, lines 7–37 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/load_tracking_data.py#L7-L37)
