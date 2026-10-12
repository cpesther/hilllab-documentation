# record_message

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} record_message(message, active=True, print_message=True, print_time=True, clear_print=False)
:module: hilllab.utilities.record_message
:canonical: hilllab.utilities.record_message.record_message
```

## Behavior and usage

Appends timestamp/message text to `LOG_FILE_PATH` when active, independently prints when `print_message=True`, and can clear notebook output first. Returns `None`. This is raw comma-separated text, not CSV quoting; commas/newlines in a message can change the apparent columns/rows. `active=False` only disables the disk write, not printing.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `message` | `required` | **str**. the message to be added to the log file. |
| `active` | `True` | **bool**. allows us to "turn off" writing easily when incorporated into other functions without needing to nest this function within a conditional. |
| `print_message` | `True` | **bool**. controls whether the message is also  printed to the console. Useful to avoid needing both this function and a print statement to display a message. This arg is not affected by the active argument. Defaults to False. |
| `print_time` | `True` | Prefix printed messages with local time when True; does not change the on-disk Unix timestamp. |
| `clear_print` | `False` | Attempt to clear IPython display output before printing. |

## Returns and side effects

Returns `None`.

## Source

`hilllab/utilities/record_message.py`, lines 5–45 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/record_message.py#L5-L45)
