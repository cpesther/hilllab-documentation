# data_preprocess

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Shuffling occurs before independent take/skip datasets with default reshuffling on iteration; independent split iteration can change membership and allow overlap. Do not assume this guarantees a fixed disjoint experimental train/test split. Splitting is by bead, not by experiment or plate.
:::

## Signature

```{py:function} data_preprocess(datasets)
:module: hilllab.beads.tf_data
:canonical: hilllab.beads.tf_data.data_preprocess
```

## Behavior and usage

Accepts one `(dataset, count)` tuple or a list of compatible tuples, encodes classes in order stuck/transiting/oscillating/discard, and returns `(train_ds, val_ds, test_ds)`. Uses integer-truncated 80%/10% splits with the remainder for test, caches each split, then padded-batches by 32 and prefetches. Only labeled datasets work.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `datasets` | `required` | output from ###_data (dataset, count) (if list, must be from same ###_data func) |

## Returns and side effects

Accepts one `(dataset, count)` tuple or a list of compatible tuples, encodes classes in order stuck/transiting/oscillating/discard, and returns `(train_ds, val_ds, test_ds)`.

## Source

`hilllab/beads/tf_data.py`, lines 251–308 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/tf_data.py#L251-L308)
