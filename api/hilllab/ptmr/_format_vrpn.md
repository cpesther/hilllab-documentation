# _format_vrpn

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _format_vrpn(data, fps, camera, magnification, units='um')
:module: hilllab.ptmr._format_vrpn
:canonical: hilllab.ptmr._format_vrpn._format_vrpn
```

## Behavior and usage

Mutates and returns the same tracking DataFrame: replaces timestamps with frame/fps seconds, drops microseconds, sorts particle_id/frame, and converts x/y/z using camera sensor pixel width divided by magnification. Units may be m/cm/mm/um/nm; unrecognized units leave pixel values unchanged rather than raising. Expected columns include frame, microseconds, particle_id, x/y/z. Nine-column event VRPN data lack microseconds and fail the unconditional drop.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **pandas.DataFrame**. the dataframe with the data from the loaded VRPN. |
| `fps` | `required` | **int**. the frame rate of the VRPN used for converting frame  numbers to timestamps. |
| `camera` | `required` | **str**. the three charcter code used for pulling the  pixel width of the camera for converting the coordiantes into um from pixels. |
| `magnification` | `required` | **float**. the factor of magnification applied when this video was recorded. |
| `units` | `'um'` | **string**. the units that the coordiates should be returned using. Defaults to 'um', but valid values include 'm', 'cm', 'mm', 'um', and 'nm'. Any other value will return the coordinates in their native unit of pixels. |

## Returns and side effects

Mutates and returns the same tracking DataFrame: replaces timestamps with frame/fps seconds, drops microseconds, sorts particle_id/frame, and converts x/y/z using camera sensor pixel width divided by magnification.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.visual._get_camera_info._get_camera_info`](../visual/_get_camera_info.md)

## Source

`hilllab/ptmr/_format_vrpn.py`, lines 4–70 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/_format_vrpn.py#L4-L70)
