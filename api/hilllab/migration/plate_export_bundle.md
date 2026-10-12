# plate_export_bundle

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The load wrapper automatically looks for `.1dpre.xlsx`, while this exporter uses `.bundle.xlsx`; automatic reuse does not discover its output. PRE import restores some dictionary-like sheets as DataFrames. Round-trip compatibility needs review.
:::

## Signature

```{py:function} plate_export_bundle(bundle)
:module: hilllab.migration.plate_export_bundle
:canonical: hilllab.migration.plate_export_bundle.plate_export_bundle
```

## Behavior and usage

Writes raw, normalized, cleaned, localization, radii, timing, group/calibration, overflow, and preparation metadata sheets to `<stem>.bundle.xlsx`; returns None. Existing destinations prompt for overwrite. All referenced tables must be initialized. This export stores preprocessing data, not the result tables in Bundle.results.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `bundle` | `required` | **migration.Bundle**. the bundle object to be saved |

## Returns and side effects

Writes raw, normalized, cleaned, localization, radii, timing, group/calibration, overflow, and preparation metadata sheets to `<stem>.bundle.xlsx`; returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.warning.warn`](../utilities/warn.md)

## Source

`hilllab/migration/plate_export_bundle.py`, lines 10–93 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/plate_export_bundle.py#L10-L93)
