# test_print_dict_table

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} test_print_dict_table(capsys)
:module: hilllab.tests.test_utilities
:canonical: hilllab.tests.test_utilities.test_print_dict_table
```

## Behavior and usage

Pytest test accepting the capsys fixture, printing a sample dictionary table, and asserting that selected keys/value/title appear in captured output. Returns None on pass and raises AssertionError on failure. Run through pytest rather than calling with a normal stream object; pytest is an additional development dependency.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `capsys` | `required` | Pytest capture fixture injected by the test runner; exposes readouterr(). |

## Returns and side effects

Returns None on pass and raises AssertionError on failure.

## Source

`hilllab/tests/test_utilities.py`, lines 7–25 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/tests/test_utilities.py#L7-L25)
