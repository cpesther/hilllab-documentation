# _calculate_CBF_FFCA_cs

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
A failed subprocess only prints diagnostics, then the code still tries to read output files; absent or stale intermediate files are not handled safely. Return tuple length varies on skip. Requires the Windows executable and its native DLLs.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _calculate_CBF_FFCA_cs(video_path, sampling_rate=60, power_threshold=5, bin_size=None, skip_existing=True, delete_process_files=True, flag=None)
:module: hilllab.cilia._calculate_CBF_FFCA_cs
:canonical: hilllab.cilia._calculate_CBF_FFCA_cs._calculate_CBF_FFCA_cs
```

## Behavior and usage

Runs the bundled Windows FFTProcessor executable, loads float32 PSD data shaped `(height, width, frames//2+1)`, resolves CBF/FFCA, and writes a sibling CSV. `sampling_rate` is supplied in Hz rather than read from video metadata. Optional binning creates a separate BINx AVI. Successful processing returns `(cbf, ffca, psd_map)`; skip-existing returns only `(None, None)`. Temporary binary/meta files are optionally deleted.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. Path to the AVI video to be processed. |
| `sampling_rate` | `60` | **int**. Frame rate of the video. |
| `power_threshold` | `5` | **int**. Minimum PSD value a pixel must exceed to  be considered ciliated. |
| `bin_size` | `None` | Optional positive integer spatial block size. None disables pre-binning; otherwise a separate binned AVI is created. |
| `skip_existing` | `True` | **bool**. whether a video should be skipped if a  MATLAB file already exists with the same name. |
| `delete_process_files` | `True` | **bool**. If true, the binary files created by the FFTProcessor.exe will be deleted once finished to free up disk space. |
| `flag` | `None` | Optional label stored in the results and prefixed to the output CSV filename; None means no prefix. |

## Returns and side effects

Successful processing returns `(cbf, ffca, psd_map)`; skip-existing returns only `(None, None)`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.cilia._resolve_CBF_FFCA._resolve_CBF_FFCA`](_resolve_CBF_FFCA.md)

## Source

`hilllab/cilia/_calculate_CBF_FFCA_cs.py`, lines 10–122 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/_calculate_CBF_FFCA_cs.py#L10-L122)
