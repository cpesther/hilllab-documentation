# hilllab.migration.gui

Desktop Tk interfaces for assigning capillary groups, radii, and calibration viscosities.

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_parameter_window`](_parameter_window.md) | Blocks in a desktop Tk window and returns `(groups, radii_values, calibration_columns)`. | needs review |
| [`_parameter_window._confirm`](_parameter_window._confirm.md) | Closure-local Tk callback reading the parent entry widgets, validating integer column/radius fields and float viscosity fields, filling the three parent dictionaries, and destroying the root on success. | documented |
| [`_parameter_window_text`](_parameter_window_text.md) | Returns explanatory text for all/groups/radii/calibration mode. | documented |
```{toctree}
:hidden:
:maxdepth: 1

_parameter_window <_parameter_window>
_parameter_window._confirm <_parameter_window._confirm>
_parameter_window_text <_parameter_window_text>
```
