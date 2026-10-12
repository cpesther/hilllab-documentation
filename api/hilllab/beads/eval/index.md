# hilllab.beads.eval

Evaluate bead-classification models and visualize predictions. Several relative imports and experiment-specific assumptions need review.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_evaluate`](batch_evaluate.md) | Calls the bead evaluate routine for each model, prints mean/std metrics, and returns three lists `(loss, accuracy, pseudo_r2)` rather than averaged scalars. | needs review |
| [`bead_traj`](bead_traj.md) | Plots one bead's XY trajectory and returns a Matplotlib Axes. | needs review |
| [`conf_matrix`](conf_matrix.md) | Displays averaged count and row-normalized confusion matrices across models; returns `None`. | documented |
| [`interpolate_roc`](interpolate_roc.md) | Displays one-vs-rest ROC curves interpolated onto 100 false-positive-rate values and returns `None`. | documented |
| [`load_models`](load_models.md) | Returns a list of successfully loaded immediate `.keras` files. | documented |
| [`performance_dist`](performance_dist.md) | Displays boxplots for a sequence of metric arrays with corresponding `keys`; returns `None`. | needs review |
| [`plot_ffca`](plot_ffca.md) | Displays an FFCA bar chart and returns `None`. | needs review |
| [`pred_ffca`](pred_ffca.md) | Returns `(avg_ffca, std_ffca, labels)` after predicting immediate `.h5` files and grouping filename prefixes by plate. | needs review |
| [`prediction_map`](prediction_map.md) | Predicts bead classes using param/position/summary features and displays pixel XY trajectories colored by `vocab`; returns `None`. | needs review |
```{toctree}
:hidden:
:maxdepth: 1

batch_evaluate <batch_evaluate>
bead_traj <bead_traj>
conf_matrix <conf_matrix>
interpolate_roc <interpolate_roc>
load_models <load_models>
performance_dist <performance_dist>
plot_ffca <plot_ffca>
pred_ffca <pred_ffca>
prediction_map <prediction_map>
```
