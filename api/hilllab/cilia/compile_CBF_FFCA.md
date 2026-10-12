# compile_CBF_FFCA

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} compile_CBF_FFCA(folder, compile_all=True)
:module: hilllab.cilia.compile_CBF_FFCA
:canonical: hilllab.cilia.compile_CBF_FFCA.compile_CBF_FFCA
```

## Behavior and usage

Writes compiled CSV data at the root (`compile_all=True`) or in each discovered CSV-containing subfolder; returns `None`. Only filenames containing `_CBF_FFCA` are included, with cbf/ffca/method/flag plus filename-derived file labels. Subfolder traversal is recursive, so a parent compilation can include descendants. There is no empty-input guard.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder` | `required` | **string**. the path to the folder containing CBF/FFCA CSV files. |
| `compile_all` | `True` | True writes one root compilation; False compiles each discovered CSV-containing folder recursively. |

## Returns and side effects

Writes compiled CSV data at the root (`compile_all=True`) or in each discovered CSV-containing subfolder; returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../utilities/walk_dir.md)

## Source

`hilllab/cilia/compile_CBF_FFCA.py`, lines 10–75 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/compile_CBF_FFCA.py#L10-L75)
