# parse_powerpoint

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_powerpoint(full_path)
:module: hilllab.indexer.parsers.powerpoint
:canonical: hilllab.indexer.parsers.powerpoint.parse_powerpoint
```

## Behavior and usage

Returns nonempty text from PowerPoint shapes exposing a text attribute; errors return None. Notes, embedded files, images, and nested group-shape recursion are not implemented. Requires python-pptx as an additional dependency.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns nonempty text from PowerPoint shapes exposing a text attribute; errors return None.

## Source

`hilllab/indexer/parsers/powerpoint.py`, lines 4–20 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/powerpoint.py#L4-L20)
