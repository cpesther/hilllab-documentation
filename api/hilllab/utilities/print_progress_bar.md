# print_progress_bar

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The completion comparison uses a fraction against `98`, not `0.98`; the special near-complete branch does not activate at 98%. Progress outside 0–total is not bounded.
:::

## Signature

```{py:function} print_progress_bar(progress, total, title, multiple=1, bar_length=50)
:module: hilllab.utilities.print_progress_bar
:canonical: hilllab.utilities.print_progress_bar.print_progress_bar
```

## Behavior and usage

Writes an in-place console progress bar with local time; returns `None`. `total` must be positive, `multiple` nonzero, and `progress` a completed-item count. It only prints when `progress % multiple == 0`. The caller supplies a final newline.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `progress` | `required` | **int**. Current progress count. |
| `total` | `required` | **int**. Total count representing 100% completion. |
| `title` | `required` | **str**. Label displayed before the progress bar. |
| `multiple` | `1` | Nonzero update interval; prints only when progress is divisible by this value. |
| `bar_length` | `50` | **int, optional**. Width of the progress bar in characters. |

## Returns and side effects

Writes an in-place console progress bar with local time; returns `None`.

## Source

`hilllab/utilities/print_progress_bar.py`, lines 5–38 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/print_progress_bar.py#L5-L38)
