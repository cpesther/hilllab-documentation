# warn

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} warn(msg, category=UserWarning, stacklevel=2)
:module: hilllab.utilities.warning
:canonical: hilllab.utilities.warning.warn
```

## Behavior and usage

Installs the simplified global formatter, then emits a warning of `category` with `stacklevel`; returns `None` unless a warning filter turns it into an exception. This does not simply print a string and can be caught with Python warning controls.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `msg` | `required` | Warning message passed to warnings.warn. |
| `category` | `UserWarning` | Python Warning subclass, such as UserWarning. |
| `stacklevel` | `2` | Python warning stack level, normally 2 to attribute the warning to the caller. |

## Returns and side effects

Installs the simplified global formatter, then emits a warning of `category` with `stacklevel`; returns `None` unless a warning filter turns it into an exception.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.warning.enable_simple_warnings`](enable_simple_warnings.md)

## Source

`hilllab/utilities/warning.py`, lines 18–23 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/warning.py#L18-L23)
