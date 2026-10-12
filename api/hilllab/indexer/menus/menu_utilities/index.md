# hilllab.indexer.menus.menu_utilities

Terminal formatting, option prompting, and global menu shortcuts.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`ask_option`](ask_option.md) | Reads console input and returns its uppercase string for ordinary options. | documented |
| [`clear_terminal`](clear_terminal.md) | Runs Windows cls or another system's clear shell command and returns None. | documentation in progress |
| [`display_footer`](display_footer.md) | Prints a blank line, width copies of line_spacer, and global command hints; returns None. width is a character count, not pixels. | documentation in progress |
| [`display_header`](display_header.md) | Clears the terminal and prints an uppercased title centered in a line of the requested character width, followed by selection instructions; returns None. | documentation in progress |
| [`display_options`](display_options.md) | Prints title-cased options numbered from 1 and returns `(n_lines, options_dict)` mapping integer numbers to original option strings. | documentation in progress |
| [`fill_vertical_space`](fill_vertical_space.md) | Uses configured HEIGHT minus occupied/header/footer counts to print filler lines and returns None. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

ask_option <ask_option>
clear_terminal <clear_terminal>
display_footer <display_footer>
display_header <display_header>
display_options <display_options>
fill_vertical_space <fill_vertical_space>
```
