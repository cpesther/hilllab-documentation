# hilllab.beads

Inspect and label bead trajectories, prepare TensorFlow datasets, and build motion classifiers.

## Subfolders

| Group | Purpose |
| --- | --- |
| [eval](eval/index.md) | Evaluate bead-classification models and visualize predictions. Several relative imports and experiment-specific assumptions need review. |

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`classify_batch`](classify_batch.md) | Labels every UUID loaded from a bead HDF file as `s`→stuck, `t`→transiting, or `o`→oscillating. | documentation in progress |
| [`classify_bead`](classify_bead.md) | Interactively plots each bead starting at the zero-based `start` index and accumulates classification rows. | documentation in progress |
| [`classify_review`](classify_review.md) | Reads an existing labels workbook, selects rows whose classification equals `label`, and revisits their beads from `start`. | documented |
| [`data_preprocess`](data_preprocess.md) | Accepts one `(dataset, count)` tuple or a list of compatible tuples, encodes classes in order stuck/transiting/oscillating/discard, and returns `(train_ds, val_ds, test_ds)`. | needs review |
| [`evaluate`](evaluate.md) | Returns `(loss, accuracy, pseudo_r2)` and optionally plots training/validation history. | needs review |
| [`load_hdf`](load_hdf.md) | Returns `(groupby_summary, groupby_positions, df_metadata, bounds)` from `/summary`, `/positions`, and `/metadata` HDF keys. | documentation in progress |
| [`param_data`](param_data.md) | Returns `(dataset, count)` with six float32 features in fixed order: displacement, straightness, circular_variance, bb_area, mean_speed, mean_acceleration. | documented |
| [`param_model`](param_model.md) | Returns an uncompiled Keras Sequential classifier for six features: two 32-unit ReLU dense layers, dropout 0.5, and four-way softmax. | documentation in progress |
| [`plot_bead`](plot_bead.md) | Displays a four-view trajectory figure and returns `None`. | needs review |
| [`plot_component_trace`](plot_component_trace.md) | Plots x/y components of one bead against a sequential sample index and returns `None`. | needs review |
| [`plot_xy`](plot_xy.md) | Returns the Matplotlib Axes after drawing trajectories. | needs review |
| [`plot_xy_maximize`](plot_xy_maximize.md) | Displays origin-shifted bead trajectories separated into rows of six, using per-trajectory range times 1.3 for spacing; returns None. | needs review |
| [`position_data`](position_data.md) | Returns `(dataset, count)` of variable-length `(frames, 2)` float32 trajectories, centered by summary mean_x/mean_y. | documented |
| [`position_model`](position_model.md) | Returns an uncompiled variable-length XY classifier with zero masking, a 64-unit LSTM, two 32-unit ReLU dense layers, dropout 0.5, and four-way softmax. | documentation in progress |
| [`summary_data`](summary_data.md) | Returns `(dataset, count)` of 27 float32 summary values selected by positional slice `iloc[:, 28:55]`, optionally paired with string classifications. | documented |
| [`summary_model`](summary_model.md) | Returns an uncompiled classifier for 27 summary features with four 128-unit ReLU dense layers, dropout 0.5, and four-way softmax. | documentation in progress |
| [`train`](train.md) | Compiles the supplied model in place with Adam, sparse categorical cross-entropy, and sparse categorical accuracy, trains on the two datasets, and returns `(model, history)`. | documented |

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`data_preprocess.encode`](data_preprocess.encode.md) | Closure-local TensorFlow mapping callback returning `(features, integer_label)` from a feature object and classification string via the parent StringLookup layer. | documentation in progress |
| [`param_data.generator`](param_data.generator.md) | Branch-specific closure-local generator. | documentation in progress |
| [`position_data.generator`](position_data.generator.md) | Branch-specific local generator yielding centered XY trajectories, optionally paired with their classification strings. | documentation in progress |
| [`summary_data.generator`](summary_data.generator.md) | Branch-specific local generator yielding the first summary row's columns 28–54, optionally with a classification string. | documentation in progress |
```{toctree}
:hidden:
:maxdepth: 1

eval <eval/index>
classify_batch <classify_batch>
classify_bead <classify_bead>
classify_review <classify_review>
data_preprocess <data_preprocess>
data_preprocess.encode <data_preprocess.encode>
evaluate <evaluate>
load_hdf <load_hdf>
param_data <param_data>
param_data.generator <param_data.generator>
param_model <param_model>
plot_bead <plot_bead>
plot_component_trace <plot_component_trace>
plot_xy <plot_xy>
plot_xy_maximize <plot_xy_maximize>
position_data <position_data>
position_data.generator <position_data.generator>
position_model <position_model>
summary_data <summary_data>
summary_data.generator <summary_data.generator>
summary_model <summary_model>
train <train>
```
