# open_in_explorer

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} open_in_explorer(path)
:module: hilllab.widgets.button_open_path
:canonical: hilllab.widgets.button_open_path.open_in_explorer
```

## Behavior and usage

Returns `None`; opens a Windows folder directly or a file's parent, uses macOS reveal-in-Finder, and on Linux opens `dirname(path)`. Consequently Linux directory inputs open their parent, not the directory itself. The path is not validated before invoking the platform tool.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Local file/directory to reveal/open using the kernel machine platform commands. |

## Returns and side effects

Returns `None`; opens a Windows folder directly or a file's parent, uses macOS reveal-in-Finder, and on Linux opens `dirname(path)`.

## Source

`hilllab/widgets/button_open_path.py`, lines 36–47 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/widgets/button_open_path.py#L36-L47)
