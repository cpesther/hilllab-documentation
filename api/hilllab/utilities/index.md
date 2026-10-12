# hilllab.utilities

Reusable path, file, formatting, plotting, logging, and data-cleaning helpers.

## Subfolders

| Group | Purpose |
| --- | --- |
| [gui](gui/index.md) | Tk popup and hover-tooltip classes. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_rename_files`](batch_rename_files.md) | Previews every immediate directory entry with `old` replaced by `new`, then renames entries only after a `Y` response. | documented |
| [`cache_clear`](cache_clear.md) | Recursively deletes the entire `APP_DATA_FOLDER`, including logs, snapshots, and cache subfolders, and returns `None`. | documented |
| [`cache_view`](cache_view.md) | Opens `APP_DATA_FOLDER` using `os.startfile`, macOS `open`, or Linux `xdg-open`; returns `None`. | documented |
| [`current_timestamp`](current_timestamp.md) | Returns the current local date/time as a string such as `October 11, 2026 at 11:30 PM`. | documentation in progress |
| [`custom_axes`](custom_axes.md) | Returns `(fig, ax)` after applying HillLab plotting styles. | documentation in progress |
| [`enable_simple_warnings`](enable_simple_warnings.md) | Sets Python's global warning formatter and returns `None`. | documented |
| [`format_duration`](format_duration.md) | Returns a space-separated duration with day/hour/minute/second components, or `0 s` for zero. | documentation in progress |
| [`format_spectra_table`](format_spectra_table.md) | Fills missing values with zero in the original DataFrame, removes every 17th row, requires exactly 24 remaining columns, and returns a table indexed with repeated A–P row labels and columns `Column 1`–`Column 24`. | documentation in progress |
| [`format_timestamp`](format_timestamp.md) | Accepts a Unix timestamp in seconds and returns `(date_string, time_string)` using local system time, formatted `MM/DD/YYYY` and `HH:MM:SS`. | documentation in progress |
| [`generate_neighbor_path`](generate_neighbor_path.md) | Returns a sibling `Path` formed from a source path, requested extension, optional prefix/suffix, and optional replacement name. | needs review |
| [`generate_safe_name`](generate_safe_name.md) | Returns `(new_file_name, new_file_path)` strings, trying the original name then numbered alternatives while preserving all filename suffixes. | documented |
| [`images_to_video`](images_to_video.md) | Lexicographically sorts immediate lowercase JPG/PNG filenames, resizes every readable image to the first image's dimensions, and writes `<folder-name>.avi` in that folder using XVID and the requested `fps`. | documented |
| [`load_matlab`](load_matlab.md) | Returns a dictionary loaded first through h5py and then, only on `OSError`, through SciPy `loadmat`. | documentation in progress |
| [`load_vrpn`](load_vrpn.md) | Returns a DataFrame extracted from `tracking.spot3DSecUsecIndexFramenumXYZRPY`. | documentation in progress |
| [`print_dict_table`](print_dict_table.md) | Prints a width-aligned console table from mapping keys/values and returns `None`. | documentation in progress |
| [`print_progress_bar`](print_progress_bar.md) | Writes an in-place console progress bar with local time; returns `None`. | needs review |
| [`record_memory_snapshot`](record_memory_snapshot.md) | When active, captures a tracemalloc snapshot and pickles it below `SNAPSHOT_FOLDER_PATH`; returns `None`. | documented |
| [`record_message`](record_message.md) | Appends timestamp/message text to `LOG_FILE_PATH` when active, independently prints when `print_message=True`, and can clear notebook output first. | documentation in progress |
| [`remove_outliers`](remove_outliers.md) | Uses the median absolute deviation scaled by `1/(sqrt(2)*erfcinv(0.5))` and keeps values within three scaled MADs. | needs review |
| [`verify_name`](verify_name.md) | Returns True for an exact valid name and False otherwise. | documented |
| [`walk_dir`](walk_dir.md) | Returns an unsorted list of file paths from a recursive os.walk. | documented |
| [`warn`](warn.md) | Installs the simplified global formatter, then emits a warning of `category` with `stacklevel`; returns `None` unless a warning filter turns it into an exception. | documentation in progress |
| [`yield_dir`](yield_dir.md) | Returns a generator yielding immediate discovered subdirectories and files for each recursive os.walk step as POSIX-style path strings. | documentation in progress |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`enable_simple_warnings._simple_warning_format`](enable_simple_warnings._simple_warning_format.md) | Closure-local warning callback returning `CategoryName: message` plus a newline. | documentation in progress |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`remove_outliers.to_number`](remove_outliers.to_number.md) | A closure-local parser taking one token and returning its float conversion or `None` on ValueError/TypeError. | documentation in progress |

## Logs and application data

Importing this package creates a HillLab application-data folder and per-session log, snapshot, CPU, and cache locations. Memory tracing is also started by a dependency import. These are shared process/filesystem effects.

| Location | Purpose |
| --- | --- |
| APP_DATA_FOLDER | Windows: APPDATA/hilllab; macOS: ~/Library/Application Support/hilllab; other systems: ~/.config/hilllab |
| LOG_FILE_PATH | Timestamp-named CSV log for the current session |
| SNAPSHOT_FOLDER_PATH | Per-session allocation snapshots |
| CPU_FOLDER_PATH | Per-session CPU folder created by initialization |
| CACHE_FOLDER_PATH | Per-session cache folder created by initialization |

## Unimplemented source items

The source contains an empty `launch_in_terminal.py` file. There is no callable implementation to document yet.

```{toctree}
:hidden:
:maxdepth: 1

gui <gui/index>
batch_rename_files <batch_rename_files>
cache_clear <cache_clear>
cache_view <cache_view>
current_timestamp <current_timestamp>
custom_axes <custom_axes>
enable_simple_warnings <enable_simple_warnings>
enable_simple_warnings._simple_warning_format <enable_simple_warnings._simple_warning_format>
format_duration <format_duration>
format_spectra_table <format_spectra_table>
format_timestamp <format_timestamp>
generate_neighbor_path <generate_neighbor_path>
generate_safe_name <generate_safe_name>
images_to_video <images_to_video>
load_matlab <load_matlab>
load_vrpn <load_vrpn>
print_dict_table <print_dict_table>
print_progress_bar <print_progress_bar>
record_memory_snapshot <record_memory_snapshot>
record_message <record_message>
remove_outliers <remove_outliers>
remove_outliers.to_number <remove_outliers.to_number>
verify_name <verify_name>
walk_dir <walk_dir>
warn <warn>
yield_dir <yield_dir>
```
