# vrpn_to_csv

[Folder overview](index.md)

## Signature

```{py:function} vrpn_to_csv(path, skip_existing=True)
:module: hilllab.ptmr.conversion.vrpn_to_csv
:canonical: hilllab.ptmr.conversion.vrpn_to_csv.vrpn_to_csv
```

## Behavior and usage

Exports raw tracking columns into sibling `<first-stem>.track.csv` for standard VRPNs or `<first-stem>.drift.track.csv` for event VRPNs; returns None. Existing files can be skipped. Dots in the base filename are discarded after the first stem fragment, so different inputs can share a destination. Unsupported suffixes leave csv_path undefined.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the path to the VRPN file |
| `skip_existing` | `True` | **bool**. when True, any CSVs that already exist  will be bypassed during conversion so as not to create duplicate CSV files for the same VRPN. |

## Returns and side effects

Exports raw tracking columns into sibling `<first-stem>.track.csv` for standard VRPNs or `<first-stem>.drift.track.csv` for event VRPNs; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.load_vrpn.load_vrpn`](../../utilities/load_vrpn.md)

## Source

`hilllab/ptmr/conversion/vrpn_to_csv.py`, lines 7–50 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/ptmr/conversion/vrpn_to_csv.py#L7-L50)
