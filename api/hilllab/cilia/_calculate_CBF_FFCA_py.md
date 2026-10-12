# _calculate_CBF_FFCA_py

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The plot argument is accepted but not forwarded to the resolver and has no effect. Unreadable trailing frames remain zero-filled. Float16 PSD storage can lose precision or overflow, and skip returns a different tuple length.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _calculate_CBF_FFCA_py(video_path, sampling_rate=60, power_threshold=5, skip_existing=True, plot=False, flag=None)
:module: hilllab.cilia._calculate_CBF_FFCA_py
:canonical: hilllab.cilia._calculate_CBF_FFCA_py._calculate_CBF_FFCA_py
```

## Behavior and usage

Loads grayscale frames, removes each pixel's mean, computes a one-sided PSD, zeroes the first 15 frequency bins, and writes CBF/FFCA via the shared resolver. This cutoff is bin-based, not a fixed Hz threshold; it changes with video length and sampling rate. Successful processing returns `(cbf, ffca, psd_map)` with float16 PSD storage; skips return `(None, None)`. Full frame/PSD arrays can be large.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `video_path` | `required` | **str**. Path to the AVI video to be processed. |
| `sampling_rate` | `60` | **int**. Frame rate of the video. |
| `power_threshold` | `5` | **int**. Minimum PSD value a pixel must exceed to  be considered ciliated. |
| `skip_existing` | `True` | **bool**. whether a video should be skipped if a  MATLAB file already exists with the same name. |
| `plot` | `False` | **bool**. whether plots should be created and saved for  each video. |
| `flag` | `None` | Optional label stored in the results and prefixed to the output CSV filename; None means no prefix. |

## Returns and side effects

Successful processing returns `(cbf, ffca, psd_map)` with float16 PSD storage; skips return `(None, None)`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.cilia._resolve_CBF_FFCA._resolve_CBF_FFCA`](_resolve_CBF_FFCA.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)

## Source

`hilllab/cilia/_calculate_CBF_FFCA_py.py`, lines 12–128 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/_calculate_CBF_FFCA_py.py#L12-L128)
