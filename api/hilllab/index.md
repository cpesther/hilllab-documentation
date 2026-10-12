# hilllab

Scientific computing tools for Hill Lab assays, image and video processing, particle trajectories, and experimental data handling.

## Subfolders

| Group | Purpose |
| --- | --- |
| [autotracker](autotracker/index.md) | Track bead-like features in videos with TrackPy and export MATLAB-compatible VRPN trajectories. |
| [beads](beads/index.md) | Inspect and label bead trajectories, prepare TensorFlow datasets, and build motion classifiers. |
| [binding](binding/index.md) | Count bead contours in paired bound/runoff images and summarize binding-assay measurements. |
| [cilia](cilia/index.md) | Estimate ciliary beat frequency (CBF) and fractional functional ciliated area (FFCA) from temporal image spectra. |
| [drives](drives/index.md) | Scan filesystem metadata into an SQLite database using the DBConnection wrapper and packaged SQL schema. |
| [dynamics](dynamics/index.md) | Calculate bead motion statistics from VRPN tracking data, assign identifiers/groups, classify motion, and prepare HDF results. |
| [indexer](indexer/index.md) | A separate SQLAlchemy-based document/file index with format-specific text parsers and experimental terminal menus. |
| [interfaces](interfaces/index.md) | Notebook interfaces that select paths and invoke the existing autotracker functions. |
| [magnets](magnets/index.md) | Track beads in 3DFM calibration videos, align voltage schedules, and fit provisional force-distance relationships. |
| [migration](migration/index.md) | Plate-reader migration analysis: load and clean spatial profiles, fit diffusion-like Gaussian curves, calibrate radii, and report results. |
| [ptmr](ptmr/index.md) | Particle-tracking microrheology utilities for conversion, calibration, drift handling, and MSD. Several pipeline/fit functions are explicit stubs. |
| [swelling](swelling/index.md) | Two-channel plate-reader swelling analysis using spatial fluorescence integrals and grouped time courses. |
| [tests](tests/index.md) | Existing source-repository tests, documented for contributors rather than as assay workflows. |
| [utilities](utilities/index.md) | Reusable path, file, formatting, plotting, logging, and data-cleaning helpers. |
| [visual](visual/index.md) | OpenCV video conversion, editing, binning, frame extraction, brightness handling, and camera calibration lookup. |
| [widgets](widgets/index.md) | Notebook buttons for opening paths in the kernel machine's native file browser. |
```{toctree}
:hidden:
:maxdepth: 1

autotracker <autotracker/index>
beads <beads/index>
binding <binding/index>
cilia <cilia/index>
drives <drives/index>
dynamics <dynamics/index>
indexer <indexer/index>
interfaces <interfaces/index>
magnets <magnets/index>
migration <migration/index>
ptmr <ptmr/index>
swelling <swelling/index>
tests <tests/index>
utilities <utilities/index>
visual <visual/index>
widgets <widgets/index>
```
