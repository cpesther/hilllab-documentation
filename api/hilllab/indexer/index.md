# hilllab.indexer

A separate SQLAlchemy-based document/file index with format-specific text parsers and experimental terminal menus.

## Subfolders

| Group | Purpose |
| --- | --- |
| [menus](menus/index.md) | Prototype terminal menu interfaces. The main menu's advertised actions are not implemented. |
| [parsers](parsers/index.md) | Extract text from local document formats for indexing; these are not assay-data loaders. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`add_file`](add_file.md) | Scans a path, creates a random item_id and local timestamp/user/node metadata, optionally records extracted keywords, and commits the File through a managed session; returns None. | needs review |
| [`add_keyword`](add_keyword.md) | Finds or inserts a Keyword row, then adds a FileKeyword association for file.item_id if absent; commits and returns None. keyword_text is used exactly as supplied. | documentation in progress |
| [`build`](build.md) | Traverses configured ROOT_DIR and calls add_file for every yielded file/directory; returns None. | documented |
| [`clean_parse`](clean_parse.md) | Returns `(filtered_keywords, keywords_present)` from a sequence of text strings and a stopword collection. | documentation in progress |
| [`get_session`](get_session.md) | A contextmanager yielding a SQLAlchemy Session. | documentation in progress |
| [`initalize_database`](initalize_database.md) | Creates declared SQLAlchemy tables on the configured engine and returns None. | documented |
| [`parser_dispatch`](parser_dispatch.md) | Returns the callable parser for a lowercase, dot-free extension such as csv/xlsx/json/pdf, or None for unsupported values. | documentation in progress |
| [`scan`](scan.md) | Returns `(File_object, keywords_or_None, keywords_present)` for readable paths, without inserting the ORM object. | needs review |
| [`traverse`](traverse.md) | Returns a generator of recursively discovered file/directory paths as POSIX strings, yielding directories before files in each os.walk step. | documentation in progress |
| [`windows_long_path`](windows_long_path.md) | Returns a Path, prefixing strings at least 260 characters long with the Windows extended-path marker unless already prefixed. | documentation in progress |

## Classes and data containers

(class-base)=

### Base

```{py:class} Base
:module: hilllab.indexer.database
:canonical: hilllab.indexer.database.Base
```

Empty subclass of SQLAlchemy DeclarativeBase used as the shared ORM metadata/registry. No HillLab methods are defined. Engine and Session are created at module scope from configured DATABASE_PATH; SQLAlchemy is an additional undeclared dependency.

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/database.py).

(class-file)=

### File

```{py:class} File
:module: hilllab.indexer.models
:canonical: hilllab.indexer.models.File
```

ORM model mapped to files, storing paths, extensions, timestamps, ownership, scan scheduling, size/count fields, and keyword relationships. Its mapped attributes and declared defaults are listed below. `file_count_recusrive` is the exact misspelled field name.

:::{admonition} Implementation needs review
:class: warning
The annotation for FileKeyword.item_id is integer while its foreign target files.item_id is a UUID-like string. Models imports Base through api, creating an import-order-sensitive cycle rather than directly from database.
:::

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `__tablename__` | Not specified | files |
| `id` | Mapped[int] | Primary key |
| `item_id` | Mapped[str] | Unique value; Indexed |
| `path` | Mapped[str] | Indexed |
| `dir_path` | Mapped[str \| None] | Indexed |
| `dir_id` | Mapped[str \| None] | Unique value; Indexed |
| `filename` | Mapped[str] | Indexed |
| `extension` | Mapped[str \| None] | Indexed |
| `suffixes` | Mapped[str \| None] | Database column |
| `is_directory` | Mapped[bool] | Default False; Indexed |
| `file_count` | Mapped[bool] | Default 0 |
| `file_count_recusrive` | Mapped[bool] | Default 0 |
| `exists` | Mapped[bool] | Default True |
| `size` | Mapped[int \| None] | Database column |
| `dt_created` | Mapped[DateTime \| None] | Database column |
| `dt_modified` | Mapped[DateTime \| None] | Database column |
| `ino` | Mapped[str \| None] | Indexed |
| `dev_id` | Mapped[str \| None] | Database column |
| `nlink` | Mapped[str \| None] | Database column |
| `uid` | Mapped[str \| None] | Database column |
| `gid` | Mapped[str \| None] | Database column |
| `dt_found` | Mapped[DateTime \| None] | Database column |
| `dt_updated` | Mapped[DateTime \| None] | Database column |
| `dt_rescan` | Mapped[DateTime \| None] | Database column |
| `node_found` | Mapped[str \| None] | Database column |
| `user_found` | Mapped[str \| None] | Database column |
| `node_updated` | Mapped[str \| None] | Database column |
| `user_updated` | Mapped[str \| None] | Database column |
| `disposition` | Mapped[str \| None] | Database column |
| `keywords` | Mapped[list['Keyword']] | ORM relationship to related records |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/models.py).

(class-keyword)=

### Keyword

```{py:class} Keyword
:module: hilllab.indexer.models
:canonical: hilllab.indexer.models.Keyword
```

ORM model mapped to keywords, with an integer primary key, a unique nonnullable keyword string, and many-to-many files relationship through file_keywords. Constructor behavior is inherited from SQLAlchemy; no handwritten methods are defined.

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `__tablename__` | Not specified | keywords |
| `keyword_id` | Mapped[int] | Primary key |
| `keyword` | Mapped[str] | Unique value; Cannot be missing |
| `files` | Mapped[list['File']] | ORM relationship to related records |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/models.py).

(class-filekeyword)=

### FileKeyword

```{py:class} FileKeyword
:module: hilllab.indexer.models
:canonical: hilllab.indexer.models.FileKeyword
```

Association ORM model using item_id and keyword_id as a composite primary key to link File and Keyword records. Constructor behavior is inherited from SQLAlchemy.

:::{admonition} Implementation needs review
:class: warning
item_id is annotated as integer although the referenced File.item_id is declared String and populated with UUID strings; this schema/type mismatch needs review.
:::

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `__tablename__` | Not specified | file_keywords |
| `item_id` | Mapped[int] | Primary key |
| `keyword_id` | Mapped[int] | Primary key |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/indexer/models.py).

## Database configuration

This index uses a configured ROOT_DIR and DATABASE_PATH, separate from the drives SQLite schema. The supplied default root is the Windows Hill Lab drive, and the database name is index.db. Scan intervals are expressed in seconds: default 86400, minimum 600, maximum 604800. The indexer.py script creates tables and runs a scan immediately when imported. Review the source configuration before running it.

```{toctree}
:hidden:
:maxdepth: 1

menus <menus/index>
parsers <parsers/index>
add_file <add_file>
add_keyword <add_keyword>
build <build>
clean_parse <clean_parse>
get_session <get_session>
initalize_database <initalize_database>
parser_dispatch <parser_dispatch>
scan <scan>
traverse <traverse>
windows_long_path <windows_long_path>
```
