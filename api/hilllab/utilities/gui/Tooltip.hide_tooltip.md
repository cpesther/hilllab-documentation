# Tooltip.hide_tooltip

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Tooltip.hide_tooltip(self, event=None)
:module: hilllab.utilities.gui.Tooltip
:canonical: hilllab.utilities.gui.Tooltip.Tooltip.hide_tooltip
```

## Behavior and usage

Destroys the current floating window, clears the stored handle, and returns `None`. `event` is accepted for callback compatibility and unused.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `event` | `None` | Event supplied by the GUI callback system; required attributes and any unused behavior are described in the usage notes. |

## Returns and side effects

Destroys the current floating window, clears the stored handle, and returns `None`.

## Source

`hilllab/utilities/gui/Tooltip.py`, lines 42–45 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Tooltip.py#L42-L45)
