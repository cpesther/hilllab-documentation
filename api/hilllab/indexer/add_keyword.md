# add_keyword

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} add_keyword(file, keyword_text)
:module: hilllab.indexer.api
:canonical: hilllab.indexer.api.add_keyword
```

## Behavior and usage

Finds or inserts a Keyword row, then adds a FileKeyword association for file.item_id if absent; commits and returns None. keyword_text is used exactly as supplied. File insertion and keyword association are separate transactions; use an existing persistent item_id when extending this routine.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `file` | `required` | Indexer File ORM instance with item_id set; association insertion is separate from File insertion. |
| `keyword_text` | `required` | Exact keyword string to find or insert. |

## Returns and side effects

Finds or inserts a Keyword row, then adds a FileKeyword association for file.item_id if absent; commits and returns None. keyword_text is used exactly as supplied.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.indexer.database.get_session`](get_session.md)
- {ref}`hilllab.indexer.models.FileKeyword <class-filekeyword>`
- {ref}`hilllab.indexer.models.Keyword <class-keyword>`

## Source

`hilllab/indexer/api.py`, lines 80–108 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/api.py#L80-L108)
