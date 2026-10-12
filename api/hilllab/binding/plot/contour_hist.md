# contour_hist

[Folder overview](index.md)

## Signature

```{py:function} contour_hist(counts, file=None, save_path=None)
:module: hilllab.binding.plot.contour_hist
:canonical: hilllab.binding.plot.contour_hist.contour_hist
```

## Behavior and usage

Displays/optionally saves contour-area histograms and returns `None`. `counts` must contain small, expected, and large lists. Bins are based on areas below 1000 and the display x-range is 0–110 pixel². All-empty or all-large collections fail min/max. The save directory must already exist.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `counts` | `required` | **dict**. the dictionary of bead counts |
| `file` | `None` | **string**. the path to the file from which these bead counts originate |
| `save_path` | `None` | **string**. when provided, this path is where a PNG copy of the created figure will be saved. |

## Returns and side effects

Displays/optionally saves contour-area histograms and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.custom_axes.custom_axes`](../../utilities/custom_axes.md)

## Source

`hilllab/binding/plot/contour_hist.py`, lines 7–58 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/binding/plot/contour_hist.py#L7-L58)
