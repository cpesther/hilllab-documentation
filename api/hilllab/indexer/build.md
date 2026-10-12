# build

[Folder overview](index.md)

## Signature

```{py:function} build()
:module: hilllab.indexer.api
:canonical: hilllab.indexer.api.build
```

## Behavior and usage

Traverses configured ROOT_DIR and calls add_file for every yielded file/directory; returns None. The root itself is not yielded. Each add_file already uses a committing context, so the extra sessions/commits every 100 entries are not a single batched transaction. Repeated runs can add duplicate path records.

## Inputs

No explicit input arguments.

## Returns and side effects

Traverses configured ROOT_DIR and calls add_file for every yielded file/directory; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.indexer.api.add_file`](add_file.md)
- [`hilllab.indexer.database.get_session`](get_session.md)
- [`hilllab.indexer.scanner.traverse`](traverse.md)

## Source

`hilllab/indexer/api.py`, lines 59–77 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/api.py#L59-L77)
