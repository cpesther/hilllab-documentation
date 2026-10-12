# _get_camera_info

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _get_camera_info(camera, magnification=None)
:module: hilllab.visual._get_camera_info
:canonical: hilllab.visual._get_camera_info._get_camera_info
```

## Behavior and usage

Reads the packaged camera JSON and returns the selected camera dictionary. Unknown camera names raise KeyError. If magnification is supplied, it must be at least 1 and `magnified_pixel_width_um` is calculated as sensor pixel width divided by magnification. This is a calibration lookup, not video metadata inspection.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `camera` | `required` | **string**. the three character code indicating what camera properties should be returned. |
| `magnification` | `None` | **float**. the factor of magnification applied when this video was recorded. For example, a value of 40 indicates 40x magnification. |

## Returns and side effects

Reads the packaged camera JSON and returns the selected camera dictionary.

## Source

`hilllab/visual/_get_camera_info.py`, lines 5–48 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/_get_camera_info.py#L5-L48)
