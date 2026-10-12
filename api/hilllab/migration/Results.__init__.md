# Results.__init__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Results.__init__(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Results.__init__
```

## Behavior and usage

Creates empty pandas result tables and an empty radii_nm_calib mapping; returns None. Row/column alignment is supplied by the calculation functions, not the constructor.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Creates empty pandas result tables and an empty radii_nm_calib mapping; returns None.

## Source

`hilllab/migration/Bundle.py`, lines 201–213 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L201-L213)
