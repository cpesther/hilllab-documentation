# publish

[Folder overview](index.md)

:::{admonition} Implementation needs review
:class: warning
The module calls publish() at top level, so importing it moves/replaces binaries immediately. Do not import it merely to inspect its function.
:::

## Signature

```{py:function} publish()
:module: hilllab.cilia.FFTProcessor.publish
:canonical: hilllab.cilia.FFTProcessor.publish.publish
```

## Behavior and usage

Moves all EXE/DLL files recursively from `bin/Release/net10.0/win-x64/publish` into the processor folder, replacing existing destination files; returns `None`. This is a build-maintenance command for the compiled Windows processor.

## Inputs

No explicit input arguments.

## Returns and side effects

Moves all EXE/DLL files recursively from `bin/Release/net10.0/win-x64/publish` into the processor folder, replacing existing destination files; returns `None`.

## Source

`hilllab/cilia/FFTProcessor/publish.py`, lines 6–36 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/cilia/FFTProcessor/publish.py#L6-L36)
