# Bundle._load_read

[Folder overview](index.md)

**Internal helper.** Supports its parent workflow; its interface may change.

## Signature

```{py:method} Bundle._load_read(self, read_number, type='clean')
:module: hilllab.migration.Bundle
:canonical: hilllab.migration.Bundle.Bundle._load_read
```

## Behavior and usage

Returns a 16-row DataFrame slice for zero-based read_number. type raw selects raw, normalized selects normalized, and all other values—including clean—select clean. It preserves row labels and does not copy/validate a complete read. The selected table must already exist.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `read_number` | `required` | **int**. the 0-based index of the read that should  be pulled. |
| `type` | `'clean'` | **string**. indicates the table from which the data  should be pulled. Possible values include 'raw', 'normalized', and 'clean'. |

## Returns and side effects

Returns a 16-row DataFrame slice for zero-based read_number. type raw selects raw, normalized selects normalized, and all other values—including clean—select clean.

## Source

`hilllab/migration/Bundle.py`, lines 21–54 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/migration/Bundle.py#L21-L54)
