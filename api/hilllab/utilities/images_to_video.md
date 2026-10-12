# images_to_video

[Folder overview](index.md)

## Signature

```{py:function} images_to_video(image_folder, fps=30)
:module: hilllab.utilities.images_to_video
:canonical: hilllab.utilities.images_to_video.images_to_video
```

## Behavior and usage

Lexicographically sorts immediate lowercase JPG/PNG filenames, resizes every readable image to the first image's dimensions, and writes `<folder-name>.avi` in that folder using XVID and the requested `fps`. Returns `None`. Unreadable later images are skipped. Use zero-padded filenames for chronological order, and keep frame dimensions consistent to avoid unintended resizing.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `image_folder` | `required` | **string**. the path to the folder filled with images |
| `fps` | `30` | **int**. the frame rate of the resultant video |

## Returns and side effects

Returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](print_progress_bar.md)

## Source

`hilllab/utilities/images_to_video.py`, lines 9–54 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/images_to_video.py#L9-L54)
