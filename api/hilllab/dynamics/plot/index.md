# hilllab.dynamics.plot

Visualize motion statistics and bead counts using the PARAMETERS display/units registry.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`bead_counts`](bead_counts.md) | Counts unique particle_id values per category/source path, then displays cumulative totals or per-video boxplots. | needs review |
| [`plot_parameter`](plot_parameter.md) | Checks the parameter against the PARAMETERS registry, loads group assignments, and displays a boxplot by group or identifier. | needs review |

## Parameter names and units

The PARAMETERS registry supplies plotting labels and units. Labels are display metadata, not proof that a calculation has applied those units; check warnings on the analysis function.

| Parameter | Display name | Declared units |
| --- | --- | --- |
| `birth_frame` | Birth Frame | frame |
| `death_frame` | Death Frame | frame |
| `birth_seconds` | Birth Time | s |
| `death_seconds` | Death Time | s |
| `lifetime_frames` | Lifetime (Frames) | frame |
| `lifetime_range_frames` | Lifetime Range (Frames) | frame |
| `lifetime_seconds` | Lifetime | s |
| `lifetime_range_seconds` | Lifetime Range | s |
| `life_fraction_alive` | % of Lifetime Tracked | % of frames |
| `total_fraction_alive` | % of Video Tracked | % of frames |
| `birth_x` | Birth X Position | µm |
| `birth_y` | Birth Y Position | µm |
| `death_x` | Death X Position | µm |
| `death_y` | Death Y Position | µm |
| `mean_x` | Mean X Position | µm |
| `mean_y` | Mean Y Position | µm |
| `median_x` | Median X Position | µm |
| `median_y` | Median Y Position | µm |
| `std_x` | X Position Standard Deviation | µm |
| `std_y` | Y Position Standard Deviation | µm |
| `min_x` | Minimum X Position | µm |
| `min_y` | Minimum Y Position | µm |
| `max_x` | Maximum X Position | µm |
| `max_y` | Maximum Y Position | µm |
| `range_x` | X Range | µm |
| `range_y` | Y Range | µm |
| `displacement` | Displacement | µm |
| `path_length` | Path Length | µm |
| `straightness` | Straightness | Unitless / not specified |
| `rg` | Radius of Gyration | µm |
| `max_distance` | Max Distance | µm |
| `mean_heading` | Mean Heading | degrees |
| `median_heading` | Median Heading | degrees |
| `std_heading` | Heading Standard Deviation | degrees |
| `min_heading` | Minimum Heading | degrees |
| `max_heading` | Maximum Heading | degrees |
| `circular_variance` | Circular Variance | Unitless / not specified |
| `mean_angle` | Mean Angle | degrees |
| `median_angle` | Median Angle | degrees |
| `std_angle` | Angle Standard Deviation | degrees |
| `min_angle` | Minimum Angle | degrees |
| `max_angle` | Maximum Angle | degrees |
| `mean_speed` | Mean Speed | µm/s |
| `median_speed` | Median Speed | µm/s |
| `std_speed` | Speed Standard Deviation | µm/s |
| `min_speed` | Minimum Speed | µm/s |
| `max_speed` | Maximum Speed | µm/s |
| `mean_acceleration` | Mean Acceleration | µm/s² |
| `median_acceleration` | Median Acceleration | µm/s² |
| `std_acceleration` | Acceleration Standard Deviation | µm/s² |
| `min_acceleration` | Minimum Acceleration | µm/s² |
| `max_acceleration` | Maximum Acceleration | µm/s² |
| `linearity` | Linearity | Unitless / not specified |
| `bb_area` | Bounding Box Area | µm² |
| `alignment_deg` | Alignment | degrees |
| `alignment_rad` | Alignment | radians |
| `alignment_strength` | Alignment Strength | Unitless / not specified |
| `path` | Path | Unitless / not specified |
| `uuid` | UUID | Unitless / not specified |
| `identifier` | Identifier | Unitless / not specified |
| `classification` | Classification | Unitless / not specified |
| `stuck_classification_weight` | Stuck Classification Weight | Unitless / not specified |
| `oscillating_classification_weight` | Oscillating Classification Weight | Unitless / not specified |
| `transiting_classification_weight` | Transiting Classification Weight | Unitless / not specified |
| `group` | Group | Unitless / not specified |
| `amplitude_abs` | Amplitude (absolute) | µm |
| `amplitude_mean` | Amplitude (mean) | µm |
| `amplitude_quar` | Amplitude (quartile) | µm |
| `frequency` | Frequency | Hz |
| `velocity_up_mean` | Velocity Up (mean) | µm/s |
| `velocity_down_mean` | Velocity Up (mean) | µm/s |
| `velocity_up_med` | Velocity Up (median) | µm/s |
| `velocity_down_med` | Velocity Up (median) | µm/s |

```{toctree}
:hidden:
:maxdepth: 1

bead_counts <bead_counts>
plot_parameter <plot_parameter>
```
