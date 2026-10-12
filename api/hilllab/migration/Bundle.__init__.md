# Bundle.__init__

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:method} Bundle.__init__(self)
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Bundle.__init__
```

## Behavior and usage

Takes no arguments, creates fresh Data and Results objects, and returns None. Constructed containers have no loaded tables and are not ready for calculations until load/preparation steps complete.

## Inputs

No explicit input arguments beyond the bound instance.

## Returns and side effects

Takes no arguments, creates fresh Data and Results objects, and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- {ref}`hilllab.migration.Bundle.Data <class-data>`
- {ref}`hilllab.migration.Bundle.Results <class-results>`

## Source

`hilllab/migration/Bundle.py`, lines 16–18 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L16-L18)
