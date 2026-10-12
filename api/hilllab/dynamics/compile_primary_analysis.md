# compile_primary_analysis

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Tables are appended sequentially before failure, so a partly readable file can contribute summary data without its matching instantaneous/metadata rows. Discovery includes prior analysis/classification outputs and can duplicate source data. No valid inputs causes concat failure.
:::

## Signature

```{py:function} compile_primary_analysis(folder_path, save_file=True)
:module: hilllab.dynamics.compile_primary_analysis
:canonical: hilllab.dynamics.compile_primary_analysis.compile_primary_analysis
```

## Behavior and usage

Recursively reads HDF summary/instantaneous/metadata tables and concatenates each. `save_file=False` returns all three DataFrames; True writes a `.batch.h5` file and returns None. Existing output prompts to overwrite or creates a timestamped alternative. Files missing expected keys are caught.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder_path` | `required` | **string**. a path to the parent folder containing H5 files, or containing subfolders with H5 files. |
| `save_file` | `True` | **bool**. controls whether the compiled dataset is saved to an H5 file or just returned. |

## Returns and side effects

`save_file=False` returns all three DataFrames; True writes a `.batch.h5` file and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)

## Source

`hilllab/dynamics/compile_primary_analysis.py`, lines 13–93 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/compile_primary_analysis.py#L13-L93)
