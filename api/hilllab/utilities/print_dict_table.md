# print_dict_table

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} print_dict_table(dict, title, gap=4, line='-')
:module: hilllab.utilities.print_dict_table
:canonical: hilllab.utilities.print_dict_table.print_dict_table
```

## Behavior and usage

Prints a width-aligned console table from mapping keys/values and returns `None`. `title` labels the header, `gap` sets spacing, and `line` is the border character. `dict` must be nonempty: an empty mapping reaches `max([])` and raises `ValueError`.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `dict` | `required` | Nonempty mapping of display keys to values, converted to strings. |
| `title` | `required` | Text shown as a heading or title. |
| `gap` | `4` | Number of spacing characters between printed key and value columns. |
| `line` | `'-'` | Character/string repeated to form the console-table border. |

## Returns and side effects

Prints a width-aligned console table from mapping keys/values and returns `None`.

## Source

`hilllab/utilities/print_dict_table.py`, lines 3–46 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/print_dict_table.py#L3-L46)
