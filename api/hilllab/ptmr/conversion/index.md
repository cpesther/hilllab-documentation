# hilllab.ptmr.conversion

Convert legacy MATLAB VRPN arrays into CSV tracking tables without applying physical calibration.

## Functions

| Function | Purpose | Status |
| --- | --- | --- |
| [`batch_vrpn_to_csv`](batch_vrpn_to_csv.md) | Recursively finds complete suffixes `.vrpn.mat` and `.vrpn.evt.evt.mat`, converts each through vrpn_to_csv, prints progress, and returns None. | documented |
| [`vrpn_to_csv`](vrpn_to_csv.md) | Exports raw tracking columns into sibling `<first-stem>.track.csv` for standard VRPNs or `<first-stem>.drift.track.csv` for event VRPNs; returns None. | documented |
```{toctree}
:hidden:
:maxdepth: 1

batch_vrpn_to_csv <batch_vrpn_to_csv>
vrpn_to_csv <vrpn_to_csv>
```
