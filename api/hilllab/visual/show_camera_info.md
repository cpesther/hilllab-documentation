# show_camera_info

[Folder overview](index.md)

## Signature

```{py:function} show_camera_info()
:module: hilllab.visual.show_camera_info
:canonical: hilllab.visual.show_camera_info.show_camera_info
```

## Behavior and usage

Prints every camera's JSON specifications as console tables and returns `None`. This does not inspect a connected camera or calculate magnified pixel sizes; use `_get_camera_info` with magnification for the latter.

## Inputs

No explicit input arguments.

## Returns and side effects

Prints every camera's JSON specifications as console tables and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)
- [`hilllab.visual._get_camera_info._get_camera_info`](_get_camera_info.md)

## Source

`hilllab/visual/show_camera_info.py`, lines 8–29 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/show_camera_info.py#L8-L29)
