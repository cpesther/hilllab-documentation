# pushbutton_start_Callback

[Folder overview](index.md)

:::{admonition} Incomplete feature — in progress
:class: warning
Incomplete feature: both actual parallel recording/drive calls and fetchNext calls are commented out. The function prints that parallel processes finished without launching them. The optional initial degauss remains active and can invoke hardware or overwrite metadata.
:::

## Signature

```matlab
function pushbutton_start_Callback(app, event)
```

## Inputs

app: GUI instance; event: button event, unused.

## Description, outputs, and use

Reads GUI parameters, optionally performs an initial degauss call, ensures a parallel pool exists, and optionally saves metadata. No explicit return.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/varforce_drive_synced_gui.mlapp) · `hilllab/magnets/gui/varforce_drive_synced_gui.mlapp`

Inspect the embedded MATLAB code in App Designer; these callback descriptions do not require running the app.
