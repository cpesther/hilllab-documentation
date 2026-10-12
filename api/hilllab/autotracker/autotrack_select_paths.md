# autotrack_select_paths

[Folder overview](index.md)

## Signature

```{py:function} autotrack_select_paths()
:module: hilllab.autotracker.autotrack_select_paths
:canonical: hilllab.autotracker.autotrack_select_paths.autotrack_select_paths
```

## Behavior and usage

Opens two desktop directory dialogs and recursively counts lowercase `.avi` files. Returns `(video_path, save_path)` strings, or `(None, None)` if either selection is cancelled. A directory containing no AVI files only prints an alert; it is still returned. This requires a desktop Tk environment.

## Inputs

No explicit input arguments.

## Returns and side effects

Returns `(video_path, save_path)` strings, or `(None, None)` if either selection is cancelled.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.current_timestamp.current_timestamp`](../utilities/current_timestamp.md)
- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)

## Source

`hilllab/autotracker/autotrack_select_paths.py`, lines 14–60 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/autotracker/autotrack_select_paths.py#L14-L60)
