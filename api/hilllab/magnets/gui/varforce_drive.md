# varforce_drive

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Filename is required without a default check. Multiple/no zero-voltage pulse entries and unguarded geometry divisions can invalidate degauss construction. The underlying DACoperator has hardware defects. This records requested signals, not independently verified output.
:::

## Signature

```matlab
function params_out = varforce_drive(params, filename)
```

## Inputs

params: MATLAB struct of DAQ/pole/waveform/degauss settings; filename: metadata MAT destination.

## Description, outputs, and use

Builds six-channel voltage and final-degauss matrices, calls DACoperator, and returns params_out with sent_signal, start_time, and dominant_coil added. Also saves the struct fields into filename. Defaults include daqtest, 100000 Hz, zero extra repeats, pole1-flat, voltages 0:5, one-second pulses, degauss on, tau .0012, and degauss frequency 10000.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/varforce_drive.m) · `hilllab/magnets/gui/varforce_drive.m`
