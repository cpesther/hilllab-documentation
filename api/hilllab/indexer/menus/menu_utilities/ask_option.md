# ask_option

[Folder overview](index.md)

## Signature

```{py:function} ask_option()
:module: hilllab.indexer.menus.menu_utilities.ask_option
:canonical: hilllab.indexer.menus.menu_utilities.ask_option.ask_option
```

## Behavior and usage

Reads console input and returns its uppercase string for ordinary options. MM recursively invokes the main menu then returns None; 00 exits the process via SystemExit(0). It does not validate whether an ordinary option exists.

## Inputs

No explicit input arguments.

## Returns and side effects

Reads console input and returns its uppercase string for ordinary options. MM recursively invokes the main menu then returns None; 00 exits the process via SystemExit(0).

## Source

`hilllab/indexer/menus/menu_utilities/ask_option.py`, lines 5–22 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_utilities/ask_option.py#L5-L22)
