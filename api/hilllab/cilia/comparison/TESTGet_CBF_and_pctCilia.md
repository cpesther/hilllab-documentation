# TESTGet_CBF_and_pctCilia

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Parameter default tests use ~isempty, so supplied nonempty Fs/fthresh values are overwritten with 60/5. ROI is hard-coded to [10,10,1000,1000] and output directory to a developer-specific Windows folder; array dimensions do not match the inclusive ROI indexing cleanly. Treat this as a comparison prototype.
:::

## Signature

```matlab
function [mens_CBF, px_CBF, FFCA] = TESTGet_CBF_and_pctCilia(vidname,Fs,fthresh)
```

## Inputs

vidname: video path; Fs: requested frame rate in Hz; fthresh: requested PSD threshold.

## Description, outputs, and use

Reads a fixed ROI, computes mean-subtracted pixel FFTs, suppresses the first 15 bins, displays the averaged PSD, calculates FFCA, and saves a MAT file. Outputs are [mens_CBF, px_CBF, FFCA]; mens_CBF is the mean PSD vector rather than a scalar beat frequency, px_CBF is a spectral array, and FFCA is a fraction.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/comparison/TESTGet_CBF_and_pctCilia.m) · `hilllab/cilia/comparison/TESTGet_CBF_and_pctCilia.m`
