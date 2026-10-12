# _binding_results_handler

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The explicit save_path is treated as a save folder, not a complete filename, and must be a Path-like object supporting mkdir. Zero totals produce undefined percentages. Missing/duplicate well-slide pairs prevent pivoting.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _binding_results_handler(results, save=False, save_path=None, save_name=None)
:module: hilllab.binding.plot._binding_results_handler
:canonical: hilllab.binding.plot._binding_results_handler._binding_results_handler
```

## Behavior and usage

Returns `(results, pivoted, file, parent, save_path)`. Inputs must include file, slide, and n_expected; slide values must include bound/runoff, with exactly one row per file/slide for pivoting. It calculates percentages from expected counts and forms plot paths when saving. Only exact string inputs trigger Excel loading; a Path object is treated as a table.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `results` | `required` | **string or pandas.DataFrame**. either the path to the binding  results file or the results dataframe itself. |
| `save` | `False` | **bool**. controls whether a specific save folder path for this file is generated. |
| `save_path` | `None` | **string**. a specific path that will be used to save any resultant file from this file's processing. Providing a value for this argument bypasses automatic save folder path generation. |
| `save_name` | `None` | **string**. used for generating the specific path for  saving any resultant files. Mostly used for plotting functions. |

## Returns and side effects

Returns `(results, pivoted, file, parent, save_path)`.

## Source

`hilllab/binding/plot/_binding_results_handler.py`, lines 5–85 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/binding/plot/_binding_results_handler.py#L5-L85)
