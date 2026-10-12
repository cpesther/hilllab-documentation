# hilllab.widgets

Notebook buttons for opening paths in the kernel machine's native file browser.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`button_open_path`](button_open_path.md) | Displays an ipywidgets Button wired to `open_in_explorer` and returns `None`, not the widget. | documentation in progress |
| [`open_in_explorer`](open_in_explorer.md) | Returns `None`; opens a Windows folder directly or a file's parent, uses macOS reveal-in-Finder, and on Linux opens `dirname(path)`. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

button_open_path <button_open_path>
open_in_explorer <open_in_explorer>
```
