# Program.Main

[Folder overview](index.md)

:::{admonition} Process errors do not establish a failing exit status
:class: warning
The entry point returns void, prints errors, and catches general exceptions. Early returns/caught errors do not explicitly set a nonzero process exit code; check output files and diagnostics. Source review does not verify that the shipped EXE was built from this revision.
:::

## Inputs

Six command-line arguments, in order: videoPath, psdFile, freqFile, metaPath, samplingRate (float Hz), and showPrint (Boolean text).

## Description and outputs

Loads video frames as grayscale, uses the actual read-frame count, subtracts pixel means, and computes MATLAB-scaled FFTs in parallel over rows. The first 15 frequency bins are zeroed. Writes little-endian float32 PSD values in row/column/frequency order, a float32 dominant-frequency pixel map, and three text lines giving frame count, height, and width. It does not itself compute the final whole-image CBF/FFCA values. Frame allocation uses reported frame count before copying the actual frames; invalid counts or zero-frame input are not independently guarded.

The project targets .NET 10 and references MathNet.Numerics 5.0.0, OpenCvSharp4 4.11.0.20250507, and its Windows runtime.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/FFTProcessor/Program.cs) · `hilllab/cilia/FFTProcessor/Program.cs`
