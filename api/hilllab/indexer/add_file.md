# add_file

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
scan() can return bare None, but the three values are unpacked before the intended missing-file check, causing TypeError. Keyword associations are committed in separate sessions before the File itself, rather than one atomic transaction.
:::

## Signature

```{py:function} add_file(path)
:module: hilllab.indexer.api
:canonical: hilllab.indexer.api.add_file
```

## Behavior and usage

Scans a path, creates a random item_id and local timestamp/user/node metadata, optionally records extracted keywords, and commits the File through a managed session; returns None. Calls do not deduplicate files by path, and os.getlogin requires a login-capable environment.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | File or directory path to scan and add to the configured index database. |

## Returns and side effects

Scans a path, creates a random item_id and local timestamp/user/node metadata, optionally records extracted keywords, and commits the File through a managed session; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.indexer.api.add_keyword`](add_keyword.md)
- [`hilllab.indexer.database.get_session`](get_session.md)
- [`hilllab.indexer.scanner.scan`](scan.md)

## Source

`hilllab/indexer/api.py`, lines 20–56 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/api.py#L20-L56)
