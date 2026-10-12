# batch_extract_frame

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} batch_extract_frame(input_folder, output_folder, frame_index=0, scale_percent=100, extension='avi')
:module: hilllab.visual.batch_extract_frame
:canonical: hilllab.visual.batch_extract_frame.batch_extract_frame
```

## Behavior and usage

Recursively finds matching videos and saves one PNG per video into a shared output folder; returns `None`. It forwards zero-based `frame_index` and scale percentage. Videos with the same stem in different folders can overwrite each other's PNGs.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_folder` | `required` | **str**. the path to the folder containing videos |
| `output_folder` | `required` | **str**. Folder to save the PNGs. |
| `frame_index` | `0` | **int**. the 0-based index of the frame to be saved. |
| `scale_percent` | `100` | **float**. Percentage to downscale the frame (default 100 = no scaling). type (str): the file extension of the type of video to process. |
| `extension` | `'avi'` | Case-sensitive complete filename suffix to include; a leading dot is optional. |

## Returns and side effects

Recursively finds matching videos and saves one PNG per video into a shared output folder; returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.visual.extract_frame.extract_frame`](extract_frame.md)

## Source

`hilllab/visual/batch_extract_frame.py`, lines 6–32 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/batch_extract_frame.py#L6-L32)
