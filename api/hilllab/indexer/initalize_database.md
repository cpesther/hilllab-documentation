# initalize_database

[Folder overview](index.md)

## Signature

```{py:function} initalize_database()
:module: hilllab.indexer.api
:canonical: hilllab.indexer.api.initalize_database
```

## Behavior and usage

Creates declared SQLAlchemy tables on the configured engine and returns None. The function name is spelled `initalize_database` in the source. This reads the hard-coded ROOT_DIR/DATABASE_PATH configuration; it is separate from the drives DBConnection/schema database.

## Inputs

No explicit input arguments.

## Returns and side effects

Creates declared SQLAlchemy tables on the configured engine and returns None.

## Source

`hilllab/indexer/api.py`, lines 13–16 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/api.py#L13-L16)
