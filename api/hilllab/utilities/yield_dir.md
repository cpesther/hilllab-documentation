# yield_dir

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} yield_dir(path)
:module: hilllab.utilities.yeild_dir
:canonical: hilllab.utilities.yeild_dir.yield_dir
```

## Behavior and usage

Returns a generator yielding immediate discovered subdirectories and files for each recursive os.walk step as POSIX-style path strings. It does not yield the starting root itself and does not sort results. The source filename is spelled `yeild_dir`, while the function is `yield_dir`.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Starting directory; contents are traversed recursively, excluding the root itself. |

## Returns and side effects

Returns a generator yielding immediate discovered subdirectories and files for each recursive os.walk step as POSIX-style path strings. It does not yield the starting root itself and does not sort results.

## Source

`hilllab/utilities/yeild_dir.py`, lines 5–23 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/yeild_dir.py#L5-L23)
