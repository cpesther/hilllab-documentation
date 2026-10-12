# enable_simple_warnings

[Folder overview](index.md)

## Signature

```{py:function} enable_simple_warnings()
:module: hilllab.utilities.warning
:canonical: hilllab.utilities.warning.enable_simple_warnings
```

## Behavior and usage

Sets Python's global warning formatter and returns `None`. Subsequent warnings throughout the process use the simplified formatting, including warnings from other libraries.

## Inputs

No explicit input arguments.

## Returns and side effects

Sets Python's global warning formatter and returns `None`.

## Source

`hilllab/utilities/warning.py`, lines 5–15 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/warning.py#L5-L15)
