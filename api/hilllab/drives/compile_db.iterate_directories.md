# compile_db.iterate_directories

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} compile_db.iterate_directories(dbconnection)
:module: hilllab.drives.compile_db
:canonical: hilllab.drives.compile_db.compile_db.iterate_directories
```

## Behavior and usage

Closure-local generator yielding `(id, path)` pairs for rows marked is_directory=1. Uses the shared DBConnection cursor; the parent uses separate cursors to avoid invalidating this iteration.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `dbconnection` | `required` | A drives.DBConnection instance exposing conn, cursor, and db_path. It is not an indexer SQLAlchemy session. |

## Returns and side effects

Closure-local generator yielding `(id, path)` pairs for rows marked is_directory=1.

## Source

`hilllab/drives/compile_db.py`, lines 11–21 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/compile_db.py#L11-L21)
