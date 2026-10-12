# _parameter_window_text

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _parameter_window_text(parameters='all')
:module: hilllab.migration.gui._parameter_window_text
:canonical: hilllab.migration.gui._parameter_window_text._parameter_window_text
```

## Behavior and usage

Returns explanatory text for all/groups/radii/calibration mode. Unknown values raise ValueError. The text describes GUI inputs and units; it does not apply settings to a Bundle.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `parameters` | `'all'` | **string**. the parameters values passed to the  _parameter_window function, which controls which version of the instructions text is returned. |

## Returns and side effects

Returns explanatory text for all/groups/radii/calibration mode.

## Source

`hilllab/migration/gui/_parameter_window_text.py`, lines 3–38 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/gui/_parameter_window_text.py#L3-L38)
