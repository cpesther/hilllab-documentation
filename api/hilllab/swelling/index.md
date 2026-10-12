# hilllab.swelling

Two-channel plate-reader swelling analysis using spatial fluorescence integrals and grouped time courses.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`calculate_NIF`](calculate_NIF.md) | Returns a DataFrame of per-column Simpson integrals across a fixed 16-point spatial grid `0, 4.5, …, 67.5`. | documentation in progress |
| [`process_2C_swelling`](process_2C_swelling.md) | Loads two channels, integrates them, divides each well by its first retained integral, groups selected column numbers, and samples every read_sample_interval rows. groups should be a mapping of group names to one-based column-number lists. | needs review |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_access_read`](_access_read.md) | Returns the 16-row slice starting at `int(read_number*16)` from a channel table. | documentation in progress |
| [`_load_file`](_load_file.md) | Reads a tab-delimited UTF-16 plate-reader export with header row index 2, removes the last four rows and every 17th separator row, fills blanks with zero, splits numbered columns into two channels, formats each into extended reads, and returns `(c1, c2, num_reads)`. | needs review |
| [`process_2C_swelling._delta_normalize_columns`](process_2C_swelling._delta_normalize_columns.md) | Closure-local function returning a new DataFrame with each column divided by its first integral value. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

_access_read <_access_read>
_load_file <_load_file>
calculate_NIF <calculate_NIF>
process_2C_swelling <process_2C_swelling>
process_2C_swelling._delta_normalize_columns <process_2C_swelling._delta_normalize_columns>
```
