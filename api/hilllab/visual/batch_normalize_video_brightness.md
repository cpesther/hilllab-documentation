# batch_normalize_video_brightness

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} batch_normalize_video_brightness(input_folder, extension='avi', **kwargs)
:module: hilllab.visual.batch_normalize_video_brightness
:canonical: hilllab.visual.batch_normalize_video_brightness.batch_normalize_video_brightness
```

## Behavior and usage

Runs normalization for every matching video recursively and returns `None`; keyword options such as `normalized_brightness` are forwarded. Each output is written beside its source, so later runs can discover earlier `NORM_` videos too.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_folder` | `required` | **str**. the path to the folder containing the videos type (str): the file extension of the video files to process |
| `extension` | `'avi'` | Case-sensitive complete filename suffix to include; a leading dot is optional. |
| `kwargs` | `extra keyword arguments` | Keywords forwarded to normalize_video_brightness, including required normalized_brightness and optional n_samples. |

## Returns and side effects

Runs normalization for every matching video recursively and returns `None`; keyword options such as `normalized_brightness` are forwarded.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.visual.normalize_video_brightness.normalize_video_brightness`](normalize_video_brightness.md)

## Source

`hilllab/visual/batch_normalize_video_brightness.py`, lines 6–28 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/batch_normalize_video_brightness.py#L6-L28)
