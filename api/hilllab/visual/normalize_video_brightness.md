# normalize_video_brightness

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
No guard handles zero/invalid sampled brightness or an unreadable sample set, and VideoWriter opening is not verified. XVID is used even when the retained input suffix is MP4; treat format compatibility as unresolved.
:::

## Signature

```{py:function} normalize_video_brightness(video_path, normalized_brightness, n_samples=5)
:module: hilllab.visual.normalize_video_brightness
:canonical: hilllab.visual.normalize_video_brightness.normalize_video_brightness
```

## Behavior and usage

Samples evenly spaced frames, computes their grayscale means, and multiplies every color frame by target/sample-mean brightness before clipping to uint8. Writes `NORM_<original-name>` beside the video and returns `None`; it does not return the output path or necessarily make a grayscale video.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. the path to the video to be normalized |
| `normalized_brightness` | `required` | **int**. the mean brightness to which the  video should be normalized. Any value between 0 and 255. |
| `n_samples` | `5` | **int**. the number of evenly spaced samples that should be taken to determine the brightness of the video before normalization. |

## Returns and side effects

Writes `NORM_<original-name>` beside the video and returns `None`; it does not return the output path or necessarily make a grayscale video.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.visual.calculate_mean_brightness.calculate_mean_brightness`](calculate_mean_brightness.md)

## Source

`hilllab/visual/normalize_video_brightness.py`, lines 8–76 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/normalize_video_brightness.py#L8-L76)
