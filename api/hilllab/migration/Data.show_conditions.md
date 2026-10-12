# Data.show_conditions

[Folder overview](index.md)

## Signature

```{py:method} Data.show_conditions(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Data.show_conditions
```

## Behavior and usage

Prints current read count, timing, temperature, extended mode, and method metadata; returns None. These values are what is stored in the bundle, not independently read from instrument metadata.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Prints current read count, timing, temperature, extended mode, and method metadata; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)

## Source

`hilllab/migration/Bundle.py`, lines 163–176 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L163-L176)
