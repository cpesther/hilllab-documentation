# Bundle.contents

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Bundle.contents(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Bundle.contents
```

## Behavior and usage

Returns a dictionary of six Boolean presence indicators: Normalization, Localization, Radii, Results, Calibration, Groups. Checks only table lengths/non-None status, not calculation correctness or completeness.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Returns a dictionary of six Boolean presence indicators: Normalization, Localization, Radii, Results, Calibration, Groups.

## Source

`hilllab/migration/Bundle.py`, lines 75–97 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L75-L97)
