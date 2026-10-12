# record_synced_video

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Timeout/fps default checks are swapped relative to argument positions. Code defaults to 1200 frames and a 90×frames/1200 timeout, differing from the comments. Requires Image Acquisition Toolbox and the PointGrey adaptor; global imaqreset/pool cleanup affects other sessions.
:::

## Signature

```matlab
function [tStart, tEnd] = record_synced_video(path, camera, total_frames, fps, timeout_seconds)
```

## Inputs

path: filename prefix; camera: GS3 or FL3; total_frames: target frame count; fps: requested rate; timeout_seconds: wait timeout.

## Description, outputs, and use

Configures a PointGrey capture device, previews it, writes a grayscale AVI at path.avi, and returns [tStart,tEnd] Unix timestamps surrounding acquisition. Resets image acquisition objects and deletes an existing parallel pool on cleanup. It does not run Python tracking despite its original comments.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/record_synced_video.m) · `hilllab/magnets/gui/record_synced_video.m`
