# display_footer

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} display_footer(width, line_spacer='—')
:module: hilllab.indexer.menus.menu_utilities.display_footer
:canonical: hilllab.indexer.menus.menu_utilities.display_footer.display_footer
```

## Behavior and usage

Prints a blank line, width copies of line_spacer, and global command hints; returns None. width is a character count, not pixels.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `width` | `required` | Requested width; see the usage notes for whether its units are characters or pixels. |
| `line_spacer` | `'—'` | Character or string repeated to draw the terminal border. |

## Returns and side effects

Prints a blank line, width copies of line_spacer, and global command hints; returns None. width is a character count, not pixels.

## Source

`hilllab/indexer/menus/menu_utilities/display_footer.py`, lines 3–10 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_utilities/display_footer.py#L3-L10)
