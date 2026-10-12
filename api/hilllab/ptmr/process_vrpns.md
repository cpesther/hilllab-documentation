# process_vrpns

[Folder overview](index.md)

:::{admonition} Incomplete feature — in progress
:class: warning
Incomplete feature: the processing pipeline is not implemented, and its docstring is a placeholder.
:::

## Signature

```{py:function} process_vrpns(folder, camera='GS3', magnification=40, bead_size=1, fps=120, long_video=False, drift_subtraction='linear', pipeline='python')
:module: hilllab.ptmr.process_vrpns
:canonical: hilllab.ptmr.process_vrpns.process_vrpns
```

## Behavior and usage

Accepts folder/calibration/processing options but the body is pass, returning None. It does not discover files, subtract drift, calculate MSD, or export results.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder` | `required` | **string**. highest level directory containing subdirectories  with VRPNs |
| `camera` | `'GS3'` | **string**. camera identifier, expected 'GS3' or 'FL3' |
| `magnification` | `40` | Objective/system magnification used with camera sensor pixel width. This parameter is currently unused in the process_vrpns stub. |
| `bead_size` | `1` | **int**. bead size in pixels |
| `fps` | `120` | Acquisition frame rate in frames per second, used to convert frame indices to seconds where implemented. |
| `long_video` | `False` | **bool**. True if long video, False otherwise |
| `drift_subtraction` | `'linear'` | **None or string**. controls the method of drift subtraction applied to the VRPNs. If None, then no drift subtraction will be applied. |
| `pipeline` | `'python'` | **string**. either 'python' or 'matlab'. Controls whether files are saved as MATLAB files compatible with legacy code or as CSV and Excel docs compatible with this Python library. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/ptmr/process_vrpns.py`, lines 5–23 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/process_vrpns.py#L5-L23)
