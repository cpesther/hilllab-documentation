# Popup.__init__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Popup.__init__(self, message, type='info', title=None)
:module: hilllab.utilities.gui.Popup
:canonical: hilllab.utilities.gui.Popup.Popup.__init__
```

## Behavior and usage

Sets `message`, normalized `type`, and `title`; returns `None`. A missing title becomes the capitalized type. Unknown types are accepted and later use the default blue color.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `message` | `required` | Text displayed in the popup body. |
| `type` | `'info'` | Case-insensitive info/warning/error severity; unknown values use the default color. |
| `title` | `None` | Optional window/body title; None uses capitalized severity. |

## Returns and side effects

Sets `message`, normalized `type`, and `title`; returns `None`.

## Source

`hilllab/utilities/gui/Popup.py`, lines 18–27 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Popup.py#L18-L27)
