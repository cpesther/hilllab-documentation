# Bundle.show

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Fresh/incompletely initialized bundles contain None or empty dictionaries, which print_dict_table cannot handle. show() can fail until radii, groups, and calibration mappings are populated.
:::

## Signature

```{py:method} Bundle.show(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Bundle.show
```

## Behavior and usage

Prints the representation and conditions/groups/radii/calibration tables; returns None. It does not print every raw/result DataFrame despite the broad docstring wording.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Prints the representation and conditions/groups/radii/calibration tables; returns None.

## Source

`hilllab/migration/Bundle.py`, lines 57–72 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L57-L72)
