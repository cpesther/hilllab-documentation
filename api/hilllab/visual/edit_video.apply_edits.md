# edit_video.apply_edits

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} edit_video.apply_edits(frame)
:module: hilllab.visual.edit_video
:canonical: hilllab.visual.edit_video.edit_video.apply_edits
```

## Behavior and usage

Closure-local transformation of a BGR uint8 frame; returns the edited frame using parent brightness, contrast, gamma table, saturation, and sharpness settings. Not separately importable; use `edit_video` for the public workflow.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `frame` | `required` | OpenCV BGR frame array; parent settings are applied and an edited frame is returned. |

## Returns and side effects

Closure-local transformation of a BGR uint8 frame; returns the edited frame using parent brightness, contrast, gamma table, saturation, and sharpness settings.

## Source

`hilllab/visual/edit_video.py`, lines 70–86 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/edit_video.py#L70-L86)
