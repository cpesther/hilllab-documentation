# hilllab.cilia.comparison

MATLAB comparison routines for pixel-wise CBF/FFCA analysis; these contain fixed ROI/output settings.

## MATLAB and C# functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`TESTGet_CBF_and_pctCilia`](TESTGet_CBF_and_pctCilia.md) | Reads a fixed ROI, computes mean-subtracted pixel FFTs, suppresses the first 15 bins, displays the averaged PSD, calculates FFCA, and saves a MAT file. | needs review |
| [`TESTrun_CBF_on_folder`](TESTrun_CBF_on_folder.md) | Recursively finds AVI files, asks for y confirmation, calls the comparison calculator on each, and warns/continues on errors. | needs review |
```{toctree}
:hidden:
:maxdepth: 1

TESTGet_CBF_and_pctCilia <TESTGet_CBF_and_pctCilia>
TESTrun_CBF_on_folder <TESTrun_CBF_on_folder>
```
