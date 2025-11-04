import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gdk, GLib

Adw.init()

def flush_gtk_events():
    """Process pending GTK/GLib events (GTK4-safe)."""
    ctx = GLib.main_context_default()
    while ctx.pending():
        ctx.iteration(False)

def get_css_var_color(var_name: str) -> str | None:
    """Return resolved RGBA string for a Libadwaita CSS variable."""
    win = Gtk.Window()
    label = Gtk.Label(label="test")
    win.set_child(label)
    win.present()  # Realize the widget so style applies
    flush_gtk_events()

    provider = Gtk.CssProvider()
    css = f"label {{ color: var(--{var_name}); }}"
    provider.load_from_data(css.encode())

    Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(),
        provider,
        Gtk.STYLE_PROVIDER_PRIORITY_USER,
    )

    flush_gtk_events()
    rgba = label.get_style_context().get_color()
    win.destroy()
    return rgba.to_string()

# --- Common Libadwaita CSS color variables ---
color_vars = [
    "window-bg-color", "window-fg-color",
    "view-bg-color", "view-fg-color",
    "headerbar-bg-color", "headerbar-fg-color",
    "card-bg-color", "card-fg-color",
    "accent-color", "accent-fg-color",
    "error-color", "warning-color", "success-color",
    "sidebar-bg-color",
]

for name in color_vars:
    try:
        print(f"{name:25}: {get_css_var_color(name)}")
    except Exception as e:
        print(f"{name:25}: [error: {e}]")

