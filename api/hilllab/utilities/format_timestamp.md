# format_timestamp

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} format_timestamp(timestamp)
:module: hilllab.utilities.format_timestamp
:canonical: hilllab.utilities.format_timestamp.format_timestamp
```

## Behavior and usage

Accepts a Unix timestamp in seconds and returns `(date_string, time_string)` using local system time, formatted `MM/DD/YYYY` and `HH:MM:SS`. It does not return a datetime object or include timezone information.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `timestamp` | `required` | Unix timestamp seconds, converted in the local system timezone. |

## Returns and side effects

Accepts a Unix timestamp in seconds and returns `(date_string, time_string)` using local system time, formatted `MM/DD/YYYY` and `HH:MM:SS`. It does not return a datetime object or include timezone information.

## Source

`hilllab/utilities/format_timestamp.py`, lines 4–8 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/format_timestamp.py#L4-L8)
