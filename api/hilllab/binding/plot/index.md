# hilllab.binding.plot

Plots and shared table handling for bead binding results.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`contour_hist`](contour_hist.md) | Displays/optionally saves contour-area histograms and returns `None`. | documented |
| [`counts_bar`](counts_bar.md) | Creates a grouped expected-bead-count plot and returns `None`. | needs review |
| [`percentage_bar`](percentage_bar.md) | Displays percent bound, runoff, or both, selected case-insensitively through `slide`, and returns `None`. | needs review |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_binding_results_handler`](_binding_results_handler.md) | Returns `(results, pivoted, file, parent, save_path)`. | needs review |
```{toctree}
:hidden:
:maxdepth: 1

_binding_results_handler <_binding_results_handler>
contour_hist <contour_hist>
counts_bar <counts_bar>
percentage_bar <percentage_bar>
```
