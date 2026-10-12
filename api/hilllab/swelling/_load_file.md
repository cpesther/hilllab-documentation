# _load_file

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The channels argument is accepted but ignored; the implementation always extracts exactly two channels. Numeric column-name formatting must match the expected strings.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _load_file(path, channels=2)
:module: hilllab.swelling._load_file
:canonical: hilllab.swelling._load_file._load_file
```

## Behavior and usage

Reads a tab-delimited UTF-16 plate-reader export with header row index 2, removes the last four rows and every 17th separator row, fills blanks with zero, splits numbered columns into two channels, formats each into extended reads, and returns `(c1, c2, num_reads)`. Requires the expected 24-column-per-channel layout.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Tab-delimited UTF-16 two-channel plate-reader export path. |
| `channels` | `2` | Accepted but unused; always extracts two channels. |

## Returns and side effects

Reads a tab-delimited UTF-16 plate-reader export with header row index 2, removes the last four rows and every 17th separator row, fills blanks with zero, splits numbered columns into two channels, formats each into extended reads, and returns `(c1, c2, num_reads)`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration._plate_format_extended._plate_format_extended`](../migration/_plate_format_extended.md)

## Source

`hilllab/swelling/_load_file.py`, lines 8–52 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/swelling/_load_file.py#L8-L52)
