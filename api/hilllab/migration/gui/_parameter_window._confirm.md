# _parameter_window._confirm

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} _parameter_window._confirm()
:module: hilllab.migration.gui._parameter_window
:canonical: hilllab.migration.gui._parameter_window._parameter_window._confirm
```

## Behavior and usage

Closure-local Tk callback reading the parent entry widgets, validating integer column/radius fields and float viscosity fields, filling the three parent dictionaries, and destroying the root on success. Returns None; it does not directly return the dictionaries. Error paths show popups except the missing-group-name branch.

## Inputs

No explicit input arguments.

## Returns and side effects

Returns None; it does not directly return the dictionaries.

## Related HillLab tools

Shared functions and classes used by this tool:

- {ref}`hilllab.utilities.gui.Popup.Popup <class-popup>`

## Source

`hilllab/migration/gui/_parameter_window.py`, lines 219–325 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/gui/_parameter_window.py#L219-L325)
