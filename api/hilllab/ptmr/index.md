# hilllab.ptmr

Particle-tracking microrheology utilities for conversion, calibration, drift handling, and MSD. Several pipeline/fit functions are explicit stubs.

## Subfolders

| Group | Purpose |
| --- | --- |
| [conversion](conversion/index.md) | Convert legacy MATLAB VRPN arrays into CSV tracking tables without applying physical calibration. |
| [drift](drift/index.md) | Linear XY drift subtraction. The current implementation has unresolved defects and is marked for review. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_subtract_drift`](batch_subtract_drift.md) | Loops over explicit file paths and is intended to write sibling `.drift.track.csv` files for the Python pipeline. | needs review |
| [`calculate_bead_msd`](calculate_bead_msd.md) | Intended return is `(ensemble_msd, msd)`: a per-lag ensemble mean/std/time table and a transposed individual-bead MSD table indexed by lag time seconds. | needs review |
| [`calculate_ensemble_moduli`](calculate_ensemble_moduli.md) | Accepts files but currently executes only pass and returns None. | incomplete |
| [`fit_fbm`](fit_fbm.md) | Takes no arguments and returns None because its only implementation statement is pass. | incomplete |
| [`load_tracking_data`](load_tracking_data.md) | The MATLAB branch loads a VRPN and intends to return a formatted, physically scaled tracking DataFrame. | needs review |
| [`process_vrpns`](process_vrpns.md) | Accepts folder/calibration/processing options but the body is pass, returning None. | incomplete |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_format_vrpn`](_format_vrpn.md) | Mutates and returns the same tracking DataFrame: replaces timestamps with frame/fps seconds, drops microseconds, sorts particle_id/frame, and converts x/y/z using camera sensor pixel width divided by magnification. | documented |
```{toctree}
:hidden:
:maxdepth: 1

conversion <conversion/index>
drift <drift/index>
_format_vrpn <_format_vrpn>
batch_subtract_drift <batch_subtract_drift>
calculate_bead_msd <calculate_bead_msd>
calculate_ensemble_moduli <calculate_ensemble_moduli>
fit_fbm <fit_fbm>
load_tracking_data <load_tracking_data>
process_vrpns <process_vrpns>
```
