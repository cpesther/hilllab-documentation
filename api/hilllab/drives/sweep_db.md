# sweep_db

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The docstring also claims orphaned-keyword deletion and space reclamation, but this implementation performs neither keyword cleanup nor VACUUM.
:::

## Signature

```{py:function} sweep_db(dbconnection)
:module: hilllab.drives.sweep_db
:canonical: hilllab.drives.sweep_db.sweep_db
```

## Behavior and usage

Deletes older duplicate path rows and returns SQLite's reported deleted-row count; it does not commit. Tied latest scan timestamps may retain multiple duplicates.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `dbconnection` | `required` | A drives.DBConnection instance exposing conn, cursor, and db_path. It is not an indexer SQLAlchemy session. |

## Returns and side effects

Deletes older duplicate path rows and returns SQLite's reported deleted-row count; it does not commit.

## Source

`hilllab/drives/sweep_db.py`, lines 3–28 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/sweep_db.py#L3-L28)
