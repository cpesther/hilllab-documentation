# _calculate_origin_from_lines

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
Parallel/degenerate lines are not rejected by checking the returned rank. Least squares can return a minimum-norm point for a nonunique geometry without raising, despite the error-message wording.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:function} _calculate_origin_from_lines(lines)
:module: hilllab.magnets._calculate_origin_from_lines
:canonical: hilllab.magnets._calculate_origin_from_lines._calculate_origin_from_lines
```

## Behavior and usage

Accepts at least two lines represented by endpoint pairs and returns a least-squares `(x, y)` origin, or None after a caught linear algebra error. Coordinate units are preserved.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `lines` | `required` | **list of tuples**. Each element is a line segment defined by start and end points: ((x_start, y_start), (x_end, y_end)). |

## Returns and side effects

Accepts at least two lines represented by endpoint pairs and returns a least-squares `(x, y)` origin, or None after a caught linear algebra error.

## Source

`hilllab/magnets/_calculate_origin_from_lines.py`, lines 4–57 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/magnets/_calculate_origin_from_lines.py#L4-L57)
