# HillLab documentation

**HillLab** provides scientific computing tools for laboratory assays, image and
video processing, particle trajectories, and experimental data handling.

Browse the guide by source folder, then go directly to a function. Folder pages
list their functions, helpers, methods, and callbacks with concise summaries.
Class descriptions and configuration details sit alongside those lists.

## Assay and analysis tools

| Folder | Focus |
| --- | --- |
| [autotracker](api/hilllab/autotracker/index.md) | Track features in videos and write VRPN trajectories |
| [beads](api/hilllab/beads/index.md) | Inspect, label, and classify bead motion |
| [binding](api/hilllab/binding/index.md) | Count bound/runoff bead contours and plot results |
| [cilia](api/hilllab/cilia/index.md) | Ciliary beat frequency and functional ciliated area |
| [dynamics](api/hilllab/dynamics/index.md) | Trajectory statistics, identifiers, grouping, and plots |
| [magnets](api/hilllab/magnets/index.md) | 3DFM tracking and calibration tools |
| [migration](api/hilllab/migration/index.md) | Plate-reader spatial profiles, diffusion fits, and reports |
| [ptmr](api/hilllab/ptmr/index.md) | Tracking conversion, drift, and MSD; unfinished features flagged |
| [swelling](api/hilllab/swelling/index.md) | Two-channel fluorescence integration and time courses |

## Tools for extending HillLab

| Folder | Focus |
| --- | --- |
| [utilities](api/hilllab/utilities/index.md) | Files, paths, plotting styles, tables, logs, and data cleaning |
| [visual](api/hilllab/visual/index.md) | Video editing, conversion, binning, frames, and camera metadata |
| [widgets](api/hilllab/widgets/index.md) | Notebook file-browser buttons |
| [drives](api/hilllab/drives/index.md) | SQLite filesystem metadata scanning |
| [indexer](api/hilllab/indexer/index.md) | Document text extraction and an experimental file index |
| [interfaces](api/hilllab/interfaces/index.md) | Existing autotracker notebooks |
| [tests](api/hilllab/tests/index.md) | Existing contributor test functions |

Read [Using this reference](getting-started.md) for calling conventions, input
layouts, status banners, and current import limitations. Internal helpers are
labelled; incomplete features and uncertain behavior appear in the
[documentation status index](reference-status.md).

```{toctree}
:maxdepth: 2
:hidden:

Using this reference <getting-started>
API reference <api/hilllab/index>
Status <reference-status>
Coverage <coverage>
```
