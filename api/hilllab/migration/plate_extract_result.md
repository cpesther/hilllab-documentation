# plate_extract_result

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The variable named nrmse_values is populated from plate_eta, so weighted_mean is weighted by viscosity, not fit error. The end-window parameter and slicing are read-count based; irregular sample times are not handled.
:::

## Signature

```{py:function} plate_extract_result(bundle, column, table, value, end_only=False, end_hours=8)
:module: hilllab.migration.plate_extract_result
:canonical: hilllab.migration.plate_extract_result.plate_extract_result
```

## Behavior and usage

Returns mean, median, weighted_mean, maximum, or minimum of a `Column N` result series. table selects eta/D/eta_calib/D_calib/Dt/nrmse/peak; end_only uses the final end_hours converted to read count. The end range must be strictly shorter than the full experiment. Supply a one-based numeric column value, not an already formatted column name.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `required` | Migration Bundle with the requested populated result table. |
| `column` | `required` | One-based column number; the routine forms Column N internally. |
| `table` | `required` | **string**. one of 'eta', 'D', eta_calib', 'D_calib', 'Dt', ' nrmse', or 'peak' |
| `value` | `required` | **string**. the statistical value to return. One of 'mean',  'median', 'weighted_mean', 'minimum', 'maximum'. |
| `end_only` | `False` | Restrict statistics to the final read-count window when True. |
| `end_hours` | `8` | Requested trailing duration in hours, converted using bundle interval_minutes; must be shorter than the experiment. |

## Returns and side effects

Returns mean, median, weighted_mean, maximum, or minimum of a `Column N` result series. table selects eta/D/eta_calib/D_calib/Dt/nrmse/peak; end_only uses the final end_hours converted to read count.

## Source

`hilllab/migration/plate_extract_result.py`, lines 4–60 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_extract_result.py#L4-L60)
