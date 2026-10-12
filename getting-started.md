# Using this reference

HillLab combines assay-specific processing with smaller tools for paths, plots,
videos, tables, and tracking data. The [package reference](api/hilllab/index.md)
follows the source folders. Each function has its own page, including methods and
named callbacks. Folder guides list the functions directly and explain their
classes, configuration, and supporting resources.

## Find the right tool

Start with the assay folder, then choose a function from its list. For general
tasks, inspect [utilities](api/hilllab/utilities/index.md) and
[visual](api/hilllab/visual/index.md). Search accepts function names, parameter
names, and terms such as *VRPN*, *radius*, or *FFCA*.

A leading underscore marks an **internal helper**. These pages are included so
contributors can reuse or understand existing components, but their interfaces
are coupled to the parent workflow. A **nested callback/helper** is defined
inside another function; its dotted documentation name does not make it a
separately importable attribute. Class profiles and initial attributes are
included on the corresponding folder guide.

## Read a function page

- **Signature:** the actual argument names and defaults in the supplied code.
  Arguments without defaults are required; named arguments make assay settings
  easier to audit. `**kwargs` accepts additional named options, whose forwarding
  or ignored behavior is explained on the page.
- **Description and usage:** what is calculated, which layouts and units are
  expected, what is saved or changed, and practical constraints.
- **Inputs:** descriptions from the docstring, expanded where the code establishes
  additional behavior. A `DataFrame` is a labelled table: column names and row
  ordering are often part of the assay contract. A NumPy array is numeric data
  organized by dimensions such as frame, particle, or channel.
- **Returns and side effects:** output types, tuple order, saved files, and object
  changes described in prose. `None` often means
  a routine writes files, displays plots, or mutates a bundle instead of returning
  the result. A generator produces values as you iterate rather than one complete
  list at the initial call.
- **Source:** a link to the implementation and its file/line location, for readers
  who want to inspect or extend the code. Full implementations and raw docstrings
  are kept out of the guide.

Some routines deliberately ask for console input or open desktop windows. Passing
explicit paths avoids a file-selection dialog where supported, but does not remove
every confirmation prompt. Use a documented bypass option only when the function
actually provides one. File creation, overwriting, logging, clipboard copying,
and changes to global plotting/warning settings are called out in the usage notes.

## Status banners

**Incomplete feature — in progress** means the advertised operation is a stub or
is explicitly unimplemented. **Implementation needs review** identifies a
specific observed mismatch, unresolved path/import, calculation limitation, or
unimplemented option. **Source documentation in progress** means the original
docstring lacks a full contract; the reference supplies code-derived descriptions.
The [status index](reference-status.md) gathers these pages.

These are static source-review findings, not results from running assays. A page
without a warning is not an experimental validation claim. No missing algorithm,
measurement unit, dataset layout, or physiological interpretation has been supplied
by guesswork.

## Imports and installation

The supplied `pyproject.toml` declares package version **1.2.260612.1**, Python
**>=3.10**, and a mix of pinned dependencies. That metadata alone does not establish
that every declared dependency is available for every Python version/platform.
Choose an environment compatible with the scientific packages before installing
the package. The documentation's Python 3.14 environment builds static pages only;
it does not install or test HillLab's runtime dependencies.

The usual explicit import pattern is:

```python
# General import pattern, after package import issues are resolved:
from hilllab.utilities.format_duration import format_duration

duration_text = format_duration(125)
```

:::{warning} Current package import blocker
`hilllab/__init__.py` imports autotracker immediately. The supplied
`autotrack_videos.py` imports `._generate_new_VRPN`, but the local source filename
is `_generate_new_vrpn.py`; the body then calls `_generate_vrpn` without importing
that name. A normal `import hilllab` or submodule import can therefore fail before
the requested utility is reached. This reference documents the current code and
does not repair it. See the
[autotracker page](api/hilllab/autotracker/autotrack_videos.md).
:::

TensorFlow/Keras model tools, pandas HDF operations, document parsers, Seaborn
plots, and pytest tests need packages not all declared in the project's dependency
list. Read the relevant function and folder notes before using an optional
subsystem; consult its source imports for the exact dependencies. Desktop
Tk/OpenCV routines also require a usable GUI.
The compiled FFT processor is supplied as a Windows executable with native DLLs;
the MATLAB routines require their own MATLAB/toolbox/hardware environment.

## Data layouts and units

- Standard VRPN MAT exports contain ten tracking columns. Event MAT files contain
  nine; functions expecting `microseconds` may not accept the latter.
- Bead-classification HDF loaders use `summary`, `positions`, and `metadata`.
  Dynamics HDF writers use `summary`, `instantaneous`, and `metadata`. These are
  related but distinct contracts; do not substitute one merely because both are HDF.
- Migration and swelling tables stack reads in **16-row blocks**, often with
  repeated A–P labels and `Column N` names. Read indices in helpers are usually
  zero-based; some endpoint interfaces convert requested elapsed time differently.
- FFCA calculators return a **fraction from 0 to 1**, while binding plots calculate
  percentages. Probe radius versus diameter and nm/µm/m conversions matter when
  invoking the Stokes–Einstein or calibration routines.
- Pixel/frame inputs are not automatically physical measurements. Read the
  calibration and frequency warnings on affected motion-analysis pages before
  interpreting outputs as µm, seconds, Hz, or force.

## Reproducibility

The reference describes the supplied local source on **October 12, 2026**, based
on revision `cc6789a0a8a3420c23f972ac041412275e7aa47a` plus the existing local
autotracker edits. Source links use that immutable revision except for the two
locally changed files, which are labelled as working-tree versions. The
[coverage page](coverage.md) lists what was documented. Recheck source behavior
when the code changes; these Markdown pages are an authored snapshot.
