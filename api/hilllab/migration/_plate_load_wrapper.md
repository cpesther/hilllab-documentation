# _plate_load_wrapper

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _plate_load_wrapper(path, data_type='SPE', **kwargs)
:module: hilllab.migration._plate_load_wrapper
:canonical: hilllab.migration._plate_load_wrapper._plate_load_wrapper
```

## Behavior and usage

Loads and prepares a migration Bundle, or offers to reuse a sibling `.1dpre.xlsx` saved bundle through console input. Returns the populated bundle. Extra keywords are forwarded to both loading and preparation; accepting a PRE bundle skips preparation entirely, preserving its saved settings.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. a file path to automatically load a file without opening a file dialog window. |
| `data_type` | `'SPE'` | **string**. Specifies the type model used to collect the  data. Options include 'SPE' (default), 'TEC', and 'PRE'. |
| `kwargs` | `extra keyword arguments` | passed down to load_file() and _plate_prepare_data(). |

## Returns and side effects

Returns the populated bundle.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration._plate_prepare_data._plate_prepare_data`](_plate_prepare_data.md)
- [`hilllab.migration.load_file.load_file`](load_file.md)

## Source

`hilllab/migration/_plate_load_wrapper.py`, lines 7–57 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_load_wrapper.py#L7-L57)
