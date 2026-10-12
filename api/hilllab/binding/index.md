# hilllab.binding

Count bead contours in paired bound/runoff images and summarize binding-assay measurements.

## Subfolders

| Group | Purpose |
| --- | --- |
| [masks](masks/index.md) | Image masks used before contour detection. |
| [plot](plot/index.md) | Plots and shared table handling for bead binding results. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`count_beads`](count_beads.md) | Requires bound/runoff subfolders, detects contours after circular masking, Gaussian blur, and Otsu thresholding, and classifies contour area into small/expected/large. | needs review |
```{toctree}
:hidden:
:maxdepth: 1

masks <masks/index>
plot <plot/index>
count_beads <count_beads>
```
