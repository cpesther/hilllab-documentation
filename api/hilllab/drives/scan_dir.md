# scan_dir

[Folder overview](index.md)

## Signature

```{py:function} scan_dir(path, dbconnection, trigger)
:module: hilllab.drives.scan_dir
:canonical: hilllab.drives.scan_dir.scan_dir
```

## Behavior and usage

Recursively scans yielded paths, commits every 100 entries, deduplicates and compiles directory metrics, then commits and returns `None`. It aborts after more than ten consecutive failures. The starting directory itself is not yielded. `trigger` is forwarded to scan_file; a verify scan still runs cleanup/compilation afterward, so the whole scan_dir workflow is not read-only.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. the path at which scanning should begin |
| `dbconnection` | `required` | **DBConnection**. the database connection object used to write the data to the .db file. |
| `trigger` | `required` | **string**. controls how the data from this scan is used.  A value of 'build' will force data entry into the connected database, while a value of 'verify' will only return the item info without touching the database. |

## Returns and side effects

Recursively scans yielded paths, commits every 100 entries, deduplicates and compiles directory metrics, then commits and returns `None`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.drives.compile_db.compile_db`](compile_db.md)
- [`hilllab.drives.scan_file.scan_file`](scan_file.md)
- [`hilllab.drives.sweep_db.sweep_db`](sweep_db.md)
- [`hilllab.utilities.yeild_dir.yield_dir`](../utilities/yield_dir.md)

## Source

`hilllab/drives/scan_dir.py`, lines 8–62 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/scan_dir.py#L8-L62)
