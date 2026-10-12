# parse_csv

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} parse_csv(full_path)
:module: hilllab.indexer.parsers.p_csv
:canonical: hilllab.indexer.parsers.p_csv.parse_csv
```

## Behavior and usage

Returns every nonblank UTF-8 CSV cell as strings using csv.reader's default dialect, including header cells and numeric-looking text. Errors return None. It does not infer a numeric DataFrame or detect arbitrary delimiters.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `full_path` | `required` | Local path to a file in the format handled by this parser. Parsing failure returns None. |

## Returns and side effects

Returns every nonblank UTF-8 CSV cell as strings using csv.reader's default dialect, including header cells and numeric-looking text. Errors return None.

## Source

`hilllab/indexer/parsers/p_csv.py`, lines 4–19 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/parsers/p_csv.py#L4-L19)
