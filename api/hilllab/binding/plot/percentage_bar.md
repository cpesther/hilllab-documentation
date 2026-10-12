# percentage_bar

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The explicit save_path argument is ignored. Saving with a DataFrame cannot infer an output location; duplicate/missing well pairs or zero totals are also unsupported.
:::

## Signature

```{py:function} percentage_bar(results, slide, save=False, save_path=None)
:module: hilllab.binding.plot.percentage_bar
:canonical: hilllab.binding.plot.percentage_bar.percentage_bar
```

## Behavior and usage

Displays percent bound, runoff, or both, selected case-insensitively through `slide`, and returns `None`. Calculations use n_expected divided by paired total. BOTH adds a percentage column to the provided results table in place.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `results` | `required` | **string or pandas.DataFrame**. either a string as the path to a pre-exported binding results Excel file or the loaded DataFrame containing those results. |
| `slide` | `required` | **string**. one of 'bound', 'runoff', or 'both'. Contols which percentages are plotted on the graph. |
| `save` | `False` | **bool**. whether the figure produced should be saved as a PNG |
| `save_path` | `None` | **bool**. allows for a specific save path to be provided,  otherwise the image will be saved to a plots folder in the same directory as the results file. If the results were loaded directly from a dataframe, then this argument will be required in order to save the plot as an image. |

## Returns and side effects

Displays percent bound, runoff, or both, selected case-insensitively through `slide`, and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.binding.plot._binding_results_handler._binding_results_handler`](_binding_results_handler.md)
- [`hilllab.utilities.custom_axes.custom_axes`](../../utilities/custom_axes.md)

## Source

`hilllab/binding/plot/percentage_bar.py`, lines 8–90 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/binding/plot/percentage_bar.py#L8-L90)
