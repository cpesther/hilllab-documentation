# calculate_AFV

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The signal is padded to a power-of-two length, but frequency bins are calculated using the original length n and the padded spectrum is trimmed. Frequency values can therefore be miscalibrated for non-power-of-two lengths. No correction for missing frame intervals is applied.
:::

## Signature

```{py:function} calculate_AFV(instantaneous_data, fps)
:module: hilllab.dynamics.calculate_AFV
:canonical: hilllab.dynamics.calculate_AFV.calculate_AFV
```

## Behavior and usage

Returns a dictionary of three amplitude measures, peak-selected frequency, and up/down mean/median speeds from one bead's pca and speed columns. PCA extrema use prominence 1; FFT peaks use prominence 300. Missing extrema/frequency produce None, while empty speed subsets can produce NaN. fps must be positive and correspond to uniformly sampled rows.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `instantaneous_data` | `required` | **pandas.DataFrame**. a dataframe containing (at minimum) values for the PCA and speed of the particle at each frame as saved in the 'instantaneous' table produced by the primary analysis function. |
| `fps` | `required` | **int**. the sampling rate of the data in frames per second. |

## Returns and side effects

Returns a dictionary of three amplitude measures, peak-selected frequency, and up/down mean/median speeds from one bead's pca and speed columns.

## Source

`hilllab/dynamics/calculate_AFV.py`, lines 6–120 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/calculate_AFV.py#L6-L120)
