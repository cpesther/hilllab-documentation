# _get_pole_tip.click_event

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} _get_pole_tip.click_event(event, x, y, flags, params)
:module: hilllab.magnets._get_pole_tip
:canonical: hilllab.magnets._get_pole_tip._get_pole_tip.click_event
```

## Behavior and usage

Closure-local OpenCV mouse callback returning None and updating the parent pole_tip list only for a left-button-down event. x/y are image coordinates; flags and params are accepted but unused.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `event` | `required` | OpenCV mouse-event integer; only EVENT_LBUTTONDOWN updates the selection. |
| `x` | `required` | Horizontal click coordinate in image pixels. |
| `y` | `required` | Vertical click coordinate in image pixels. |
| `flags` | `required` | OpenCV modifier/button flags; accepted but unused. |
| `params` | `required` | OpenCV user-data callback parameter; accepted but unused. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/magnets/_get_pole_tip.py`, lines 11–18 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/_get_pole_tip.py#L11-L18)
