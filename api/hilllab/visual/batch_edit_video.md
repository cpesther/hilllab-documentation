# batch_edit_video

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} batch_edit_video(input_folder, output_folder, **kwargs)
:module: hilllab.visual.batch_edit_video
:canonical: hilllab.visual.batch_edit_video.batch_edit_video
```

## Behavior and usage

Recursively edits AVI/MP4 inputs into AVI files in mirrored output folders and returns `None`. Extra keywords are forwarded to `edit_video`, but `show_preview` is explicitly False; passing that keyword again causes a duplicate-keyword TypeError. Existing destination names can be overwritten.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_folder` | `required` | **string**. the path to the folder containing videos and/or containing subfolders with videos |
| `output_folder` | `required` | **string**. the path to the folder where the converted videos should be saved. |
| `kwargs` | `extra keyword arguments` | Extra edit_video settings. Do not pass show_preview because this wrapper already sets it False. |

## Returns and side effects

Recursively edits AVI/MP4 inputs into AVI files in mirrored output folders and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.visual.edit_video.edit_video`](edit_video.md)

## Source

`hilllab/visual/batch_edit_video.py`, lines 9–45 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/batch_edit_video.py#L9-L45)
