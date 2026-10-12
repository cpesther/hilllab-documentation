# windows_long_path

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} windows_long_path(path)
:module: hilllab.indexer.utilities
:canonical: hilllab.indexer.utilities.windows_long_path
```

## Behavior and usage

Returns a Path, prefixing strings at least 260 characters long with the Windows extended-path marker unless already prefixed. It does not normalize to an absolute path, test the OS, or implement UNC-specific conversion; use only with appropriate Windows paths.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Path-like Windows filename to convert to a Path, adding an extended-path prefix at length 260 or greater. |

## Returns and side effects

Returns a Path, prefixing strings at least 260 characters long with the Windows extended-path marker unless already prefixed.

## Source

`hilllab/indexer/utilities.py`, lines 4–10 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/utilities.py#L4-L10)
