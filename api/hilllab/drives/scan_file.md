# scan_file

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Insert/update exceptions are printed and suppressed, so successful return does not confirm persistence. On Windows the existence lookup uses native separators while stored paths are POSIX, risking mismatched lookups.
:::

## Signature

```{py:function} scan_file(file_path, dbconnection, trigger=None, update_queue=None)
:module: hilllab.drives.scan_file
:canonical: hilllab.drives.scan_file.scan_file
```

## Behavior and usage

Collects relative path/stat metadata against the database file's parent. Paths must lie below that parent, and os.getlogin must succeed. `trigger='verify'` returns the metadata dictionary without insertion; `'build'` always inserts; other values check for an existing row and update/insert. Normal database writes return `None` and are not committed here. `update_queue` is unused.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `file_path` | `required` | **string**. the path to the file to be scanned |
| `dbconnection` | `required` | **DBConnection**. the database connection object used to write the data to the .db file. |
| `trigger` | `None` | **string**. controls how the data from this scan is used.  A value of 'build' will force data entry into the connected database, while a value of 'verify' will only return the item info without touching the database. |
| `update_queue` | `None` | Accepted but never read or written by the supplied implementation. |

## Returns and side effects

`trigger='verify'` returns the metadata dictionary without insertion; `'build'` always inserts; other values check for an existing row and update/insert. Normal database writes return `None` and are not committed here.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.drives.safe_execute.safe_execute`](safe_execute.md)

## Source

`hilllab/drives/scan_file.py`, lines 8–119 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/scan_file.py#L8-L119)
