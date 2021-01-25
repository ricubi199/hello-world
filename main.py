import sys
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from src.hello_world import ApplicationWindow

if __name__ == "__main__":
    app = ApplicationWindow()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
