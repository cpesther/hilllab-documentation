# parse_word

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_word(full_path)
:module: hilllab.indexer.parsers.word
:canonical: hilllab.indexer.parsers.word.parse_word
```

## Behavior and usage

Returns words split on literal spaces from nonempty document paragraphs; errors return None. Word tables, headers/footers, and images are not traversed. Requires python-docx as an additional dependency.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns words split on literal spaces from nonempty document paragraphs; errors return None.

## Source

`hilllab/indexer/parsers/word.py`, lines 4–23 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/word.py#L4-L23)
