# classify_GMM

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Gaussian-mixture component numbers do not establish biological classes; the mapping is hard-coded without calibration. Rows with missing features are dropped before fitting but labels are assigned to the original full table, causing length mismatch. Passing identifier attempts to pivot on a cluster column that is never created.
:::

## Signature

```{py:function} classify_GMM(h5_path, identifier=None)
:module: hilllab.dynamics.classify_GMM
:canonical: hilllab.dynamics.classify_GMM.classify_GMM
```

## Behavior and usage

Standardizes six summary features, fits a three-component Gaussian mixture, and returns `(summary_with_labels_and_weights, pivot_or_None)`. Component indices are mapped to stuck/oscillating/transiting by a fixed dictionary. It does not persist changes itself.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | HDF filename with a summary table containing the six required motion features. |
| `identifier` | `None` | Optional summary column intended for count pivoting. This branch currently refers to an undefined cluster column. |

## Returns and side effects

Standardizes six summary features, fits a three-component Gaussian mixture, and returns `(summary_with_labels_and_weights, pivot_or_None)`.

## Source

`hilllab/dynamics/classify_GMM.py`, lines 7–67 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/classify_GMM.py#L7-L67)
