# count_beads

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The histogram destination `plots/contour_hist` is not created before saving, and the final counts_bar call passes a DataFrame with save=True to a helper that cannot infer a destination. The caller's supplied save_path is ignored by counts_bar. The current full workflow can fail before its intended return.
:::

## Signature

```{py:function} count_beads(folder, bead_type, radius_um, bead_area_range=(3, 40))
:module: hilllab.binding.count_beads
:canonical: hilllab.binding.count_beads.count_beads
```

## Behavior and usage

Requires bound/runoff subfolders, detects contours after circular masking, Gaussian blur, and Otsu thresholding, and classifies contour area into small/expected/large. Areas are pixel²; `radius_um` is recorded metadata and only checked heuristically, not used to calibrate detection. Intended return is a per-image counts DataFrame; output side effects include annotated PNGs, contour histograms, a counts Excel workbook, and a count bar plot. Match image stems between bound and runoff so pivoting pairs wells correctly.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder` | `required` | **string**. the path to the folder which contains a  'runoff' and 'bound' subfolder. |
| `bead_type` | `required` | **string**. the type of bead used in the experiment.  Suggested values are 'COOH', 'Amine', 'PEG', or 'Other'. This value is only stored in the Excel file and does not affect processing. |
| `radius_um` | `required` | **float**. the radius of the bead used in micrometers (µm).  This value is only stored in the Excel file and does not affect processing. |
| `bead_area_range` | `(3, 40)` | **tuple**. the range of areas in pixels² of pixels that will be counted. The first number is the minimum area and the second area is the maximum area. |

## Returns and side effects

Intended return is a per-image counts DataFrame; output side effects include annotated PNGs, contour histograms, a counts Excel workbook, and a count bar plot.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.binding.masks.circular.circular`](masks/circular.md)
- [`hilllab.binding.plot._binding_results_handler._binding_results_handler`](plot/_binding_results_handler.md)
- [`hilllab.binding.plot.contour_hist.contour_hist`](plot/contour_hist.md)
- [`hilllab.binding.plot.counts_bar.counts_bar`](plot/counts_bar.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)
- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/binding/count_beads.py`, lines 16–208 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/binding/count_beads.py#L16-L208)
