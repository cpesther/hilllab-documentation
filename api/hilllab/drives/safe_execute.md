# safe_execute

[Folder overview](index.md)

## Signature

```{py:function} safe_execute(function)
:module: hilllab.drives.safe_execute
:canonical: hilllab.drives.safe_execute.safe_execute
```

## Behavior and usage

Calls a no-argument callable and returns its result; on any Exception returns None without logging. Wrap functions requiring arguments in a closure. A legitimate None result is indistinguishable from a caught error.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `function` | `required` | **callable**. A no-argument function or lambda that  performs a potentially unsafe operation. |

## Returns and side effects

Calls a no-argument callable and returns its result; on any Exception returns None without logging.

## Source

`hilllab/drives/safe_execute.py`, lines 3–32 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/drives/safe_execute.py#L3-L32)
