# hilllab.cilia

Estimate ciliary beat frequency (CBF) and fractional functional ciliated area (FFCA) from temporal image spectra.

## Subfolders

| Group | Purpose |
| --- | --- |
| [FFTProcessor](FFTProcessor/index.md) | Compiled C# FFT processing and its Python binary-publishing utility. |
| [comparison](comparison/index.md) | MATLAB comparison routines for pixel-wise CBF/FFCA analysis; these contain fixed ROI/output settings. |
| [verification](verification/index.md) | Reference images shipped with the cilia code. No callable Python definitions are present. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_calculate_CBF_FFCA`](batch_calculate_CBF_FFCA.md) | Recursively analyzes lowercase AVI files with method `py` or `cs`, printing status and optionally prompting for confirmation; returns `None`, with one CSV per processed video. | documentation in progress |
| [`compile_CBF_FFCA`](compile_CBF_FFCA.md) | Writes compiled CSV data at the root (`compile_all=True`) or in each discovered CSV-containing subfolder; returns `None`. | documentation in progress |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_calculate_CBF_FFCA_cs`](_calculate_CBF_FFCA_cs.md) | Runs the bundled Windows FFTProcessor executable, loads float32 PSD data shaped `(height, width, frames//2+1)`, resolves CBF/FFCA, and writes a sibling CSV. | needs review |
| [`_calculate_CBF_FFCA_py`](_calculate_CBF_FFCA_py.md) | Loads grayscale frames, removes each pixel's mean, computes a one-sided PSD, zeroes the first 15 frequency bins, and writes CBF/FFCA via the shared resolver. | needs review |
| [`_resolve_CBF_FFCA`](_resolve_CBF_FFCA.md) | Returns `(cbf, ffca)`: CBF is the frequency of maximum spatially averaged PSD, and FFCA is the fraction of pixels whose maximum PSD exceeds the threshold. | needs review |
| [`compile_CBF_FFCA._compile_files`](compile_CBF_FFCA._compile_files.md) | Closure-local helper accepting CSV paths and an output folder, returning the saved CSV path string. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

FFTProcessor <FFTProcessor/index>
comparison <comparison/index>
verification <verification/index>
_calculate_CBF_FFCA_cs <_calculate_CBF_FFCA_cs>
_calculate_CBF_FFCA_py <_calculate_CBF_FFCA_py>
_resolve_CBF_FFCA <_resolve_CBF_FFCA>
batch_calculate_CBF_FFCA <batch_calculate_CBF_FFCA>
compile_CBF_FFCA <compile_CBF_FFCA>
compile_CBF_FFCA._compile_files <compile_CBF_FFCA._compile_files>
```
