#!/usr/bin/env python3

import gi.repository
import psutil
import time
import datetime
gi.require_version('Budgie', '1.0')
gi.require_version('Wnck', '3.0')
from _thread import start_new_thread
from gi.repository import Budgie, GObject, Wnck, Gtk
import threading 
class fourtwentystats(GObject.GObject, Budgie.Plugin):
    __gtype_name__ = "fourtwentystats"

    def __init__(self):
        GObject.Object.__init__(self)

    def do_get_panel_widget(self, uuid):
        return fourtwentystatsApplet(uuid)
class myThread (threading.Thread):
    def __init__(self, label):
        threading.Thread.__init__(self)
        self.label = label
        self.counter = 2
    def run(self): 
        while self.counter>1: #infinite loop, maybe ill change that some time

            self.counter = self.counter +1
            self.mem = psutil.virtual_memory() #get virtual memory
            self.memp  = str((self.mem.used / self.mem.total)*100)[:2] #first 2 numbers of percental memory usage
            self.cpu = str(psutil.cpu_percent(interval=0.0)) #cpu usage
            stri = "CPU: "+ self.cpu+"% RAM: " +self.memp+"%" #label string
            self.label.set_text(stri) 
            time.sleep(5) #intervall

class fourtwentystatsApplet(Budgie.Applet):
    def __init__(self, uuid):
        Budgie.Applet.__init__(self)

        self.label = Gtk.Label.new()
        self.add(self.label)
        self.show_all()

        t = myThread(self.label)
        t.start()

