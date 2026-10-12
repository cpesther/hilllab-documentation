# edit_sequences_Callback

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
str2num interprets MATLAB expressions; the input is not restricted to a simple numeric-list parser.
:::

## Signature

```matlab
function edit_sequences_Callback(app, event)
```

## Inputs

app: GUI instance; event: edit event, unused.

## Description, outputs, and use

Parses pulse widths/sequence count and updates text_expt_duration.Text with their product. No explicit output.

## Source

[View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/gui/varforce_drive_synced_gui.mlapp) · `hilllab/magnets/gui/varforce_drive_synced_gui.mlapp`

Inspect the embedded MATLAB code in App Designer; these callback descriptions do not require running the app.
