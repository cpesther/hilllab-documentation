# parse_pdf

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_pdf(full_path)
:module: hilllab.indexer.parsers.pdf
:canonical: hilllab.indexer.parsers.pdf.parse_pdf
```

## Behavior and usage

Returns stripped nonempty lines extracted from PDF pages by PyPDF2; errors return None. This is text extraction without OCR, so scanned images can produce an empty list. PyPDF2 is not declared in the package dependencies.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns stripped nonempty lines extracted from PDF pages by PyPDF2; errors return None.

## Source

`hilllab/indexer/parsers/pdf.py`, lines 4–21 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/pdf.py#L4-L21)
