# counts_bar

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The save_path parameter is never forwarded to `_binding_results_handler`; saving a DataFrame therefore raises instead of using the requested path. Seaborn's edgecolor/linewidth aggregation is a plot of input rows rather than a verified pairing algorithm.
:::

## Signature

```{py:function} counts_bar(results, save=False, save_path=None)
:module: hilllab.binding.plot.counts_bar
:canonical: hilllab.binding.plot.counts_bar.counts_bar
```

## Behavior and usage

Creates a grouped expected-bead-count plot and returns `None`. Accepts a results table or Excel path; saving from an Excel string infers a sibling plots folder. It uses Seaborn, which is not declared in pyproject dependencies.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `results` | `required` | **string or pandas.DataFrame**. either a string as the path to a pre-exported binding results Excel file or the loaded DataFrame containing those results. |
| `save` | `False` | **bool**. whether the figure produced should be saved as a PNG |
| `save_path` | `None` | **bool**. allows for a specific save path to be provided,  otherwise the image will be saved to a plots folder in the same directory as the results file. If the results were loaded directly from a dataframe, then this argument will be required in order to save the plot as an image. |

## Returns and side effects

Creates a grouped expected-bead-count plot and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.binding.plot._binding_results_handler._binding_results_handler`](_binding_results_handler.md)
- [`hilllab.utilities.custom_axes.custom_axes`](../../utilities/custom_axes.md)

## Source

`hilllab/binding/plot/counts_bar.py`, lines 8–45 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/binding/plot/counts_bar.py#L8-L45)
