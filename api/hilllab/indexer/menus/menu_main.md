# menu_main

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
All option branches are pass statements; no action is implemented. menu_utilities/__init__.py also uses bare imports rather than package-relative imports, which can fail in a normal package environment.
:::

## Signature

```{py:function} menu_main()
:module: hilllab.indexer.menus.menu_main
:canonical: hilllab.indexer.menus.menu_main.menu_main
```

## Behavior and usage

Draws a console menu, prompts through ask_option, and returns None. The listed recording/browsing/searching actions are menu labels only.

## Inputs

No explicit input arguments.

## Returns and side effects

Draws a console menu, prompts through ask_option, and returns None.

## Source

`hilllab/indexer/menus/menu_main.py`, lines 5–41 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/menus/menu_main.py#L5-L41)
