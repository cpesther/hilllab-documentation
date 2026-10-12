# parse_html

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_html(full_path)
:module: hilllab.indexer.parsers.html
:canonical: hilllab.indexer.parsers.html.parse_html
```

## Behavior and usage

Reads UTF-8 HTML with BeautifulSoup and returns stripped, nonempty extracted text lines; errors return None. It does not fetch linked pages, run JavaScript, or provide structured fields.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Reads UTF-8 HTML with BeautifulSoup and returns stripped, nonempty extracted text lines; errors return None.

## Source

`hilllab/indexer/parsers/html.py`, lines 4–20 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/html.py#L4-L20)
