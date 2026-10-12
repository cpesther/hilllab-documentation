# plate_generate_report

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Experiments must be longer than 24 hours because plate_extract_result rejects a full-length end window. Unequal groups are padded with None before outlier processing, which may not support that object-valued array. Report arithmetic and outlier choices need verification in Excel before using the summary as an assay result.
:::

## Signature

```{py:function} plate_generate_report(bundle, include_calibrated=True)
:module: hilllab.migration.plate_generate_report
:canonical: hilllab.migration.plate_generate_report.plate_generate_report
```

## Behavior and usage

Generates a formatted REPORT Excel workbook and returns None. Requires nonempty groups and calculated result tables; takes each capillary's mean over the final 24 hours, then flags viscosity-based MAD outliers across groups. Those same indices are removed from diffusion/calibrated tables. Optional calibrated sections are included only when calibrated eta data exist. Excel AVERAGE/MEDIAN/STDEV formulas are written but not recalculated by openpyxl.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `required` | **migration.Bundle**. the data bundle after processing groups (dict): a dictionary of which columns should be grouped together, where the keys are the names of the groups as strings and the value is a list of the column numbers included in the group. |
| `include_calibrated` | `True` | Include calibrated sections if this is exactly True and calibrated eta results exist. |

## Returns and side effects

Generates a formatted REPORT Excel workbook and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration.plate_extract_result.plate_extract_result`](plate_extract_result.md)
- [`hilllab.utilities.remove_outliers.remove_outliers`](../utilities/remove_outliers.md)

## Source

`hilllab/migration/plate_generate_report.py`, lines 12–334 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_generate_report.py#L12-L334)
