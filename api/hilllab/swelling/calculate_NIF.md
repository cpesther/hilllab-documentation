# calculate_NIF

[Folder overview](index.md)

:::{admonition} Source documentation in progress
:class: caution
The original docstring has gaps. This guide describes what the current code establishes; unconfirmed details remain flagged.
:::

## Signature

```{py:function} calculate_NIF(channel_data, num_reads)
:module: hilllab.swelling.calculate_NIF
:canonical: hilllab.swelling.calculate_NIF.calculate_NIF
```

## Behavior and usage

Returns a DataFrame of per-column Simpson integrals across a fixed 16-point spatial grid `0, 4.5, …, 67.5`. Iterates read blocks 1 through num_reads-1, intentionally/implicitly omitting read 0. It does not itself normalize fluorescence, despite the NIF name; normalization happens in process_2C_swelling. Spatial-unit interpretation is not specified in this function.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `channel_data` | `required` | **pd.DataFrame**. the dataframe containing the data to be analyzed. |
| `num_reads` | `required` | Number of complete 16-row read blocks expected in the input table. |

## Returns and side effects

Returns a DataFrame of per-column Simpson integrals across a fixed 16-point spatial grid `0, 4.5, …, 67.5`.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.swelling._access_read._access_read`](_access_read.md)
- [`hilllab.utilities.print_progress_bar.print_progress_bar`](../utilities/print_progress_bar.md)

## Source

`hilllab/swelling/calculate_NIF.py`, lines 9–53 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/swelling/calculate_NIF.py#L9-L53)
