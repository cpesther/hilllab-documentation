# parse_excel

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_excel(full_path)
:module: hilllab.indexer.parsers.excel
:canonical: hilllab.indexer.parsers.excel.parse_excel
```

## Behavior and usage

Returns nonblank string cell values from pandas' default first worksheet, excluding numeric cells and header names. Any parsing exception returns None rather than an empty list. Excel formats depend on installed engines; additional worksheets are not scanned.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns nonblank string cell values from pandas' default first worksheet, excluding numeric cells and header names. Any parsing exception returns None rather than an empty list.

## Source

`hilllab/indexer/parsers/excel.py`, lines 4–25 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/excel.py#L4-L25)
