# traverse

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} traverse(traverse_path)
:module: hilllab.indexer.scanner
:canonical: hilllab.indexer.scanner.traverse
```

## Behavior and usage

Returns a generator of recursively discovered file/directory paths as POSIX strings, yielding directories before files in each os.walk step. No sorting, filtering, or root-path emission is provided.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `traverse_path` | `required` | Starting directory for recursive os.walk traversal. |

## Returns and side effects

Returns a generator of recursively discovered file/directory paths as POSIX strings, yielding directories before files in each os.walk step.

## Source

`hilllab/indexer/scanner.py`, lines 73–88 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/scanner.py#L73-L88)
