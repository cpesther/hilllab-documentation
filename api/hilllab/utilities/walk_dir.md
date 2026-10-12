# walk_dir

[Folder overview](index.md)

## Signature

```{py:function} walk_dir(path, extension=None)
:module: hilllab.utilities.walk_dir
:canonical: hilllab.utilities.walk_dir.walk_dir
```

## Behavior and usage

Returns an unsorted list of file paths from a recursive os.walk. `extension` may be a string or list; comparison uses the complete suffix sequence and is case sensitive. For example `vrpn.mat` matches `.vrpn.mat`, while `mat` alone does not.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `path` | `required` | **string**. the path to the root folder to be walked |
| `extension` | `None` | **list**. allows the specification of a certain file  extension types to record, filtering out all others |

## Returns and side effects

Returns an unsorted list of file paths from a recursive os.walk.

## Source

`hilllab/utilities/walk_dir.py`, lines 5–48 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/walk_dir.py#L5-L48)
