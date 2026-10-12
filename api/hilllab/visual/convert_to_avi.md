# convert_to_avi

[Folder overview](index.md)

## Signature

```{py:function} convert_to_avi(video_path, output_path, grayscale=False, codec='XVID')
:module: hilllab.visual.convert_to_avi
:canonical: hilllab.visual.convert_to_avi.convert_to_avi
```

## Behavior and usage

Writes to the explicit `output_path` and returns `None`. It uses the source frame size/rate, falls back to 30 fps if the rate is falsy, and optionally performs BGR-to-gray conversion. The output parent folder must already exist; failed input/writer opening raises an error. The codec must be a four-character codec supported by the environment.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **string**. the path to the video |
| `output_path` | `required` | **string**. the full output path where the converted video will be saved. Should end with .avi. |
| `grayscale` | `False` | **bool**. whether the video should be converted to grayscale. |
| `codec` | `'XVID'` | **string, default 'XVID'**. the coded used for the converted video |

## Returns and side effects

Writes to the explicit `output_path` and returns `None`.

## Source

`hilllab/visual/convert_to_avi.py`, lines 7–68 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/convert_to_avi.py#L7-L68)
