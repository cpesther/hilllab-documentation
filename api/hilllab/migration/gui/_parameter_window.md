# _parameter_window

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Inputs are not bounded against the actual plate or checked for duplicates/overlap; later assignments overwrite earlier ones. Missing group names instantiate a Popup without calling show(), so no visible error appears. A failed confirmation can leave partially populated dictionaries.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _parameter_window(parameters='all')
:module: hilllab.migration.gui._parameter_window
:canonical: hilllab.migration.gui._parameter_window._parameter_window
```

## Behavior and usage

Blocks in a desktop Tk window and returns `(groups, radii_values, calibration_columns)`. Up to 15 rows accept inclusive column ranges and/or comma-separated numbers. Groups map names to column lists, radii map `Column N` to integer nm, and calibration maps integer column numbers to float mPa·s. Unselected dictionaries remain empty. Closing the window returns current state rather than a separate cancellation flag.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `parameters` | `'all'` | **string**. controls which fields are shown in the selction window, allowing this function to be used for inputting either groups, radii, or eta calibration values, or all three at once. One of 'all', 'groups', 'radii', or 'calibration'. |

## Returns and side effects

Blocks in a desktop Tk window and returns `(groups, radii_values, calibration_columns)`. Closing the window returns current state rather than a separate cancellation flag.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration.gui._parameter_window_text._parameter_window_text`](_parameter_window_text.md)
- {ref}`hilllab.utilities.gui.Popup.Popup <class-popup>`
- {ref}`hilllab.utilities.gui.Tooltip.Tooltip <class-tooltip>`
- [`hilllab.utilities.warning.warn`](../../utilities/warn.md)

## Source

`hilllab/migration/gui/_parameter_window.py`, lines 10–334 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/gui/_parameter_window.py#L10-L334)
