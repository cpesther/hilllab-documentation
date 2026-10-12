# generate_neighbor_path

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
With `check_safety=True`, the function passes `full_path.stem` to `generate_safe_name`, losing the requested extension and returning a string instead of the usual Path. Treat this mode as incomplete.
:::

## Signature

```{py:function} generate_neighbor_path(path, extension, prefix=None, suffix=None, name=None, check_safety=False)
:module: hilllab.utilities.generate_neighbor_path
:canonical: hilllab.utilities.generate_neighbor_path.generate_neighbor_path
```

## Behavior and usage

Returns a sibling `Path` formed from a source path, requested extension, optional prefix/suffix, and optional replacement name. Without `name`, the base is the stem before its first dot. It does not create a file or directory.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the full path to the file which the resultant path should be a neighbor to. |
| `extension` | `required` | **string**. the file extension which this new path should use (with or without preceeding period) |
| `prefix` | `None` | **string**. a string to append at the front of the new file's name. |
| `suffix` | `None` | **string**. a string to append at the end of the new file's name before the extension. |
| `name` | `None` | **string**. an entirely custom name to give the newly generated file path. If none is provided, the name of the file provided in the path argument will be used along with any provided prefix or suffix. |
| `check_safety` | `False` | **bool**. if True, the function will automatically check if a file with this path already exists, and if so, it will add an increment to the end of the file name until no collision is found. |

## Returns and side effects

Returns a sibling `Path` formed from a source path, requested extension, optional prefix/suffix, and optional replacement name.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.generate_safe_name.generate_safe_name`](generate_safe_name.md)

## Source

`hilllab/utilities/generate_neighbor_path.py`, lines 6–65 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/generate_neighbor_path.py#L6-L65)
