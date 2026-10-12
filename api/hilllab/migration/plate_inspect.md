# plate_inspect

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
With normalize=True and recorded overflows, the annotation code uses dataset_max although it was only initialized in the nonnormalized branch. Overflow vertical-line ymax is passed in intensity units even though Matplotlib expects an axes fraction.
:::

## Signature

```{py:function} plate_inspect(bundle=None, path=None, data_type='SPE', extended=False, normalize=False, export=False)
:module: hilllab.migration.plate_inspect
:canonical: hilllab.migration.plate_inspect.plate_inspect
```

## Behavior and usage

Draws raw curves by read for 24 or 32 columns and returns None. A supplied bundle is reused; otherwise path/data_type/extended load raw data. normalize divides each curve by its maximum for display only. export writes a sibling INSPECT PNG. Curves are cast to integers before plotting, which discards fractional values.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `None` | **migration.Bundle**. data stored in the bundle class |
| `path` | `None` | **string**. the path to the data to be analyzed if a bundle is not provided. |
| `data_type` | `'SPE'` | **string**. Specifies the type model used to collect the  data. Options include 'SPE' (default), 'TEC', and 'PRE'. |
| `extended` | `False` | **bool**. controls whether the plate is interpreted as an extended or standard layout. |
| `normalize` | `False` | **bool**. controls whether the data is normalized before plotting |
| `export` | `False` | **bool**. controls whether the inspection plot is  exported to a PNG |

## Returns and side effects

Draws raw curves by read for 24 or 32 columns and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.migration.load_file.load_file`](load_file.md)

## Source

`hilllab/migration/plate_inspect.py`, lines 8–125 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_inspect.py#L8-L125)
