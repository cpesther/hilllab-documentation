# bin_video

[Folder overview](index.md)

## Signature

```{py:function} bin_video(video_path, bin_size, print_output=True)
:module: hilllab.visual.bin_video
:canonical: hilllab.visual.bin_video.bin_video
```

## Behavior and usage

Returns the path string of `BINx<bin_size>_<stem>.avi` next to the source. Frames are cropped at the bottom/right to a multiple of `bin_size`, block-averaged across both spatial axes, and converted back to uint8; frame rate is retained. Use a positive integer bin size no larger than the image dimensions. This reduces resolution rather than summing pixel intensities.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. the path to the video to bin |
| `bin_size` | `required` | **int**. the size of the bins of pixels |
| `print_output` | `True` | **bool**. allows printed output messages to be disabled |

## Returns and side effects

Returns the path string of `BINx<bin_size>_<stem>.avi` next to the source.

## Source

`hilllab/visual/bin_video.py`, lines 7–68 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/bin_video.py#L7-L68)
