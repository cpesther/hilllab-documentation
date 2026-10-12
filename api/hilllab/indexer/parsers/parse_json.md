# parse_json

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_json(full_path)
:module: hilllab.indexer.parsers.json
:canonical: hilllab.indexer.parsers.json.parse_json
```

## Behavior and usage

Returns nonblank string values from recursively traversed UTF-8 JSON dictionaries/lists; dictionary keys and numeric values are ignored. Any exception returns None.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns nonblank string values from recursively traversed UTF-8 JSON dictionaries/lists; dictionary keys and numeric values are ignored. Any exception returns None.

## Source

`hilllab/indexer/parsers/json.py`, lines 4–30 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/json.py#L4-L30)
