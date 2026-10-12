# calculate_mean_brightness

[Folder overview](index.md)

## Signature

```{py:function} calculate_mean_brightness(video_path=None, frame=None)
:module: hilllab.visual.calculate_mean_brightness
:canonical: hilllab.visual.calculate_mean_brightness.calculate_mean_brightness
```

## Behavior and usage

Returns NumPy's mean of the BGR-to-gray converted supplied frame, or the first video frame if no frame is given. Input frames must be OpenCV-style BGR arrays, not already-grayscale arrays. Supplying both arguments prioritizes `frame`. With neither, the code prints an error but still tries to open a video.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `None` | **string**. the path to the video file |
| `frame` | `None` | **numpy.array**. 2D array of values |

## Returns and side effects

Returns NumPy's mean of the BGR-to-gray converted supplied frame, or the first video frame if no frame is given.

## Source

`hilllab/visual/calculate_mean_brightness.py`, lines 5–44 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/calculate_mean_brightness.py#L5-L44)
