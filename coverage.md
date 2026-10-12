# Reference coverage

The guide is organized by **source folders and functions**, with no landing page per source file. Every locally defined function, helper, method, and named callback has a separate page. Class descriptions, configuration, notebooks, and supporting resources are included in their folder guides.

- 33 folder guides.
- 212 unique Python function/method pages covering 215 definitions; three branch-specific generator pairs share their function pages.
- 18 supporting MATLAB/C# callable pages.
- 10 Python class profiles within folder guides.
- 192 Python source files reviewed.

## Folder guides

| Group | Function pages |
| --- | --- |
| [hilllab.autotracker](api/hilllab/autotracker/index.md) | 7 |
| [hilllab.beads.eval](api/hilllab/beads/eval/index.md) | 9 |
| [hilllab.beads](api/hilllab/beads/index.md) | 21 |
| [hilllab.binding](api/hilllab/binding/index.md) | 1 |
| [hilllab.binding.masks](api/hilllab/binding/masks/index.md) | 1 |
| [hilllab.binding.plot](api/hilllab/binding/plot/index.md) | 4 |
| [hilllab.cilia.FFTProcessor](api/hilllab/cilia/FFTProcessor/index.md) | 2 |
| [hilllab.cilia.comparison](api/hilllab/cilia/comparison/index.md) | 2 |
| [hilllab.cilia](api/hilllab/cilia/index.md) | 6 |
| [hilllab.cilia.verification](api/hilllab/cilia/verification/index.md) | 0 |
| [hilllab.drives](api/hilllab/drives/index.md) | 7 |
| [hilllab.dynamics](api/hilllab/dynamics/index.md) | 14 |
| [hilllab.dynamics.plot](api/hilllab/dynamics/plot/index.md) | 2 |
| [hilllab](api/hilllab/index.md) | 0 |
| [hilllab.indexer](api/hilllab/indexer/index.md) | 10 |
| [hilllab.indexer.menus](api/hilllab/indexer/menus/index.md) | 1 |
| [hilllab.indexer.menus.menu_utilities](api/hilllab/indexer/menus/menu_utilities/index.md) | 6 |
| [hilllab.indexer.parsers](api/hilllab/indexer/parsers/index.md) | 11 |
| [hilllab.interfaces](api/hilllab/interfaces/index.md) | 0 |
| [hilllab.magnets.gui](api/hilllab/magnets/gui/index.md) | 15 |
| [hilllab.magnets](api/hilllab/magnets/index.md) | 6 |
| [hilllab.migration.cleaning](api/hilllab/migration/cleaning/index.md) | 2 |
| [hilllab.migration.gui](api/hilllab/migration/gui/index.md) | 3 |
| [hilllab.migration](api/hilllab/migration/index.md) | 37 |
| [hilllab.ptmr.conversion](api/hilllab/ptmr/conversion/index.md) | 2 |
| [hilllab.ptmr.drift](api/hilllab/ptmr/drift/index.md) | 1 |
| [hilllab.ptmr](api/hilllab/ptmr/index.md) | 7 |
| [hilllab.swelling](api/hilllab/swelling/index.md) | 5 |
| [hilllab.tests](api/hilllab/tests/index.md) | 1 |
| [hilllab.utilities.gui](api/hilllab/utilities/gui/index.md) | 6 |
| [hilllab.utilities](api/hilllab/utilities/index.md) | 25 |
| [hilllab.visual](api/hilllab/visual/index.md) | 14 |
| [hilllab.widgets](api/hilllab/widgets/index.md) | 2 |

## Review basis

The reference describes the supplied local snapshot of HillLab, based on revision `cc6789a0a8a3420c23f972ac041412275e7aa47a` plus the existing autotracker working-tree changes. Behavior was established from docstrings and static code review. The documentation build does not import HillLab, run assays, operate hardware, or execute notebook cells.

Source links lead to the reviewed repository revision. Locally changed/unpublished source files are labelled as such on their function pages. Compiled assets are inventoried without claiming that they match a particular source revision.

The [status index](reference-status.md) gathers source-documentation and implementation flags. The [machine-readable coverage inventory](_static/reference-coverage.json) retains source paths, definition lines, and guide locations for maintenance.
