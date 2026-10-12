# button_open_path

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} button_open_path(file_path, text=None, width=150, button_color='gray', text_color='white')
:module: hilllab.widgets.button_open_path
:canonical: hilllab.widgets.button_open_path.button_open_path
```

## Behavior and usage

Displays an ipywidgets Button wired to `open_in_explorer` and returns `None`, not the widget. `width` is in pixels; label defaults to the path. Requires an IPython notebook display environment, and clicking opens the file browser on the machine running the kernel.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `file_path` | `required` | **string**. Path to the file or folder to open. |
| `text` | `None` | Button label; None/empty uses Open: followed by the file path. |
| `width` | `150` | Button width in pixels. |
| `button_color` | `'gray'` | Ipywidgets button background color. |
| `text_color` | `'white'` | Requested text color in the widget style; rendering support depends on the widget frontend. |

## Returns and side effects

Displays an ipywidgets Button wired to `open_in_explorer` and returns `None`, not the widget.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.widgets.button_open_path.open_in_explorer`](open_in_explorer.md)

## Source

`hilllab/widgets/button_open_path.py`, lines 8–33 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/widgets/button_open_path.py#L8-L33)
