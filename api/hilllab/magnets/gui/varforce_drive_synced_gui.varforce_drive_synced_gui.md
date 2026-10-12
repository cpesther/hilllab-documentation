# varforce_drive_synced_gui

[Folder overview](index.md)

:::{note}
Source documentation is sparse; this description comes from the embedded MATLAB code, not a running App Designer session.
:::

## Signature

```matlab
function app = varforce_drive_synced_gui(varargin)
```

## Inputs

varargin: startup arguments passed through to the opening callback.

## Description, outputs, and use

Constructor returning the new or existing singleton app. Creates/registers components and runs startup if no app is active; otherwise focuses the existing figure. No-output construction clears the local reference while leaving the registered app lifecycle in MATLAB.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/varforce_drive_synced_gui.mlapp) · `hilllab/magnets/gui/varforce_drive_synced_gui.mlapp`

Inspect the embedded MATLAB code in App Designer; these callback descriptions do not require running the app.
