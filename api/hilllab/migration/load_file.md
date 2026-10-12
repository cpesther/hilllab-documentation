# load_file

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
PRE restores groups and calibration_columns as DataFrames, while downstream code treats them as dictionaries. Loading a prepared bundle therefore does not guarantee compatibility with grouped reports/calibration. Input row counts are truncated to int(rows/16), without validating complete reads.
:::

## Signature

```{py:function} load_file(path, data_type='SPE', extended=False, **kwargs)
:module: hilllab.migration.load_file
:canonical: hilllab.migration.load_file.load_file
```

## Behavior and usage

Returns a Bundle with raw plate data and overflow metadata. SPE reads 24 columns from a UTF-16 tab export; TEC reads XLSX/XLS/CSV then trims layout rows; SIM reads an Excel table with a <> index; PRE restores named preprocessing sheets. Extended mode converts extra rows into additional columns. Path is required; no file chooser is opened, despite the docstring. kwargs are accepted but unused.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. a file path to automatically load a file without opening a file dialog window. |
| `data_type` | `'SPE'` | **string**. Specifies the type model used to collect the  data. Options include 'SPE' (default), 'TEC', and 'PRE'. |
| `extended` | `False` | For non-PRE data, convert the bottom four plate rows into eight additional pseudo-columns. PRE loads its saved mode. |
| `kwargs` | `extra keyword arguments` | None used, but will accept anyways. |

## Returns and side effects

Returns a Bundle with raw plate data and overflow metadata.

## Related HillLab tools

Shared functions and classes used by this tool:

- {ref}`hilllab.migration.Bundle.Bundle <class-bundle>`
- [`hilllab.migration._plate_format_extended._plate_format_extended`](_plate_format_extended.md)
- [`hilllab.migration._plate_remove_overflows._plate_remove_overflows`](_plate_remove_overflows.md)

## Source

`hilllab/migration/load_file.py`, lines 13–172 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/load_file.py#L13-L172)
