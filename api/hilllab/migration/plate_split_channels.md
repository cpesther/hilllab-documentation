# plate_split_channels

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Values above n_channels=4 are accepted but only four channels are extracted. Excitation metadata is read from fixed header positions, and repeated excitation labels can overwrite both output files and mapping entries.
:::

## Signature

```{py:function} plate_split_channels(path, n_channels=4)
:module: hilllab.migration.plate_split_channels
:canonical: hilllab.migration.plate_split_channels.plate_split_channels
```

## Behavior and usage

Reads a UTF-16 SpectraMax export, separates numbered channel columns, and writes one `<excitation>nm_<stem>.xlsx` file per extracted channel. Returns an excitation-string→Path mapping. It extracts two, three, or four channels; metadata mismatches prompt for excitation wavelengths. Output workbooks preserve repeated A–P read labels.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the path to the file containing multiple chanenls of data. |
| `n_channels` | `4` | **int**. the number of channels in the file |

## Returns and side effects

Returns an excitation-string→Path mapping.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.format_spectra_table.format_spectra_table`](../utilities/format_spectra_table.md)
- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/migration/plate_split_channels.py`, lines 10–109 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_split_channels.py#L10-L109)
