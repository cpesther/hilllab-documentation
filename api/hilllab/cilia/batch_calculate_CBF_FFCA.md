# batch_calculate_CBF_FFCA

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} batch_calculate_CBF_FFCA(path, sampling_rate=60, method='cs', power_threshold=1, skip_existing=True, bypass_confirmation=False, delete_process_files=True, flag=None)
:module: hilllab.cilia.batch_calculate_CBF_FFCA
:canonical: hilllab.cilia.batch_calculate_CBF_FFCA.batch_calculate_CBF_FFCA
```

## Behavior and usage

Recursively analyzes lowercase AVI files with method `py` or `cs`, printing status and optionally prompting for confirmation; returns `None`, with one CSV per processed video. The batch threshold default is 1, while individual calculator defaults are 5. `delete_process_files` only affects the C# route. Skip status is based on an unprefixed output name even if flags are used.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. a path to a folder containing the AVI videos that should be processed. |
| `sampling_rate` | `60` | **int**. Frame rate of the video. |
| `method` | `'cs'` | **string**. either 'py' or 'cs'. If 'py', the  calculations will be performed by the pure Python code. If 'cs', the calculations will be performed by the compiled C# executable included in this module. |
| `power_threshold` | `1` | **int**. Minimum PSD value a pixel must exceed to  be considered ciliated. |
| `skip_existing` | `True` | **bool**. whether a video should be skipped if a  MATLAB file already exists with the same name. |
| `bypass_confirmation` | `False` | **bool**. allows the function to skip the  confirmation step that typically requires user input. |
| `delete_process_files` | `True` | For the C# route, attempt to remove intermediate PSD/frequency/meta files after successful resolution. |
| `flag` | `None` | Optional label stored in the results and prefixed to the output CSV filename; None means no prefix. |

## Returns and side effects

Recursively analyzes lowercase AVI files with method `py` or `cs`, printing status and optionally prompting for confirmation; returns `None`, with one CSV per processed video.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.cilia._calculate_CBF_FFCA_cs._calculate_CBF_FFCA_cs`](_calculate_CBF_FFCA_cs.md)
- [`hilllab.cilia._calculate_CBF_FFCA_py._calculate_CBF_FFCA_py`](_calculate_CBF_FFCA_py.md)
- [`hilllab.utilities.current_timestamp.current_timestamp`](../utilities/current_timestamp.md)

## Source

`hilllab/cilia/batch_calculate_CBF_FFCA.py`, lines 14–100 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/batch_calculate_CBF_FFCA.py#L14-L100)
