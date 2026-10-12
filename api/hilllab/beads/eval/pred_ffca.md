# pred_ffca

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Imports `.tf_data` from beads.eval although that module exists in the parent folder. The current module is not importable as written.
:::

## Signature

```{py:function} pred_ffca(path, models, key)
:module: hilllab.beads.eval.ffca
:canonical: hilllab.beads.eval.ffca.pred_ffca
```

## Behavior and usage

Returns `(avg_ffca, std_ffca, labels)` after predicting immediate `.h5` files and grouping filename prefixes by plate. It assumes class IDs 0=stuck and 2=oscillating, computes oscillating/(oscillating+stuck), and averages across both files and models. Plate prefixes must parse as `Plate<number>` for sorting; zero denominators are unguarded.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. path to folder containing a bunch of plate h5 files |
| `models` | `required` | **list**. list of models |
| `key` | `required` | **str**. model type ('position','parameter','summary') |

## Returns and side effects

Returns `(avg_ffca, std_ffca, labels)` after predicting immediate `.h5` files and grouping filename prefixes by plate.

## Source

`hilllab/beads/eval/ffca.py`, lines 18–95 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/ffca.py#L18-L95)
