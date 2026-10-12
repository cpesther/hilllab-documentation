# scan

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
If both normal and long-path stat attempts fail, it returns bare None instead of the usual tuple. Parser dependencies are imported eagerly; unavailable optional document packages can prevent importing the scanner.
:::

## Signature

```{py:function} scan(path)
:module: hilllab.indexer.scanner
:canonical: hilllab.indexer.scanner.scan
```

## Behavior and usage

Returns `(File_object, keywords_or_None, keywords_present)` for readable paths, without inserting the ORM object. Reads stat metadata and invokes a format parser, then removes stopwords. st_ctime is stored as creation time, although its platform semantics vary. Directory size is the stat entry size, not recursively aggregated content.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | Filesystem file/directory path whose stat metadata and optional text content should be read. |

## Returns and side effects

Returns `(File_object, keywords_or_None, keywords_present)` for readable paths, without inserting the ORM object.

## Related HillLab tools

Shared functions and classes used by this tool:

- {ref}`hilllab.indexer.models.File <class-file>`
- [`hilllab.indexer.parse.clean_parse`](clean_parse.md)
- [`hilllab.indexer.parse.parser_dispatch`](parser_dispatch.md)
- [`hilllab.indexer.utilities.windows_long_path`](windows_long_path.md)

## Source

`hilllab/indexer/scanner.py`, lines 10–70 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/scanner.py#L10-L70)
