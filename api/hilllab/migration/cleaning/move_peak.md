# move_peak

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The docstring says the first index, but the target is index 1 (the second sample), and wrapping is not zero padding. Confirm that circularly reused tail values are appropriate for the assay.
:::

## Signature

```{py:function} move_peak(data, peak_index)
:module: hilllab.migration.cleaning.peak
:canonical: hilllab.migration.cleaning.peak.move_peak
```

## Behavior and usage

Returns an array repositioning candidate peaks 0–4 toward index 1. Peak 0 inserts the second value at the beginning and drops the last; larger shifts wrap tail data to preserve length. Peaks ≥5 are left unchanged.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **list**. the array of unshifted data |
| `peak_index` | `required` | **int**. the amount that the data should be shifted as given by the profile number |

## Returns and side effects

Returns an array repositioning candidate peaks 0–4 toward index 1.

## Source

`hilllab/migration/cleaning/peak.py`, lines 4–53 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/cleaning/peak.py#L4-L53)
