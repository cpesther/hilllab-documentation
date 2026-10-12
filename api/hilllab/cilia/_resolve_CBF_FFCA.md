# _resolve_CBF_FFCA

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Despite the docstring's optional-output wording, output_path is used unconditionally. The requested FFCA plot panel is created but never populated. No physiological frequency-range filter is applied in this resolver.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _resolve_CBF_FFCA(psd_map, frequency_vector, power_threshold, output_path, method, plot=False, flag=None)
:module: hilllab.cilia._resolve_CBF_FFCA
:canonical: hilllab.cilia._resolve_CBF_FFCA._resolve_CBF_FFCA
```

## Behavior and usage

Returns `(cbf, ffca)`: CBF is the frequency of maximum spatially averaged PSD, and FFCA is the fraction of pixels whose maximum PSD exceeds the threshold. Requires a matching frequency vector and nonempty 3D PSD array. Always writes cbf/ffca/method/flag CSV data; `flag` prefixes the output filename. FFCA is a 0–1 fraction, not percent.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `psd_map` | `required` | Three-dimensional numeric array (height, width, frequency bins). |
| `frequency_vector` | `required` | Frequency values in Hz, with length matching the last PSD-map axis. |
| `power_threshold` | `required` | Pixel is counted as functional when its maximum PSD strictly exceeds this scalar. |
| `output_path` | `required` | Required CSV destination path; the parent folder must exist. |
| `method` | `required` | Method label written to the CSV, normally py or cs; it does not select an algorithm in this resolver. |
| `plot` | `False` | When True, creates diagnostic spectrum/map panels; the FFCA panel is currently unpopulated. |
| `flag` | `None` | Optional label stored in the results and prefixed to the output CSV filename; None means no prefix. |

## Returns and side effects

Returns `(cbf, ffca)`: CBF is the frequency of maximum spatially averaged PSD, and FFCA is the fraction of pixels whose maximum PSD exceeds the threshold.

## Source

`hilllab/cilia/_resolve_CBF_FFCA.py`, lines 9–68 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/_resolve_CBF_FFCA.py#L9-L68)
