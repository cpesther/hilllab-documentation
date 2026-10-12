# batch_convert_to_avi

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} batch_convert_to_avi(input_folder, output_folder, **kwagrs)
:module: hilllab.visual.batch_convert_to_avi
:canonical: hilllab.visual.batch_convert_to_avi.batch_convert_to_avi
```

## Behavior and usage

Recursively converts MP4 files only, preserving relative subfolders and writing `.avi` below `output_folder`; returns `None`. The misspelled `**kwagrs` receives keyword options and forwards them correctly to `convert_to_avi`. Parent output folders are created.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_folder` | `required` | **string**. the path to the folder containing videos and/or containing subfolders with videos |
| `output_folder` | `required` | **string**. the path to the folder where the converted videos should be saved. |
| `kwagrs` | `extra keyword arguments` | Extra keywords forwarded to convert_to_avi, such as grayscale and codec. The source spelling is kwagrs. |

## Returns and side effects

Recursively converts MP4 files only, preserving relative subfolders and writing `.avi` below `output_folder`; returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.visual.convert_to_avi.convert_to_avi`](convert_to_avi.md)

## Source

`hilllab/visual/batch_convert_to_avi.py`, lines 9–46 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/batch_convert_to_avi.py#L9-L46)
