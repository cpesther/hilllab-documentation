# Tooltip.show_tooltip

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Calling it manually with the default `event=None` creates the window and then calls `move_tooltip(None)`, which accesses `event.x_root` and fails. Use a real event through the widget binding.
:::

## Signature

```{py:method} Tooltip.show_tooltip(self, event=None)
:module: hilllab.utilities.gui.Tooltip
:canonical: hilllab.utilities.gui.Tooltip.Tooltip.show_tooltip
```

## Behavior and usage

Returns `None`; creates a borderless topmost window unless a tooltip already exists or text is empty. The normal enter callback supplies a mouse event.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `event` | `None` | Event supplied by the GUI callback system; required attributes and any unused behavior are described in the usage notes. |

## Returns and side effects

Returns `None`; creates a borderless topmost window unless a tooltip already exists or text is empty.

## Source

`hilllab/utilities/gui/Tooltip.py`, lines 21–32 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Tooltip.py#L21-L32)
