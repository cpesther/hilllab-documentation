# Tooltip.move_tooltip

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Tooltip.move_tooltip(self, event)
:module: hilllab.utilities.gui.Tooltip
:canonical: hilllab.utilities.gui.Tooltip.Tooltip.move_tooltip
```

## Behavior and usage

Moves an existing tooltip to 10 pixels right/below the mouse event's screen coordinates and returns `None`. `event` must provide `x_root` and `y_root`. It has no effect if no tooltip exists.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `event` | `required` | Event supplied by the GUI callback system; required attributes and any unused behavior are described in the usage notes. |

## Returns and side effects

Moves an existing tooltip to 10 pixels right/below the mouse event's screen coordinates and returns `None`.

## Source

`hilllab/utilities/gui/Tooltip.py`, lines 35–39 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Tooltip.py#L35-L39)
