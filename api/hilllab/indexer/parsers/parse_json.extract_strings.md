# parse_json.extract_strings

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} parse_json.extract_strings(obj)
:module: hilllab.indexer.parsers.json
:canonical: hilllab.indexer.parsers.json.parse_json.extract_strings
```

## Behavior and usage

Closure-local recursive visitor appending string values to the parent words list. Takes a JSON-decoded object and returns None. It descends dictionary values and list items, but not keys or other value types.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `obj` | `required` | JSON-decoded scalar/list/dictionary to visit recursively. |

## Returns and side effects

Takes a JSON-decoded object and returns None.

## Source

`hilllab/indexer/parsers/json.py`, lines 14–23 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/json.py#L14-L23)
