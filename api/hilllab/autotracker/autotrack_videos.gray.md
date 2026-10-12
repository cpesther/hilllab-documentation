# autotrack_videos.gray

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} autotrack_videos.gray(image)
:module: hilllab.autotracker.autotrack_videos
:canonical: hilllab.autotracker.autotrack_videos.autotrack_videos.gray
```

## Behavior and usage

A nested PIMS pipeline callback taking an H×W×C image and returning `image[:, :, 1]`, the green channel. It is defined inside the tracking call and cannot be imported as a standalone helper. A single-channel frame does not meet the indexing requirement.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `image` | `required` | Decoded multichannel image array with a channel axis; the callback selects channel index 1. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/autotracker/autotrack_videos.py`, lines 149–150 · Local working-tree version; differs from the recorded repository revision.
