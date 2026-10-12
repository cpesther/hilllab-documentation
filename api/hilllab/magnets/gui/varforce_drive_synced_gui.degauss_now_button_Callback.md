# degauss_now_button_Callback

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Comments say metadata is not overwritten, but varforce_drive saves to app.edit_filename.Value. deg_tau/deg_freq are copied from text edit fields without str2double, unlike the Start callback. The underlying DAQ routine also needs review.
:::

## Signature

```matlab
function degauss_now_button_Callback(app, event)
```

## Inputs

app: GUI instance; event: button event, unused.

## Description, outputs, and use

Builds a fixed 5/0 V sequence for PCIe-6738, reads degauss/pole settings, calls varforce_drive, and pauses for params.duration. No explicit output.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/varforce_drive_synced_gui.mlapp) · `hilllab/magnets/gui/varforce_drive_synced_gui.mlapp`

Inspect the embedded MATLAB code in App Designer; these callback descriptions do not require running the app.
