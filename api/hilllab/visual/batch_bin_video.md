# batch_bin_video

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} batch_bin_video(input_folder, bin_size, extension='avi')
:module: hilllab.visual.batch_bin_video
:canonical: hilllab.visual.batch_bin_video.batch_bin_video
```

## Behavior and usage

Recursively processes files matching the full `extension`, saves each binned AVI beside its source, and returns `None`. It does not collect the output paths returned by `bin_video`. An empty folder reaches a progress-bar call with total zero.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_folder` | `required` | **str**. the path to the folder of videos to bin |
| `bin_size` | `required` | **int**. the size of the bins of pixels type (str): the file type extension of the videos to be binned. |
| `extension` | `'avi'` | Case-sensitive complete filename suffix to include; a leading dot is optional. |

## Returns and side effects

Recursively processes files matching the full `extension`, saves each binned AVI beside its source, and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.visual.bin_video.bin_video`](bin_video.md)

## Source

`hilllab/visual/batch_bin_video.py`, lines 6–26 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/batch_bin_video.py#L6-L26)
