# _plate_remove_overflows

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Scientific-notation strings such as 1e-3 and NaN/inf strings contain letters and can be treated as overflows. The replacement search can cross a read boundary, and the function does not explicitly convert the whole result table to numeric types.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _plate_remove_overflows(input_data)
:module: hilllab.migration._plate_remove_overflows
:canonical: hilllab.migration._plate_remove_overflows._plate_remove_overflows
```

## Behavior and usage

Returns `(no_overflow_data, overflow_meta)`, replacing values whose string contains any alphabetic character with the first following nonalphabetic token within ten rows, or zero. Metadata records column/read/row/old/replacement values. It is not limited to the literal Overflow marker.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `input_data` | `required` | **pandas.DataFrame**. the dataframe containing the  raw data that may contain overflows. |

## Returns and side effects

Returns `(no_overflow_data, overflow_meta)`, replacing values whose string contains any alphabetic character with the first following nonalphabetic token within ten rows, or zero.

## Source

`hilllab/migration/_plate_remove_overflows.py`, lines 5–72 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/_plate_remove_overflows.py#L5-L72)
