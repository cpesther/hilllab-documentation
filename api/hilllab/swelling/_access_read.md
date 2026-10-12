# _access_read

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _access_read(read_number, channel_table)
:module: hilllab.swelling._access_read
:canonical: hilllab.swelling._access_read._access_read
```

## Behavior and usage

Returns the 16-row slice starting at `int(read_number*16)` from a channel table. Read numbering is zero-based; read 0 is rows 0–15. Index labels are preserved and no check verifies a complete block. Supply nonnegative integer read indices.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `read_number` | `required` | Zero-based read-block index; each read spans 16 table rows. |
| `channel_table` | `required` | Channel DataFrame stacked in 16-row read blocks. |

## Returns and side effects

Returns the 16-row slice starting at `int(read_number*16)` from a channel table.

## Source

`hilllab/swelling/_access_read.py`, lines 3–15 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/swelling/_access_read.py#L3-L15)
