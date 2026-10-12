# DBConnection.__init__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} DBConnection.__init__(self, db_path=None)
:module: hilllab.drives.DBConnection
:canonical: hilllab.drives.DBConnection.DBConnection.__init__
```

## Behavior and usage

Accepts an SQLite filename or compatible connection target, opens it, configures sqlite3.Row results, executes schema SQL, and returns `None`. Although db_path defaults to None, sqlite3.connect does not accept None as a usable filename; provide an explicit database path.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `db_path` | `None` | SQLite database filename or connection target; None is not a valid filename. |

## Returns and side effects

Accepts an SQLite filename or compatible connection target, opens it, configures sqlite3.Row results, executes schema SQL, and returns `None`.

## Source

`hilllab/drives/DBConnection.py`, lines 12–31 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/DBConnection.py#L12-L31)
