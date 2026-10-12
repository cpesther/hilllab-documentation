# hilllab.dynamics

Calculate bead motion statistics from VRPN tracking data, assign identifiers/groups, classify motion, and prepare HDF results.

## Subfolders

| Group | Purpose |
| --- | --- |
| [plot](plot/index.md) | Visualize motion statistics and bead counts using the PARAMETERS display/units registry. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_calculate_AFV`](batch_calculate_AFV.md) | For every summary UUID, loads instantaneous rows, looks up its source fps, computes AFV metrics, and writes `<stem>.afv.h5` with key afv. | documented |
| [`batch_primary_analysis`](batch_primary_analysis.md) | Recursively analyzes `.vrpn.mat` files with shared fps and pixel_width calibrations. | needs review |
| [`calculate_AFV`](calculate_AFV.md) | Returns a dictionary of three amplitude measures, peak-selected frequency, and up/down mean/median speeds from one bead's pca and speed columns. | needs review |
| [`classify_batch`](classify_batch.md) | With method gmm, copies the source HDF to `<stem>.classify.h5`, replaces its summary table with mixture labels, and returns None. | needs review |
| [`classify_GMM`](classify_GMM.md) | Standardizes six summary features, fits a three-component Gaussian mixture, and returns `(summary_with_labels_and_weights, pivot_or_None)`. | needs review |
| [`compile_primary_analysis`](compile_primary_analysis.md) | Recursively reads HDF summary/instantaneous/metadata tables and concatenates each. | needs review |
| [`create_groups`](create_groups.md) | Reads summary identifiers and writes a collision-safe `.groups.json` template, distributing unique IDs into five example groups. | documented |
| [`create_identifiers`](create_identifiers.md) | Returns None after writing a copied sibling `<stem>.identify.h5` with an updated summary table. | needs review |
| [`dynamics_pipeline`](dynamics_pipeline.md) | Takes no arguments and returns None. | incomplete |
| [`inspect_h5`](inspect_h5.md) | Returns None after printing summary-row count, distinct VRPN source paths, parent-folder count, and presence of identifier/classification columns. show_parents=True also lists each source parent directory. | documented |
| [`primary_analysis`](primary_analysis.md) | Returns `(summary, instantaneous, metadata)` from one VRPN file, or `(None, None, None)` for an empty tracking array. fps converts frames to seconds; pixel_width scales XY into the requested physical units. | needs review |
| [`test_create_identifiers`](test_create_identifiers.md) | Samples seven summary paths, previews identifiers, and asks whether to extract/print all unique identifiers. | documented |

## Internal helpers

| Function | Purpose | Status |
| --- | --- | --- |
| [`_identifier_from_path`](_identifier_from_path.md) | Returns the substring after the last occurrence of split1 and before the first following split2. | documented |
| [`_load_with_groups`](_load_with_groups.md) | Returns a summary DataFrame with a group column. | documented |
```{toctree}
:hidden:
:maxdepth: 1

plot <plot/index>
_identifier_from_path <_identifier_from_path>
_load_with_groups <_load_with_groups>
batch_calculate_AFV <batch_calculate_AFV>
batch_primary_analysis <batch_primary_analysis>
calculate_AFV <calculate_AFV>
classify_batch <classify_batch>
classify_GMM <classify_GMM>
compile_primary_analysis <compile_primary_analysis>
create_groups <create_groups>
create_identifiers <create_identifiers>
dynamics_pipeline <dynamics_pipeline>
inspect_h5 <inspect_h5>
primary_analysis <primary_analysis>
test_create_identifiers <test_create_identifiers>
```
