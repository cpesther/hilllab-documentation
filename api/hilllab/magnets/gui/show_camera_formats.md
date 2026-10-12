# show_camera_formats

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The upper-bound device count is checked, but zero/negative/noninteger IDs are not validated.
:::

## Signature

```matlab
function show_camera_formats(cameraID)
```

## Inputs

cameraID: one-based index into PointGrey adaptor device information, default 1.

## Description, outputs, and use

Prints supported format strings and the device name; no explicit output. Requires MATLAB image-acquisition hardware support.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/show_camera_formats.m) · `hilllab/magnets/gui/show_camera_formats.m`
