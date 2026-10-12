# parser_dispatch

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parser_dispatch(extension)
:module: hilllab.indexer.parse
:canonical: hilllab.indexer.parse.parser_dispatch
```

## Behavior and usage

Returns the callable parser for a lowercase, dot-free extension such as csv/xlsx/json/pdf, or None for unsupported values. It supports text/config extensions through parse_txt and Office XML variants through their document parsers. The mapping itself is in the source evidence. Case normalization is the caller's responsibility.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `extension` | `required` | Lowercase extension without a leading dot, for example csv or pdf. Returns None if unsupported. |

## Returns and side effects

Returns the callable parser for a lowercase, dot-free extension such as csv/xlsx/json/pdf, or None for unsupported values.

## Source

`hilllab/indexer/parse.py`, lines 6–42 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parse.py#L6-L42)
