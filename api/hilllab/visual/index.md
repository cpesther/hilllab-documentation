# hilllab.visual

OpenCV video conversion, editing, binning, frame extraction, brightness handling, and camera calibration lookup.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_bin_video`](batch_bin_video.md) | Recursively processes files matching the full `extension`, saves each binned AVI beside its source, and returns `None`. | documentation in progress |
| [`batch_convert_to_avi`](batch_convert_to_avi.md) | Recursively converts MP4 files only, preserving relative subfolders and writing `.avi` below `output_folder`; returns `None`. | documentation in progress |
| [`batch_edit_video`](batch_edit_video.md) | Recursively edits AVI/MP4 inputs into AVI files in mirrored output folders and returns `None`. | documentation in progress |
| [`batch_extract_frame`](batch_extract_frame.md) | Recursively finds matching videos and saves one PNG per video into a shared output folder; returns `None`. | documentation in progress |
| [`batch_normalize_video_brightness`](batch_normalize_video_brightness.md) | Runs normalization for every matching video recursively and returns `None`; keyword options such as `normalized_brightness` are forwarded. | documentation in progress |
| [`bin_video`](bin_video.md) | Returns the path string of `BINx<bin_size>_<stem>.avi` next to the source. | documented |
| [`calculate_mean_brightness`](calculate_mean_brightness.md) | Returns NumPy's mean of the BGR-to-gray converted supplied frame, or the first video frame if no frame is given. | documented |
| [`convert_to_avi`](convert_to_avi.md) | Writes to the explicit `output_path` and returns `None`. | documented |
| [`edit_video`](edit_video.md) | Writes the edited video and returns `None`. | needs review |
| [`extract_frame`](extract_frame.md) | Seeks the zero-based frame index, optionally resizes by `scale_percent`, saves `<stem>_frame<index>.png`, and returns the BGR frame array. | documented |
| [`normalize_video_brightness`](normalize_video_brightness.md) | Samples evenly spaced frames, computes their grayscale means, and multiplies every color frame by target/sample-mean brightness before clipping to uint8. | needs review |
| [`show_camera_info`](show_camera_info.md) | Prints every camera's JSON specifications as console tables and returns `None`. | documented |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_get_camera_info`](_get_camera_info.md) | Reads the packaged camera JSON and returns the selected camera dictionary. | documented |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`edit_video.apply_edits`](edit_video.apply_edits.md) | Closure-local transformation of a BGR uint8 frame; returns the edited frame using parent brightness, contrast, gamma table, saturation, and sharpness settings. | documentation in progress |

## Data and supporting resources

(resource-cameras-json)=

### cameras.json

Camera calibration values used by [_get_camera_info](_get_camera_info.md). Sensor pixel width is in micrometers; divide by magnification for the effective width.

| Camera | Model | Pixel width (µm) | Resolution | Frame rate |
| --- | --- | --- | --- | --- |
| GS3 | GS3-U3-51S5M-C | 3.45 | 2448 × 2048 | 75 fps |
| FL3 | FL3-U3-13Y3M-C | 4.8 | 1280 × 1024 | 150 fps |
| ORCA | C11440-36U | 5.86 | 1920 × 1200 | 65 fps |

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/visual/cameras.json).

```{toctree}
:hidden:
:maxdepth: 1

_get_camera_info <_get_camera_info>
batch_bin_video <batch_bin_video>
batch_convert_to_avi <batch_convert_to_avi>
batch_edit_video <batch_edit_video>
batch_extract_frame <batch_extract_frame>
batch_normalize_video_brightness <batch_normalize_video_brightness>
bin_video <bin_video>
calculate_mean_brightness <calculate_mean_brightness>
convert_to_avi <convert_to_avi>
edit_video <edit_video>
edit_video.apply_edits <edit_video.apply_edits>
extract_frame <extract_frame>
normalize_video_brightness <normalize_video_brightness>
show_camera_info <show_camera_info>
```
