# create_groups

[Folder overview](index.md)

## Signature

```{py:function} create_groups(h5_path)
:module: hilllab.dynamics.create_groups
:canonical: hilllab.dynamics.create_groups.create_groups
```

## Behavior and usage

Reads summary identifiers and writes a collision-safe `.groups.json` template, distributing unique IDs into five example groups. Returns None and prints the new path. Edit this JSON to actual experimental conditions before plotting; the generated example groups have no scientific meaning.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `h5_path` | `required` | **string**. the path to the h5 batch file for which the groups will be created. |

## Returns and side effects

Returns None and prints the new path.

## Related HillLab tools

Shared functions and classes used by this tool:

- [`hilllab.utilities.generate_safe_name.generate_safe_name`](../utilities/generate_safe_name.md)

## Source

`hilllab/dynamics/create_groups.py`, lines 9–51 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/dynamics/create_groups.py#L9-L51)
