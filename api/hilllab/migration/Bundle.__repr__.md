# Bundle.__repr__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Bundle.__repr__(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Bundle.__repr__
```

## Behavior and usage

Returns a multiline string containing the source path and presence flags from contents(); does not itself print. Python uses it in repr(bundle) and some notebook displays.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Returns a multiline string containing the source path and presence flags from contents(); does not itself print.

## Source

`hilllab/migration/Bundle.py`, lines 100–115 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L100-L115)
