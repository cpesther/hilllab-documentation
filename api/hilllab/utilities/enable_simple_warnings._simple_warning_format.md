# enable_simple_warnings._simple_warning_format

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

**Internal helper.** Supports its parent workflow; its interface may change.

**Nested callback/helper.** Available inside its parent function, rather than as a separately importable attribute.

## Signature

```{py:function} enable_simple_warnings._simple_warning_format(message, category, filename, lineno, file=None, line=None)
:module: hilllab.utilities.warning
:canonical: hilllab.utilities.warning.enable_simple_warnings._simple_warning_format
```

## Behavior and usage

Closure-local warning callback returning `CategoryName: message` plus a newline. Filename, line number, file, and source-line arguments are accepted for Python's formatter interface but omitted from the output.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `message` | `required` | Warning message object/text to format. |
| `category` | `required` | Warning category class whose name is printed. |
| `filename` | `required` | Accepted Python formatter source filename; omitted from the output. |
| `lineno` | `required` | Accepted source line number; omitted from the output. |
| `file` | `None` | Accepted formatter stream parameter; unused. |
| `line` | `None` | Accepted source text parameter; unused. |

## Returns and side effects

Returns `None`; any files, plots, messages, or object changes are described under Behavior and usage.

## Source

`hilllab/utilities/warning.py`, lines 11–12 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/warning.py#L11-L12)
