# display_header

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} display_header(title, width, line_spacer='—')
:module: hilllab.indexer.menus.menu_utilities.display_header
:canonical: hilllab.indexer.menus.menu_utilities.display_header.display_header
```

## Behavior and usage

Clears the terminal and prints an uppercased title centered in a line of the requested character width, followed by selection instructions; returns None. Titles wider than width are not truncated.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `title` | `required` | Text shown as a heading or title. |
| `width` | `required` | Requested width; see the usage notes for whether its units are characters or pixels. |
| `line_spacer` | `'—'` | Character or string repeated to draw the terminal border. |

## Returns and side effects

Clears the terminal and prints an uppercased title centered in a line of the requested character width, followed by selection instructions; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.indexer.menus.menu_utilities.clear_terminal.clear_terminal`](clear_terminal.md)

## Source

`hilllab/indexer/menus/menu_utilities/display_header.py`, lines 4–19 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_utilities/display_header.py#L4-L19)
