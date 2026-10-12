# parse_yaml

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_yaml(full_path)
:module: hilllab.indexer.parsers.yaml
:canonical: hilllab.indexer.parsers.yaml.parse_yaml
```

## Behavior and usage

Loads UTF-8 YAML with safe_load and returns recursively encountered nonblank string values. Keys, numeric scalars, and other types are ignored; errors return None. Requires PyYAML, which is not declared in HillLab's dependency list.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Loads UTF-8 YAML with safe_load and returns recursively encountered nonblank string values. Keys, numeric scalars, and other types are ignored; errors return None.

## Source

`hilllab/indexer/parsers/yaml.py`, lines 4–29 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/yaml.py#L4-L29)
