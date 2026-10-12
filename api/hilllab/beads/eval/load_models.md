# load_models

[Folder overview](index.md)

## Signature

```{py:function} load_models(path)
:module: hilllab.beads.eval.load_models
:canonical: hilllab.beads.eval.load_models.load_models
```

## Behavior and usage

Returns a list of successfully loaded immediate `.keras` files. Invalid directory paths raise SyntaxError; individual model load failures are silently discarded. Ordering follows os.listdir rather than filenames, so associate models with files yourself if identity matters. Keras is an undeclared optional dependency.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **str**. path to folder where models are |

## Returns and side effects

Returns a list of successfully loaded immediate `.keras` files.

## Source

`hilllab/beads/eval/load_models.py`, lines 6–33 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/beads/eval/load_models.py#L6-L33)
