# cache_clear

[Folder overview](index.md)

## Signature

```{py:function} cache_clear()
:module: hilllab.utilities.cache_clear
:canonical: hilllab.utilities.cache_clear.cache_clear
```

## Behavior and usage

Recursively deletes the entire `APP_DATA_FOLDER`, including logs, snapshots, and cache subfolders, and returns `None`. It is not limited to cached data. All failures are caught and replaced by a printed message; callers do not receive a success flag. Imported utilities may retain paths pointing to the now-deleted directories.

## Inputs

No explicit input arguments.

## Returns and side effects

Recursively deletes the entire `APP_DATA_FOLDER`, including logs, snapshots, and cache subfolders, and returns `None`.

## Source

`hilllab/utilities/cache_clear.py`, lines 4–19 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/cache_clear.py#L4-L19)
