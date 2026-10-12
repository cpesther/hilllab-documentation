# get_session

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} get_session()
:module: hilllab.indexer.database
:canonical: hilllab.indexer.database.get_session
```

## Behavior and usage

A contextmanager yielding a SQLAlchemy Session. Normal exit commits, exceptions roll back and re-raise, and finally closes the session. Use `with get_session() as session:` rather than treating the return value as a Session directly.

## Inputs

No explicit input arguments.

## Returns and side effects

A contextmanager yielding a SQLAlchemy Session. Use `with get_session() as session:` rather than treating the return value as a Session directly.

## Source

`hilllab/indexer/database.py`, lines 18–27 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/database.py#L18-L27)
