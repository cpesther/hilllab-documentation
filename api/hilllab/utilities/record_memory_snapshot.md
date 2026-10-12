# record_memory_snapshot

[Folder overview](index.md)

## Signature

```{py:function} record_memory_snapshot(breakpoint=None, active=True)
:module: hilllab.utilities.record_memory_snapshot
:canonical: hilllab.utilities.record_memory_snapshot.record_memory_snapshot
```

## Behavior and usage

When active, captures a tracemalloc snapshot and pickles it below `SNAPSHOT_FOLDER_PATH`; returns `None`. `breakpoint` adds a filename label, so use filesystem-safe text. Importing this module starts tracemalloc globally, and snapshots require the utilities-created directory to remain available.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `breakpoint` | `None` | **str**. a value that can be added to the file name to more clearly indicate where the snapshot is being taken. |
| `active` | `True` | **bool**. allows us to "turn off" monitoring easily when incorporated into other functions without needing to nest this function within a conditional. |

## Returns and side effects

When active, captures a tracemalloc snapshot and pickles it below `SNAPSHOT_FOLDER_PATH`; returns `None`.

## Source

`hilllab/utilities/record_memory_snapshot.py`, lines 8–43 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/record_memory_snapshot.py#L8-L43)
