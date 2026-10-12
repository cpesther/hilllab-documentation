# _load_with_groups

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _load_with_groups(h5_path, groups_path=None, expectations=[])
:module: hilllab.dynamics._load_with_groups
:canonical: hilllab.dynamics._load_with_groups._load_with_groups
```

## Behavior and usage

Returns a summary DataFrame with a group column. Checks named expectations, then loads an explicit groups JSON or the newest sibling filename containing `.groups.json`. JSON maps group names to identifiers; unmatched IDs become NaN and duplicate IDs use the last mapping. Without a groups file, group equals identifier. Confirm automatic file selection before comparing experiments.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the path to the h5 file to be loaded |
| `groups_path` | `None` | **string**. the path to the .groups.json file to be  used for group assignment. If None, the most recently modified .groups.json file in the same directory as the h5 file will be used, or if none exist, groups will be the same as the identifier. |
| `expectations` | `[]` | **list**. a list of strings indicating what features of the data (such as classification or identification) are exepcted to be included, allowing for quick error handling and user guidance. |

## Returns and side effects

Returns a summary DataFrame with a group column.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.print_dict_table.print_dict_table`](../utilities/print_dict_table.md)

## Source

`hilllab/dynamics/_load_with_groups.py`, lines 11–94 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/_load_with_groups.py#L11-L94)
