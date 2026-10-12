# remove_outliers

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
See the exact filtering and return expression in the implementation evidence below; empty input and zero MAD are not separately guarded.
:::

## Signature

```{py:function} remove_outliers(array=[], info=True, paste_mode=True, delimiter=None)
:module: hilllab.utilities.remove_outliers
:canonical: hilllab.utilities.remove_outliers.remove_outliers
```

## Behavior and usage

Uses the median absolute deviation scaled by `1/(sqrt(2)*erfcinv(0.5))` and keeps values within three scaled MADs. Default `paste_mode=True` prompts for values and ignores the supplied array; use `paste_mode=False` for programmatic arrays. Non-numeric pasted tokens are discarded. Returns `(filtered_array, removed_values, removed_indices)` as lists. Paste mode also replaces removed values with blank/NaN cells and copies the result to the system clipboard; programmatic mode avoids that side effect.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `array` | `[]` | **list**. Array of data containing outliers |
| `info` | `True` | **bool**. Whether a print message should be displayed with information about the removed outliers. |
| `paste_mode` | `True` | **bool**. controls whether the function is run in a mode where data can be pasted directly from Excel. |
| `delimiter` | `None` | **string**. the value used for separating the data pasted  when paste_mode is set to True. This is only used if the function cannot regonize the delimiter automatically. |

## Returns and side effects

Returns `(filtered_array, removed_values, removed_indices)` as lists.

## Source

`hilllab/utilities/remove_outliers.py`, lines 7–112 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/remove_outliers.py#L7-L112)
