import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Window(Gtk.ApplicationWindow):
    """ This is the main window widget """
    def __init__(self, application):
        Gtk.Window.__init__(self, title = "Hello World",
                            application = application)
        self.set_default_size(500, 500)

        label = Gtk.Label()
        label.set_markup('<span font="40">Hello World!</span>')
        self.add(label)

        
class ApplicationWindow(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = Window(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        
        
    
