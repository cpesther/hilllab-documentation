# compile_CBF_FFCA._compile_files

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} compile_CBF_FFCA._compile_files(all_csvs, output_folder)
:module: hilllab.cilia.compile_CBF_FFCA
:canonical: hilllab.cilia.compile_CBF_FFCA.compile_CBF_FFCA._compile_files
```

## Behavior and usage

Closure-local helper accepting CSV paths and an output folder, returning the saved CSV path string. It concatenates matching result tables and writes `<output-folder-stem>.csv`. With no matching result tables, pandas concat raises rather than creating an empty workbook.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `all_csvs` | `required` | Sequence of CSV paths; only names containing _CBF_FFCA are included. |
| `output_folder` | `required` | Existing destination directory; its stem becomes the compiled CSV basename. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)

## Source

`hilllab/cilia/compile_CBF_FFCA.py`, lines 21–51 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/compile_CBF_FFCA.py#L21-L51)
