# DACoperator

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Default-argument nargin checks are shifted relative to the signature containing final_degauss. Hardware code calls misspelled postixtime and is caught into fallback. Vrange defaults in code to [-5,5], not the docstring [-10,10]. Caller-supplied channel indices do not drive the fixed hardware mapping. Review before hardware use.
:::

## Signature

```matlab
function v = DACoperator(inputs, final_degauss, Nrepeat, board, channels, srate, Vrange)
```

## Inputs

inputs: M×N voltage samples; final_degauss: final signal matrix; Nrepeat: extra repeats; board: daqtest or PCIe-6738; channels: requested channel indices; srate: Hz; Vrange: clipping limits.

## Description, outputs, and use

Clips voltages, attempts hardware output for PCIe-6738, falls back to virtual plotting, constructs repeated/final degauss signals, and returns v as a Unix start timestamp (or 0 on signal-allocation failure). Hardware mapping is fixed to six channels on Dev2. The fallback still plots and computes timing; it does not establish that voltage was delivered.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/DACoperator.m) · `hilllab/magnets/gui/DACoperator.m`
