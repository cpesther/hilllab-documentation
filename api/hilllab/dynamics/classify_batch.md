# classify_batch

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The model method explicitly raises 'not yet implemented'. The gmm route inherits classify_GMM's uncalibrated cluster semantics and missing-feature problems.
:::

## Signature

```{py:function} classify_batch(h5_path, method='gmm')
:module: hilllab.dynamics.classify_batch
:canonical: hilllab.dynamics.classify_batch.classify_batch
```

## Behavior and usage

With method gmm, copies the source HDF to `<stem>.classify.h5`, replaces its summary table with mixture labels, and returns None. Other HDF tables are preserved by the copy. Existing destination files can be overwritten.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the file path to the h5 file to classify |
| `method` | `'gmm'` | **string**. either 'gmm' for the Gaussian mixture model  method or 'model' for the machine learning model method. |

## Returns and side effects

With method gmm, copies the source HDF to `<stem>.classify.h5`, replaces its summary table with mixture labels, and returns None.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.dynamics.classify_GMM.classify_GMM`](classify_GMM.md)

## Source

`hilllab/dynamics/classify_batch.py`, lines 10–53 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/classify_batch.py#L10-L53)
