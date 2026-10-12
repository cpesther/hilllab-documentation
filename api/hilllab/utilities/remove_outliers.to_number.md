# remove_outliers.to_number

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} remove_outliers.to_number(x)
:module: hilllab.utilities.remove_outliers
:canonical: hilllab.utilities.remove_outliers.remove_outliers.to_number
```

## Behavior and usage

A closure-local parser taking one token and returning its float conversion or `None` on ValueError/TypeError. Used only inside pasted-input mode and not importable independently.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `x` | `required` | One pasted token converted to float, or None on conversion failure. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/utilities/remove_outliers.py`, lines 53–57 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/remove_outliers.py#L53-L57)
