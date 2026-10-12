# circular

[Folder overview](index.md)

## Signature

```{py:function} circular(image, margin=10)
:module: hilllab.binding.masks.circular
:canonical: hilllab.binding.masks.circular.circular
```

## Behavior and usage

Returns a copy-like masked image of the same shape with pixels outside a centered circle set to zero. `margin` is in pixels and is subtracted from half the shorter image dimension; it must leave a valid nonnegative radius. Supports grayscale and multichannel images via an 8-bit mask.

## Inputs

| Argument | Default / calling convention | Description |
| --- | --- | --- |
| `image` | `required` | **numpy.ndarray**. input image array of shape (H, W) or (H, W, C) |
| `margin` | `10` | **int**. the number of pixels by which the radius of the  mask will be reduced as compared to the total width and height of the image. |

## Returns and side effects

Returns a copy-like masked image of the same shape with pixels outside a centered circle set to zero.

## Source

`hilllab/binding/masks/circular.py`, lines 6–43 · [View source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/binding/masks/circular.py#L6-L43)
