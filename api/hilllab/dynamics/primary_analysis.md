# primary_analysis

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
PCA is calculated from unscaled input XY while most motion statistics use pixel_width-scaled coordinates, so the stored PCA/amplitudes remain in pixels despite plot metadata advertising micrometers. Power-of-two FFT padding uses frequency bins for the original signal length. Missing frames are compressed while derivatives assume constant dt. Short/degenerate tracks can fail extrema, PCA, or Savitzky–Golay filtering; minimum window length is 5.
:::

## Signature

```{py:function} primary_analysis(path, fps, pixel_width)
:module: hilllab.dynamics.primary_analysis
:canonical: hilllab.dynamics.primary_analysis.primary_analysis
```

## Behavior and usage

Returns `(summary, instantaneous, metadata)` from one VRPN file, or `(None, None, None)` for an empty tracking array. fps converts frames to seconds; pixel_width scales XY into the requested physical units. Calculates lifetime, path/displacement, headings/turning, velocity/acceleration, shape, PCA alignment, detrended amplitudes, and frequency. Each bead receives a new random UUID plus a rounded-feature hash. HDF persistence is performed by batch wrappers, not here.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the path to the VRPN file |
| `fps` | `required` | **int**. the frame rate of the video |
| `pixel_width` | `required` | **float**. the width of the pixel in micrometers |

## Returns and side effects

Returns `(summary, instantaneous, metadata)` from one VRPN file, or `(None, None, None)` for an empty tracking array. fps converts frames to seconds; pixel_width scales XY into the requested physical units.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.load_vrpn.load_vrpn`](../utilities/load_vrpn.md)

## Source

`hilllab/dynamics/primary_analysis.py`, lines 13–486 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/primary_analysis.py#L13-L486)
