# _get_pole_tip

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _get_pole_tip(image)
:module: hilllab.magnets._get_pole_tip
:canonical: hilllab.magnets._get_pole_tip._get_pole_tip
```

## Behavior and usage

Shows an OpenCV image window, records the most recent left click, and returns `(x, y)` image coordinates or None if nothing is selected. Requires a desktop GUI and blocks on waitKey(0); a keypress also proceeds. It destroys all OpenCV windows on completion.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `image` | `required` | Image array to display for manual pole-tip selection, usually an OpenCV frame. |

## Returns and side effects

Shows an OpenCV image window, records the most recent left click, and returns `(x, y)` image coordinates or None if nothing is selected.

## Source

`hilllab/magnets/_get_pole_tip.py`, lines 4–38 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/_get_pole_tip.py#L4-L38)
