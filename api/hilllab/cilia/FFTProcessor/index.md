# hilllab.cilia.FFTProcessor

Compiled C# FFT processing and its Python binary-publishing utility.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`publish`](publish.md) | Moves all EXE/DLL files recursively from `bin/Release/net10.0/win-x64/publish` into the processor folder, replacing existing destination files; returns `None`. | needs review |

## MATLAB and C# functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`Program.Main`](Program.Main.md) | Loads video frames as grayscale, uses the actual read-frame count, subtracts pixel means, and computes MATLAB-scaled FFTs in parallel over rows. | needs review |

## Data and supporting resources

(resource-fftprocessor-csproj)=

### FFTProcessor.csproj

Build configuration for the FFTProcessor C# entry point.

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/FFTProcessor/FFTProcessor.csproj).

(resource-fftprocessor-exe)=

### FFTProcessor.exe

Compiled Windows executable/native dependency shipped with the FFT processor. No callable Python definition is contained in this asset. Behavior is documented from Program.cs and the Python wrapper; binary equivalence and platform operation were not tested. This documentation does not execute or reverse-engineer the binary.

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/FFTProcessor/FFTProcessor.exe).

(resource-opencvsharpextern-dll)=

### OpenCvSharpExtern.dll

Compiled Windows executable/native dependency shipped with the FFT processor. No callable Python definition is contained in this asset. Behavior is documented from Program.cs and the Python wrapper; binary equivalence and platform operation were not tested. This documentation does not execute or reverse-engineer the binary.

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/FFTProcessor/OpenCvSharpExtern.dll).

(resource-opencv-videoio-ffmpeg4110-64-dll)=

### opencv_videoio_ffmpeg4110_64.dll

Compiled Windows executable/native dependency shipped with the FFT processor. No callable Python definition is contained in this asset. Behavior is documented from Program.cs and the Python wrapper; binary equivalence and platform operation were not tested. This documentation does not execute or reverse-engineer the binary.

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/FFTProcessor/opencv_videoio_ffmpeg4110_64.dll).

```{toctree}
:hidden:
:maxdepth: 1

Program.Main <Program.Main>
publish <publish>
```
