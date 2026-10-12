# Data.__init__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Data.__init__(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Data.__init__
```

## Behavior and usage

Creates empty/default state and returns None. Default read interval is 15 minutes, delay 0, column loading rate 1.5 minutes, and temperature 297 K. Raw/clean tables and radii start None; localization tables and group mappings start empty.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Creates empty/default state and returns None.

## Source

`hilllab/migration/Bundle.py`, lines 126–160 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L126-L160)
