# format_duration

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} format_duration(seconds)
:module: hilllab.utilities.format_duration
:canonical: hilllab.utilities.format_duration.format_duration
```

## Behavior and usage

Returns a space-separated duration with day/hour/minute/second components, or `0 s` for zero. Negative durations raise `ValueError`. Fractional seconds are truncated when converted to integer text.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `seconds` | `required` | Nonnegative duration in seconds; fractional displayed components are truncated. |

## Returns and side effects

Returns a space-separated duration with day/hour/minute/second components, or `0 s` for zero.

## Source

`hilllab/utilities/format_duration.py`, lines 2–25 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/format_duration.py#L2-L25)
