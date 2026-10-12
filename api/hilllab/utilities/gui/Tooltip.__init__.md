# Tooltip.__init__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Tooltip.__init__(self, widget, text)
:module: hilllab.utilities.gui.Tooltip
:canonical: hilllab.utilities.gui.Tooltip.Tooltip.__init__
```

## Behavior and usage

Accepts a Tk `widget` and tooltip `text`, stores state, and registers event callbacks; returns `None`. Keep a reference to the instance if you need to manage its state explicitly.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `widget` | `required` | Tk widget whose enter/leave/motion bindings will be set. |
| `text` | `required` | Tooltip text; empty text disables window creation. |

## Returns and side effects

Accepts a Tk `widget` and tooltip `text`, stores state, and registers event callbacks; returns `None`.

## Source

`hilllab/utilities/gui/Tooltip.py`, lines 11–18 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Tooltip.py#L11-L18)
