# _subtract_linear_drift

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Trend-corrected x/y are assigned only for the selected interval, leaving out-of-window rows NaN. Final branching mistakenly checks the last DataFrame `clean_bead_data` rather than the list of bead tables, and no surviving beads leaves it undefined. The advertised 3D correction only modifies x/y.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _subtract_linear_drift(data, drift_start_time=None, drift_end_time=None)
:module: hilllab.ptmr.drift._subtract_linear_drift
:canonical: hilllab.ptmr.drift._subtract_linear_drift._subtract_linear_drift
```

## Behavior and usage

Fits independent linear trends for each bead's x/y over the requested absolute timestamp interval. Intended output is a concatenated tracking DataFrame, leaving z unchanged. Empty input returns directly. Both time bounds must be supplied despite default None values. Beads with two or fewer points in the interval are skipped.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `data` | `required` | **pandas.DataFrame**. the data from the VRPN. Must be run through the _format_vrpn function first. |
| `drift_start_time` | `None` | **float**. start time for computing drift (seconds).  Only frames at or after this time are included in the drift fit. |
| `drift_end_time` | `None` | **float**. snd time for computing drift (seconds).  Only frames at or before this time are included in the drift fit. |

## Returns and side effects

Empty input returns directly.

## Source

`hilllab/ptmr/drift/_subtract_linear_drift.py`, lines 5–100 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/drift/_subtract_linear_drift.py#L5-L100)
