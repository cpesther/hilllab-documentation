# TESTrun_CBF_on_folder

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Inherits the fixed ROI/output and overridden parameter issues of TESTGet_CBF_and_pctCilia.
:::

## Signature

```matlab
function TESTrun_CBF_on_folder(rootFolder, Fs, fthresh)
```

## Inputs

rootFolder: existing starting directory; Fs/fthresh: forwarded sampling rate and threshold.

## Description, outputs, and use

Recursively finds AVI files, asks for y confirmation, calls the comparison calculator on each, and warns/continues on errors. No explicit return value.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/comparison/TESTrun_CBF_on_folder.m) · `hilllab/cilia/comparison/TESTrun_CBF_on_folder.m`
