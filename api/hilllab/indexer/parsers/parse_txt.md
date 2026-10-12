# parse_txt

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_txt(full_path)
:module: hilllab.indexer.parsers.txt
:canonical: hilllab.indexer.parsers.txt.parse_txt
```

## Behavior and usage

Returns stripped nonempty lines from a UTF-8 text file. Any decoding or I/O exception returns None. It does not attempt another encoding or tokenize the returned lines.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns stripped nonempty lines from a UTF-8 text file. Any decoding or I/O exception returns None.

## Source

`hilllab/indexer/parsers/txt.py`, lines 2–16 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/txt.py#L2-L16)
