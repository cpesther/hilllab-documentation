# hilllab.magnets.gui

MATLAB magnet-drive and synchronized-camera tools, including hardware-specific routines and a packaged App Designer project.

## MATLAB and C# functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`DACoperator`](DACoperator.md) | Clips voltages, attempts hardware output for PCIe-6738, falls back to virtual plotting, constructs repeated/final degauss signals, and returns v as a Unix start timestamp (or 0 on signal-allocation failure). | needs review |
| [`downsample`](downsample.md) | Local MATLAB helper returning input(1:factor:end,:), taking every factor-th row while preserving columns. | documented |
| [`print_message`](print_message.md) | Prints a local HH:mm:ss timestamp and message to the command window; no return value or log file write. | documented |
| [`record_synced_video`](record_synced_video.md) | Configures a PointGrey capture device, previews it, writes a grayscale AVI at path.avi, and returns [tStart,tEnd] Unix timestamps surrounding acquisition. | needs review |
| [`show_camera_formats`](show_camera_formats.md) | Prints supported format strings and the device name; no explicit output. | needs review |
| [`varforce_drive`](varforce_drive.md) | Builds six-channel voltage and final-degauss matrices, calls DACoperator, and returns params_out with sent_signal, start_time, and dominant_coil added. | needs review |
| [`varforce_drive_synced_gui.createComponents`](varforce_drive_synced_gui.createComponents.md) | Creates the figure, panels, labels, text inputs, dropdowns, checkboxes, buttons, and callback registrations. | documentation in progress |
| [`varforce_drive_synced_gui.degauss_now_button_Callback`](varforce_drive_synced_gui.degauss_now_button_Callback.md) | Builds a fixed 5/0 V sequence for PCIe-6738, reads degauss/pole settings, calls varforce_drive, and pauses for params.duration. | needs review |
| [`varforce_drive_synced_gui.delete`](varforce_drive_synced_gui.delete.md) | Lifecycle method deleting the app figure; no explicit output. | documentation in progress |
| [`varforce_drive_synced_gui.edit_pulsewidths_Callback`](varforce_drive_synced_gui.edit_pulsewidths_Callback.md) | Parses pulse-width text and sequence count and computes totalDuration. | incomplete |
| [`varforce_drive_synced_gui.edit_sequences_Callback`](varforce_drive_synced_gui.edit_sequences_Callback.md) | Parses pulse widths/sequence count and updates text_expt_duration.Text with their product. | needs review |
| [`varforce_drive_synced_gui.pushbutton_close_Callback`](varforce_drive_synced_gui.pushbutton_close_Callback.md) | Calls delete(app), closing the app figure. | documentation in progress |
| [`varforce_drive_synced_gui.pushbutton_start_Callback`](varforce_drive_synced_gui.pushbutton_start_Callback.md) | Reads GUI parameters, optionally performs an initial degauss call, ensures a parallel pool exists, and optionally saves metadata. | incomplete |
| [`varforce_drive_synced_gui.varforce_drive_gui_OpeningFcn`](varforce_drive_synced_gui.varforce_drive_gui_OpeningFcn.md) | Moves the figure onscreen, converts arguments into GUIDE-compatible handles, stores the output handle, and calls guidata. | documentation in progress |
| [`varforce_drive_synced_gui.varforce_drive_synced_gui`](varforce_drive_synced_gui.varforce_drive_synced_gui.md) | Constructor returning the new or existing singleton app. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

DACoperator <DACoperator>
downsample <downsample>
print_message <print_message>
record_synced_video <record_synced_video>
show_camera_formats <show_camera_formats>
varforce_drive <varforce_drive>
varforce_drive_synced_gui.createComponents <varforce_drive_synced_gui.createComponents>
varforce_drive_synced_gui.degauss_now_button_Callback <varforce_drive_synced_gui.degauss_now_button_Callback>
varforce_drive_synced_gui.delete <varforce_drive_synced_gui.delete>
varforce_drive_synced_gui.edit_pulsewidths_Callback <varforce_drive_synced_gui.edit_pulsewidths_Callback>
varforce_drive_synced_gui.edit_sequences_Callback <varforce_drive_synced_gui.edit_sequences_Callback>
varforce_drive_synced_gui.pushbutton_close_Callback <varforce_drive_synced_gui.pushbutton_close_Callback>
varforce_drive_synced_gui.pushbutton_start_Callback <varforce_drive_synced_gui.pushbutton_start_Callback>
varforce_drive_synced_gui.varforce_drive_gui_OpeningFcn <varforce_drive_synced_gui.varforce_drive_gui_OpeningFcn>
varforce_drive_synced_gui.varforce_drive_synced_gui <varforce_drive_synced_gui.varforce_drive_synced_gui>
```
