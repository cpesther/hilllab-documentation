# extract_frame

[Folder overview](index.md)

## Signature

```{py:function} extract_frame(video_path, output_folder, frame_index=0, scale_percent=100)
:module: hilllab.visual.extract_frame
:canonical: hilllab.visual.extract_frame.extract_frame
```

## Behavior and usage

Seeks the zero-based frame index, optionally resizes by `scale_percent`, saves `<stem>_frame<index>.png`, and returns the BGR frame array. The output folder is created automatically. `cv2.imwrite` success is not checked, so a printed message does not independently confirm the file write.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. Path to the AVI video file. |
| `output_folder` | `required` | **str**. Folder to save the PNG. |
| `frame_index` | `0` | **int**. the 0-based index of the frame to be saved |
| `scale_percent` | `100` | **float**. Percentage to downscale the frame (default 100 = no scaling). |

## Returns and side effects

Seeks the zero-based frame index, optionally resizes by `scale_percent`, saves `<stem>_frame<index>.png`, and returns the BGR frame array.

## Source

`hilllab/visual/extract_frame.py`, lines 5–48 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/extract_frame.py#L5-L48)
