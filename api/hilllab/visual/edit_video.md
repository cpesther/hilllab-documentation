# edit_video

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The output writer is opened before preview confirmation, so declining can leave an empty destination file. Brightness uses convertScaleAbs, which takes absolute values rather than a simple signed offset. The output directory is not created here.
:::

## Signature

```{py:function} edit_video(video_path, output_path, brightness=0, contrast=1.0, gamma=1.0, saturation=1.0, sharpness=0.0, codec='XVID', show_preview=False)
:module: hilllab.visual.edit_video
:canonical: hilllab.visual.edit_video.edit_video
```

## Behavior and usage

Writes the edited video and returns `None`. Applies contrast/brightness via convertScaleAbs, reciprocal-gamma lookup, HSV saturation scaling, then unsharp masking when sharpness is positive. `gamma` must be positive; dimensions and rate are retained, with a 30-fps fallback. Preview mode shows first-frame comparisons and asks for confirmation.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **string**. the path to the video to be edited |
| `output_path` | `required` | **string**. the full path where the edited video  should be saved. |
| `brightness` | `0` | **int, optional**. value added to each pixel intensity. Negative values darken the image, positive values brighten it. Recommended range is -100 to 100. Default is 0. |
| `contrast` | `1.0` | **float, optional**. scales difference between light and dark regions. Values above 1 increase contrast while values between 0 and 1 decrease it. Recommended range is 0.5 to 2.0. Default is 1.0. |
| `gamma` | `1.0` | **float, optional**. nonlinear brightness correction factor. Values below 1 brighten shadows, values above 1 darken shadows. Recommended range is 0.5 to 2.5. Default is 1.0. |
| `saturation` | `1.0` | **float, optional**. multiplies color intensity. Values above 1 increase color vividness, values between 0 and 1 reduce saturation. A value of 0 produces grayscale. Recommended range is 0 to 3. Default is 1.0. |
| `sharpness` | `0.0` | **float, optional**. controls edge enhancement strength. Higher values increase edge contrast and detail but may introduce noise or artifacts. Recommended range is 0 to 2. Default is 0.0. |
| `codec` | `'XVID'` | **string, optional**. four character video codec identifier used for encoding the output video. Must be supported by the system's OpenCV build. Default is 'XVID'. |
| `show_preview` | `False` | **bool, optional**. if True, displays the first frame of the video side by side before and after edits using matplotlib before processing begins allowing user to confirm. Default is False. |

## Returns and side effects

Writes the edited video and returns `None`.

## Source

`hilllab/visual/edit_video.py`, lines 9–141 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/edit_video.py#L9-L141)
