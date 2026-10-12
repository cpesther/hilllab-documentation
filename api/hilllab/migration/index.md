# hilllab.migration

Plate-reader migration analysis: load and clean spatial profiles, fit diffusion-like Gaussian curves, calibrate radii, and report results.

## Subfolders

| Group | Purpose |
| --- | --- |
| [cleaning](cleaning/index.md) | Background-shifting and peak-repositioning primitives for migration profiles. |
| [gui](gui/index.md) | Desktop Tk interfaces for assigning capillary groups, radii, and calibration viscosities. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`D`](D.md) | Returns diffusion coefficient in m²/s from temperature_K, viscosity eta_mPas in mPa·s, and radius_nm in nm using the Stokes–Einstein formula. | documented |
| [`eta`](eta.md) | Returns viscosity in mPa·s from Kelvin temperature, diffusion in m²/s, and radius in nm. | documented |
| [`load_file`](load_file.md) | Returns a Bundle with raw plate data and overflow metadata. | needs review |
| [`plate_calibrate_results`](plate_calibrate_results.md) | Mutates and returns a Bundle. | documented |
| [`plate_define_radii`](plate_define_radii.md) | Returns a `Column N`→radius mapping. radius_nm may be scalar, a list assigned consecutively from column 1, or multi for interactive entry. | needs review |
| [`plate_endpoint_calculation`](plate_endpoint_calculation.md) | Returns a DataFrame of eta, Dt, D, NRMSE, and peak amplitude for one read across cleaned columns. | needs review |
| [`plate_export_bundle`](plate_export_bundle.md) | Writes raw, normalized, cleaned, localization, radii, timing, group/calibration, overflow, and preparation metadata sheets to `<stem>.bundle.xlsx`; returns None. | needs review |
| [`plate_extract_result`](plate_extract_result.md) | Returns mean, median, weighted_mean, maximum, or minimum of a `Column N` result series. table selects eta/D/eta_calib/D_calib/Dt/nrmse/peak; end_only uses the final end_hours converted to read count. | needs review |
| [`plate_generate_report`](plate_generate_report.md) | Generates a formatted REPORT Excel workbook and returns None. | needs review |
| [`plate_inspect`](plate_inspect.md) | Draws raw curves by read for 24 or 32 columns and returns None. | needs review |
| [`plate_kinetic_calculation`](plate_kinetic_calculation.md) | Resets and fills plate_eta/Dt/D/nrmse/peak result tables for every zero-based read, then returns the mutated Bundle. | documentation in progress |
| [`plate_optimize_gaussian`](plate_optimize_gaussian.md) | Returns a dictionary with eta (mPa·s), Dt (m²), D (m²/s), NRMSE, and Peak (fitted amplitude). | needs review |
| [`plate_relative_kinetic_calculation`](plate_relative_kinetic_calculation.md) | First performs kinetic fitting, then derives pairwise D from `(Dt2-Dt1)/(2*(t2-t1))` for read separations strictly greater than read_gap. | needs review |
| [`plate_split_channels`](plate_split_channels.md) | Reads a UTF-16 SpectraMax export, separates numbered channel columns, and writes one `<excitation>nm_<stem>.xlsx` file per extracted channel. | needs review |
| [`r`](r.md) | Returns radius in nm from Kelvin temperature, diffusion in m²/s, and viscosity in mPa·s. | documented |
| [`T`](T.md) | Returns temperature in Kelvin from diffusion in m²/s, viscosity in mPa·s, and radius in nm. | documented |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_plate_calculate_gaussian`](_plate_calculate_gaussian.md) | Accepts `(A, Dt)` and a curve, evaluates `A*exp(-(x-delta_x_m)^2/(2*Dt))`, and returns normalized RMSE, or `(nrmse, fit_curve)` when return_fit=True. x spacing is in meters, Dt in m², and fitting errors use indices 1 through end_index-1. | documented |
| [`_plate_format_extended`](_plate_format_extended.md) | Returns 32 columns per 16-row read by preserving the first 12 rows of 24 columns, padding them, and converting original rows M–P into eight 12-value pseudo-columns. | documentation in progress |
| [`_plate_load_wrapper`](_plate_load_wrapper.md) | Loads and prepares a migration Bundle, or offers to reuse a sibling `.1dpre.xlsx` saved bundle through console input. | documented |
| [`_plate_prepare_data`](_plate_prepare_data.md) | Mutates and returns a bundle after selecting one-based columns, assigning radii/timing, normalizing each curve, localizing peaks/ranges, shifting peaks and background, and saving a preprocessing workbook. | needs review |
| [`_plate_profile_curve`](_plate_profile_curve.md) | Returns `(peak_index, end_index)` for a nominal 16-point curve using candidate peaks 0–4, bounded Gaussian fits over the first eight points, and empirical penalties. | needs review |
| [`_plate_remove_overflows`](_plate_remove_overflows.md) | Returns `(no_overflow_data, overflow_meta)`, replacing values whose string contains any alphabetic character with the first following nonalphabetic token within ten rows, or zero. | needs review |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`_plate_profile_curve.gaussian`](_plate_profile_curve.gaussian.md) | Closure-local model returning `a*exp(-(x-mu)^2/(2*sigma^2))` for array x and scalar amplitude/center/width. | documentation in progress |
| [`Bundle.__init__`](Bundle.__init__.md) | Takes no arguments, creates fresh Data and Results objects, and returns None. | documentation in progress |
| [`Bundle.__repr__`](Bundle.__repr__.md) | Returns a multiline string containing the source path and presence flags from contents(); does not itself print. | documentation in progress |
| [`Bundle._load_read`](Bundle._load_read.md) | Returns a 16-row DataFrame slice for zero-based read_number. type raw selects raw, normalized selects normalized, and all other values—including clean—select clean. | documented |
| [`Bundle.contents`](Bundle.contents.md) | Returns a dictionary of six Boolean presence indicators: Normalization, Localization, Radii, Results, Calibration, Groups. | documentation in progress |
| [`Bundle.show`](Bundle.show.md) | Prints the representation and conditions/groups/radii/calibration tables; returns None. | needs review |
| [`Data.__init__`](Data.__init__.md) | Creates empty/default state and returns None. | documentation in progress |
| [`Data.show_calibration`](Data.show_calibration.md) | Prints the calibration-columns mapping and returns None. | documented |
| [`Data.show_conditions`](Data.show_conditions.md) | Prints current read count, timing, temperature, extended mode, and method metadata; returns None. | documented |
| [`Data.show_groups`](Data.show_groups.md) | Prints the current group mapping and returns None. | documented |
| [`Data.show_radii`](Data.show_radii.md) | Prints the radii mapping and returns None. | documented |
| [`plate_generate_report.colnum_to_letter`](plate_generate_report.colnum_to_letter.md) | Closure-local helper returning Excel letters for a one-based integer column index: 1→A, 26→Z, 27→AA. | documentation in progress |
| [`plate_generate_report.excel_row_cells`](plate_generate_report.excel_row_cells.md) | Closure-local helper returning a list of cell-address strings for num_cols consecutive columns at row_num, starting with one-based start_col_num. | documentation in progress |
| [`plate_generate_report.write_metric_formulas`](plate_generate_report.write_metric_formulas.md) | Closure-local helper modifying an openpyxl worksheet in place and returning None. | documentation in progress |
| [`Results.__init__`](Results.__init__.md) | Creates empty pandas result tables and an empty radii_nm_calib mapping; returns None. | documentation in progress |

## Classes and data containers

(class-bundle)=

### Bundle

```{py:class} Bundle
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Bundle
```

Container holding `.data` (a Data instance) and `.results` (a Results instance). It is created empty; load_file populates raw data, preparation adds cleaned/localized data, and calculation functions add result tables. Most migration functions mutate this object and return the same bundle, so preserve separate copies when comparing processing settings.

[Constructor arguments and defaults](Bundle.__init__.md).

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `data` | Not specified | Data container |
| `results` | Not specified | Results container |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py).

(class-data)=

### Data

```{py:class} Data
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Data
```

Stores raw/normalized/clean/average tables, localization and fit ranges, column radii, read timing, temperature, groups, and calibration definitions. Constructor values below are initial defaults, not measurements. Rows are stacked in 16-row read blocks; columns use `Column N` names.

[Constructor arguments and defaults](Data.__init__.md).

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `path` | Not specified | Empty text |
| `extended` | Not specified | False |
| `num_columns` | Not specified | 0 |
| `num_rows` | Not specified | 0 |
| `num_reads` | Not specified | 0 |
| `overflow_meta` | Not specified | Not yet set |
| `raw` | Not specified | Not yet set |
| `normalized` | Not specified | Not yet set |
| `clean` | Not specified | Not yet set |
| `average` | Not specified | Not yet set |
| `peaks_raw` | Not specified | Empty table |
| `peaks_final` | Not specified | Empty table |
| `ranges_raw` | Not specified | Empty table |
| `ranges_final` | Not specified | Empty table |
| `radii_nm` | Not specified | Not yet set |
| `interval_minutes` | Not specified | 15 |
| `delay_minutes` | Not specified | 0 |
| `load_rate_minutes` | Not specified | 1.5 |
| `temperature_K` | Not specified | 297 |
| `method` | Not specified | Empty text |
| `groups` | Not specified | Empty mapping |
| `calibration_columns` | Not specified | Empty mapping |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py).

(class-results)=

### Results

```{py:class} Results
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Results
```

Stores plate_eta, plate_Dt, plate_D, plate_nrmse, and plate_peak tables plus calibrated radius/viscosity/diffusion results. All start empty; the presence of a result object alone does not mean a calculation has run.

[Constructor arguments and defaults](Results.__init__.md).

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `plate_eta` | Not specified | Empty table |
| `plate_Dt` | Not specified | Empty table |
| `plate_D` | Not specified | Empty table |
| `plate_nrmse` | Not specified | Empty table |
| `plate_peak` | Not specified | Empty table |
| `radii_nm_calib` | Not specified | Empty mapping |
| `plate_eta_calib` | Not specified | Empty table |
| `plate_D_calib` | Not specified | Empty table |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py).

```{toctree}
:hidden:
:maxdepth: 1

cleaning <cleaning/index>
gui <gui/index>
_plate_calculate_gaussian <_plate_calculate_gaussian>
_plate_format_extended <_plate_format_extended>
_plate_load_wrapper <_plate_load_wrapper>
_plate_prepare_data <_plate_prepare_data>
_plate_profile_curve <_plate_profile_curve>
_plate_profile_curve.gaussian <_plate_profile_curve.gaussian>
_plate_remove_overflows <_plate_remove_overflows>
Bundle.__init__ <Bundle.__init__>
Bundle.__repr__ <Bundle.__repr__>
Bundle._load_read <Bundle._load_read>
Bundle.contents <Bundle.contents>
Bundle.show <Bundle.show>
D <D>
Data.__init__ <Data.__init__>
Data.show_calibration <Data.show_calibration>
Data.show_conditions <Data.show_conditions>
Data.show_groups <Data.show_groups>
Data.show_radii <Data.show_radii>
eta <eta>
load_file <load_file>
plate_calibrate_results <plate_calibrate_results>
plate_define_radii <plate_define_radii>
plate_endpoint_calculation <plate_endpoint_calculation>
plate_export_bundle <plate_export_bundle>
plate_extract_result <plate_extract_result>
plate_generate_report <plate_generate_report>
plate_generate_report.colnum_to_letter <plate_generate_report.colnum_to_letter>
plate_generate_report.excel_row_cells <plate_generate_report.excel_row_cells>
plate_generate_report.write_metric_formulas <plate_generate_report.write_metric_formulas>
plate_inspect <plate_inspect>
plate_kinetic_calculation <plate_kinetic_calculation>
plate_optimize_gaussian <plate_optimize_gaussian>
plate_relative_kinetic_calculation <plate_relative_kinetic_calculation>
plate_split_channels <plate_split_channels>
r <r>
Results.__init__ <Results.__init__>
T <T>
```
