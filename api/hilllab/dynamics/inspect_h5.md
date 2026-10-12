# inspect_h5

[Folder overview](index.md)

## Signature

```{py:function} inspect_h5(h5_path, show_parents=True)
:module: hilllab.dynamics.inspect_h5
:canonical: hilllab.dynamics.inspect_h5.inspect_h5
```

## Behavior and usage

Returns None after printing summary-row count, distinct VRPN source paths, parent-folder count, and presence of identifier/classification columns. show_parents=True also lists each source parent directory. It reads the summary key only and does not validate all HDF tables or analysis quality.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the file path to the h5 file to inspect |
| `show_parents` | `True` | **bool**. controls whether the parent folders of  every VRPN included in the h5 file should be printed. |

## Returns and side effects

Returns None after printing summary-row count, distinct VRPN source paths, parent-folder count, and presence of identifier/classification columns. show_parents=True also lists each source parent directory.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)

## Source

`hilllab/dynamics/inspect_h5.py`, lines 10–47 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/inspect_h5.py#L10-L47)
