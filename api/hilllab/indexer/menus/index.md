# hilllab.indexer.menus

Prototype terminal menu interfaces. The main menu's advertised actions are not implemented.

## Subfolders

| Group | Purpose |
| --- | --- |
| [menu_utilities](menu_utilities/index.md) | Terminal formatting, option prompting, and global menu shortcuts. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`menu_main`](menu_main.md) | Draws a console menu, prompts through ask_option, and returns None. | needs review |

## Terminal layout

The supplied terminal dimensions are 130 columns by 25 rows, with nominal header/footer heights of 2 and 3. Menu actions are prototypes; see the individual function flags.

```{toctree}
:hidden:
:maxdepth: 1

menu_utilities <menu_utilities/index>
menu_main <menu_main>
```
