# hilllab.utilities.gui

Tk popup and hover-tooltip classes.

## Methods and callbacks

| Function | Purpose | Status |
| --- | --- | --- |
| [`Popup.__init__`](Popup.__init__.md) | Sets `message`, normalized `type`, and `title`; returns `None`. | documentation in progress |
| [`Popup.show`](Popup.show.md) | Creates a nonmodal Tk Toplevel containing severity, title, message, and an OK button. | documentation in progress |
| [`Tooltip.__init__`](Tooltip.__init__.md) | Accepts a Tk `widget` and tooltip `text`, stores state, and registers event callbacks; returns `None`. | documentation in progress |
| [`Tooltip.hide_tooltip`](Tooltip.hide_tooltip.md) | Destroys the current floating window, clears the stored handle, and returns `None`. | documentation in progress |
| [`Tooltip.move_tooltip`](Tooltip.move_tooltip.md) | Moves an existing tooltip to 10 pixels right/below the mouse event's screen coordinates and returns `None`. | documentation in progress |
| [`Tooltip.show_tooltip`](Tooltip.show_tooltip.md) | Returns `None`; creates a borderless topmost window unless a tooltip already exists or text is empty. | needs review |

## Classes and data containers

(class-popup)=

### Popup

```{py:class} Popup
:module: hilllab.utilities.gui.Popup
:canonical: hilllab.utilities.gui.Popup.Popup
```

Stores a message, lowercased severity, and window title. Creating the object does not display it; call its `show()` method in an active Tk application. `COLORS` maps warning/error/info to orange/red/blue.

[Constructor arguments and defaults](Popup.__init__.md).

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `COLORS` | Not specified | Configured lookup mapping; see source for entries. |
| `message` | Not specified | Set from the supplied arguments or runtime context. |
| `type` | Not specified | Set from the supplied arguments or runtime context. |
| `title` | Not specified | Set from the supplied arguments or runtime context. |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Popup.py).

(class-tooltip)=

### Tooltip

```{py:class} Tooltip
:module: hilllab.utilities.gui.Tooltip
:canonical: hilllab.utilities.gui.Tooltip.Tooltip
```

Associates hover text with a Tk widget by binding enter/leave/motion events. The constructor replaces bindings for those events rather than adding to existing ones. Its floating window is created on entry and destroyed on exit.

[Constructor arguments and defaults](Tooltip.__init__.md).

| Attribute | Declared type | Initial state / role |
| --- | --- | --- |
| `widget` | Not specified | Set from the supplied arguments or runtime context. |
| `text` | Not specified | Set from the supplied arguments or runtime context. |
| `tooltip` | Not specified | Not yet set |

[View class source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/utilities/gui/Tooltip.py).

```{toctree}
:hidden:
:maxdepth: 1

Popup.__init__ <Popup.__init__>
Popup.show <Popup.show>
Tooltip.__init__ <Tooltip.__init__>
Tooltip.hide_tooltip <Tooltip.hide_tooltip>
Tooltip.move_tooltip <Tooltip.move_tooltip>
Tooltip.show_tooltip <Tooltip.show_tooltip>
```
