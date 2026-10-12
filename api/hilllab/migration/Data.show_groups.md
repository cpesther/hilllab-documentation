# Data.show_groups

[Folder overview](index.md)

## Signature

```{py:method} Data.show_groups(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Data.show_groups
```

## Behavior and usage

Prints the current group mapping and returns None. An empty mapping reaches print_dict_table's max() on an empty sequence and fails.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Prints the current group mapping and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)

## Source

`hilllab/migration/Bundle.py`, lines 184–186 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L184-L186)
