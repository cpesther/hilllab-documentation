# compile_db

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Recursive size sums already-stored directory sizes as well as file sizes, so repeated compilations can double-count nested content. The name file_count does not imply a files-only SQL filter.
:::

## Signature

```{py:function} compile_db(dbconnection)
:module: hilllab.drives.compile_db
:canonical: hilllab.drives.compile_db.compile_db
```

## Behavior and usage

Updates each directory row's immediate file_count and recursive count/size from rows whose dir_path matches the directory or its descendants, commits, and returns `None`. Counts include both file and directory records.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `dbconnection` | `required` | A drives.DBConnection instance exposing conn, cursor, and db_path. It is not an indexer SQLAlchemy session. |

## Returns and side effects

Updates each directory row's immediate file_count and recursive count/size from rows whose dir_path matches the directory or its descendants, commits, and returns `None`.

## Source

`hilllab/drives/compile_db.py`, lines 3–56 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/compile_db.py#L3-L56)
