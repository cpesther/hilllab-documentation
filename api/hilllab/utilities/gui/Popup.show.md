# Popup.show

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Popup.show(self)
:module: hilllab.utilities.gui.Popup
:canonical: hilllab.utilities.gui.Popup.Popup.show
```

## Behavior and usage

Creates a nonmodal Tk Toplevel containing severity, title, message, and an OK button. Returns `None`, with no window handle. A Tk root/event loop is needed; the button destroys only the popup.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Returns `None`, with no window handle.

## Source

`hilllab/utilities/gui/Popup.py`, lines 30–56 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Popup.py#L30-L56)
