# parse_yaml.extract_strings

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} parse_yaml.extract_strings(obj)
:module: hilllab.indexer.parsers.yaml
:canonical: hilllab.indexer.parsers.yaml.parse_yaml.extract_strings
```

## Behavior and usage

Closure-local recursive YAML visitor appending string values into the parent words list. Returns None, visits dictionary values/list elements, and does not emit keys.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `obj` | `required` | YAML-decoded scalar/list/dictionary to visit recursively. |

## Returns and side effects

Returns None, visits dictionary values/list elements, and does not emit keys.

## Source

`hilllab/indexer/parsers/yaml.py`, lines 13–22 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/yaml.py#L13-L22)
