# clean_parse

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} clean_parse(parse_results, stopwords)
:module: hilllab.indexer.parse
:canonical: hilllab.indexer.parse.clean_parse
```

## Behavior and usage

Returns `(filtered_keywords, keywords_present)` from a sequence of text strings and a stopword collection. It lowercases, keeps printable alphabetic characters/whitespace, strips digits and punctuation, and removes exact stopwords. Repeated keywords remain repeated. This deliberately loses numeric identifiers and non-English letters.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `parse_results` | `required` | Iterable of strings returned by a format parser. |
| `stopwords` | `required` | Collection of lowercase words to remove by exact membership matching. |

## Returns and side effects

Returns `(filtered_keywords, keywords_present)` from a sequence of text strings and a stopword collection.

## Source

`hilllab/indexer/parse.py`, lines 44–80 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parse.py#L44-L80)
