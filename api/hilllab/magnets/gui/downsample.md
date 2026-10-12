# downsample

[Folder overview](index.md)

## Signature

```matlab
function outs = downsample(input, factor)
```

## Inputs

input: row-organized numeric matrix; factor: positive integer stride.

## Description, outputs, and use

Local MATLAB helper returning input(1:factor:end,:), taking every factor-th row while preserving columns. This is decimation without filtering, used only for faster plots.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/DACoperator.m) · `hilllab/magnets/gui/DACoperator.m`
