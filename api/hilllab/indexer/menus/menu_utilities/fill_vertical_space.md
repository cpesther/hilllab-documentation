# fill_vertical_space

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} fill_vertical_space(lines_occupied, count_header=True, count_footer=True)
:module: hilllab.indexer.menus.menu_utilities.fill_vertical_space
:canonical: hilllab.indexer.menus.menu_utilities.fill_vertical_space.fill_vertical_space
```

## Behavior and usage

Uses configured HEIGHT minus occupied/header/footer counts to print filler lines and returns None. It also prints a debugging `fill vertical` line, and each loop prints a string containing a newline, so the nominal fill count is not an exact terminal-row count.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `lines_occupied` | `required` | Nominal count of already-used terminal rows. |
| `count_header` | `True` | Include configured HEADER_HEIGHT in the occupied count. |
| `count_footer` | `True` | Include configured FOOTER_HEIGHT in the occupied count. |

## Returns and side effects

Uses configured HEIGHT minus occupied/header/footer counts to print filler lines and returns None.

## Source

`hilllab/indexer/menus/menu_utilities/fill_vertical_space.py`, lines 4–21 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_utilities/fill_vertical_space.py#L4-L21)
