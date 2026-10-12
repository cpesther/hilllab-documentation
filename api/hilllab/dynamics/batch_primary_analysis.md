# batch_primary_analysis

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Folders containing only empty VRPNs and batches with no newly processed folders reach concat on empty lists. If the input root itself contains VRPNs, root-level compilation can overwrite its per-folder outputs. Existing-output skip is based only on HDF presence.
:::

## Signature

```{py:function} batch_primary_analysis(folder_path, fps, pixel_width, compile=True, skip_existing=True)
:module: hilllab.dynamics.batch_primary_analysis
:canonical: hilllab.dynamics.batch_primary_analysis.batch_primary_analysis
```

## Behavior and usage

Recursively analyzes `.vrpn.mat` files with shared fps and pixel_width calibrations. Writes per-folder summary/metadata Excel and summary/instantaneous/metadata HDF tables. With compile=True, also writes root-level compiled files and returns `(compiled_excel_path, compiled_h5_path)` strings; otherwise returns `(None, None)`. Skipped folders are not included in the new compiled output.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder_path` | `required` | **string**. the path to the folder containing VRPN files or containing folders with VRPN files. |
| `fps` | `required` | **int**. the frame rate of the video |
| `pixel_width` | `required` | **float**. the width of a pixel in micrometers |
| `compile` | `True` | When True, also concatenate newly processed folders into root-level Excel/HDF outputs. |
| `skip_existing` | `True` | When True, skip a file whose expected destination already exists; this checks existence, not whether its parameters match the current run. |

## Returns and side effects

With compile=True, also writes root-level compiled files and returns `(compiled_excel_path, compiled_h5_path)` strings; otherwise returns `(None, None)`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.dynamics.primary_analysis.primary_analysis`](primary_analysis.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)

## Source

`hilllab/dynamics/batch_primary_analysis.py`, lines 12–150 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/batch_primary_analysis.py#L12-L150)
