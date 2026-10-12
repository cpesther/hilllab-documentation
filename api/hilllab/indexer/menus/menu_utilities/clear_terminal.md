# clear_terminal

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} clear_terminal()
:module: hilllab.indexer.menus.menu_utilities.clear_terminal
:canonical: hilllab.indexer.menus.menu_utilities.clear_terminal.clear_terminal
```

## Behavior and usage

Runs Windows cls or another system's clear shell command and returns None. It operates on the active terminal, not notebook display output. Shell command availability and return codes are not checked.

## Inputs

No explicit input arguments.

## Returns and side effects

Runs Windows cls or another system's clear shell command and returns None. Shell command availability and return codes are not checked.

## Source

`hilllab/indexer/menus/menu_utilities/clear_terminal.py`, lines 5–7 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_utilities/clear_terminal.py#L5-L7)
