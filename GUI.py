#!/usr/bin/python
# -*- coding: utf-8 -*-
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess
import json

class ourwindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ResumeWriter Program")
        Gtk.Window.set_default_size(self, 400,325)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        button1 = Gtk.Button("Click when done inserting link")
        button1.connect("clicked", self.whenbutton1_clicked)
        hbox.pack_start(button1, True, True, 0)
        
    def whenbutton1_clicked(self, button):
        link = "./main.sh " + self.entry.get_text()
        subprocess.call(link, shell=True)
        window.destroy()
window = ourwindow()        
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

class TreeViewFilterWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Phrases to consider")
        Gtk.Window.set_default_size(self, 400,325)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
        with open('filtered.json') as f:
            data = json.load(f)
        self.liststore = Gtk.ListStore(str, str)
        for key,value in data.items():
            self.liststore.append([key,value])
        treeview = Gtk.TreeView(model=self.liststore)
        renderer_num = Gtk.CellRendererText()
        column_num = Gtk.TreeViewColumn("Number", renderer_num, text=0)
        treeview.append_column(column_num)
        renderer_value = Gtk.CellRendererText()
        column_value = Gtk.TreeViewColumn(
            "Value", renderer_value, text=1
        )
        treeview.append_column(column_value)
        self.add(treeview)
window = TreeViewFilterWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
