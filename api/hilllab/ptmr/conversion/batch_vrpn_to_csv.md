# batch_vrpn_to_csv

[Folder overview](index.md)

## Signature

```{py:function} batch_vrpn_to_csv(folder)
:module: hilllab.ptmr.conversion.batch_vrpn_to_csv
:canonical: hilllab.ptmr.conversion.batch_vrpn_to_csv.batch_vrpn_to_csv
```

## Behavior and usage

Recursively finds complete suffixes `.vrpn.mat` and `.vrpn.evt.evt.mat`, converts each through vrpn_to_csv, prints progress, and returns None. Individual conversions use the default skip-existing behavior. No calibration or drift calculation is performed.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `folder` | `required` | **string**. the path to the folder containing CSVs. |

## Returns and side effects

Recursively finds complete suffixes `.vrpn.mat` and `.vrpn.evt.evt.mat`, converts each through vrpn_to_csv, prints progress, and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.ptmr.conversion.vrpn_to_csv.vrpn_to_csv`](vrpn_to_csv.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../../utilities/print_progress_bar.md)
- [`hilllab.utilities.walk_dir.walk_dir`](../../utilities/walk_dir.md)

## Source

`hilllab/ptmr/conversion/batch_vrpn_to_csv.py`, lines 6–26 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/conversion/batch_vrpn_to_csv.py#L6-L26)
