# hilllab.drives

Scan filesystem metadata into an SQLite database using the DBConnection wrapper and packaged SQL schema.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`compile_db`](compile_db.md) | Updates each directory row's immediate file_count and recursive count/size from rows whose dir_path matches the directory or its descendants, commits, and returns `None`. | needs review |
| [`safe_execute`](safe_execute.md) | Calls a no-argument callable and returns its result; on any Exception returns None without logging. | documented |
| [`scan_dir`](scan_dir.md) | Recursively scans yielded paths, commits every 100 entries, deduplicates and compiles directory metrics, then commits and returns `None`. | documented |
| [`scan_file`](scan_file.md) | Collects relative path/stat metadata against the database file's parent. | needs review |
| [`sweep_db`](sweep_db.md) | Deletes older duplicate path rows and returns SQLite's reported deleted-row count; it does not commit. | needs review |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`compile_db.iterate_directories`](compile_db.iterate_directories.md) | Closure-local generator yielding `(id, path)` pairs for rows marked is_directory=1. | documentation in progress |
| [`DBConnection.__init__`](DBConnection.__init__.md) | Accepts an SQLite filename or compatible connection target, opens it, configures sqlite3.Row results, executes schema SQL, and returns `None`. | documentation in progress |

## Classes and data containers

(class-dbconnection)=

### DBConnection

```{py:class} DBConnection
:module: hilllab.drives.DBConnection
:canonical: hilllab.drives.DBConnection.DBConnection
```

Creates an SQLite connection/cursor, applies packaged schema.sql, and commits immediately. Instances expose db_path, conn, and cursor for the scanning helpers. No context manager or close method is supplied; close `connection.conn` yourself when finished.

[Constructor arguments and defaults](DBConnection.__init__.md).

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `db_path` | Not specified | Set from the supplied arguments or runtime context. |
| `conn` | Not specified | Set from the supplied arguments or runtime context. |
| `cursor` | Not specified | Set from the supplied arguments or runtime context. |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/DBConnection.py).

## Data and supporting resources

(resource-schema-sql)=

### schema.sql

SQLite schema executed by drives.DBConnection. Includes files, keywords, file_keywords, metadata, versioning, sectors, rules, and policies tables. File sizes are bytes; timestamp fields are populated by scanner code. It is distinct from the SQLAlchemy indexer schema.

:::{admonition} Index-name collision
:class: warning
Both path and dir_path CREATE INDEX statements use idx_files_path with IF NOT EXISTS. The second statement does not create a separate dir_path index when the first name already exists.
:::

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/schema.sql).

```{toctree}
:hidden:
:maxdepth: 1

compile_db <compile_db>
compile_db.iterate_directories <compile_db.iterate_directories>
DBConnection.__init__ <DBConnection.__init__>
safe_execute <safe_execute>
scan_dir <scan_dir>
scan_file <scan_file>
sweep_db <sweep_db>
```
