# cache_view

[Folder overview](index.md)

## Signature

```{py:function} cache_view()
:module: hilllab.utilities.cache_view
:canonical: hilllab.utilities.cache_view.cache_view
```

## Behavior and usage

Opens `APP_DATA_FOLDER` using `os.startfile`, macOS `open`, or Linux `xdg-open`; returns `None`. It requires the native file browser to be installed and accessible.

## Inputs

No explicit input arguments.

## Returns and side effects

Opens `APP_DATA_FOLDER` using `os.startfile`, macOS `open`, or Linux `xdg-open`; returns `None`.

## Source

`hilllab/utilities/cache_view.py`, lines 6–20 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/cache_view.py#L6-L20)
