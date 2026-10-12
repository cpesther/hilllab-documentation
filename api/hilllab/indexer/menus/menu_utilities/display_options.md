# display_options

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} display_options(options)
:module: hilllab.indexer.menus.menu_utilities.display_options
:canonical: hilllab.indexer.menus.menu_utilities.display_options.display_options
```

## Behavior and usage

Prints title-cased options numbered from 1 and returns `(n_lines, options_dict)` mapping integer numbers to original option strings. It does not prompt or execute a selection.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `options` | `required` | Sequence of option strings; display numbers begin at 1. |

## Returns and side effects

Prints title-cased options numbered from 1 and returns `(n_lines, options_dict)` mapping integer numbers to original option strings.

## Source

`hilllab/indexer/menus/menu_utilities/display_options.py`, lines 3–14 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_utilities/display_options.py#L3-L14)
