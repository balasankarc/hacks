#! /usr/bin/env python
#
# journalize - A software to keep daily journals in plain text format
#
# Copyright (c) 2014
#        Balasankar C <balasankarc@autistici.org>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.



#Note : The stuff is save as you go. That means, no undo. :(
#TODO : Enable Ctrl + Z => undo

import pygtk
import gtk
import sys
import os


class Base:

    def changedate(self,widget):
        filetext = self.filecontent.get_buffer().get_text(self.filecontent.get_buffer().get_start_iter(),self.filecontent.get_buffer().get_end_iter())
        self.inpfile.write(filetext)
        self.inpfile.close()        
        date = self.datetostring(self.calendar.get_date())
        self.inpfile.close()
        try:
            self.inpfile = open("Posts/" + date + ".txt","r")
            self.filecontent.get_buffer().set_text(self.inpfile.read())
            self.inpfile.close()
        except:
            self.filecontent.get_buffer().set_text("")
        finally:
            self.inpfile = open("Posts/" + date + ".txt","w")

    def datetostring(widget,date):
        day=str(date[0])
        month=str(date[1])
        year=str(date[2])
        stringdate = day + "_" + month + "_" + year
        return stringdate

    def destroy(self,widget,data=None):
        filetext = self.filecontent.get_buffer().get_text(self.filecontent.get_buffer().get_start_iter(),self.filecontent.get_buffer().get_end_iter())
        self.inpfile.write(filetext)
        self.inpfile.close()        
        sys.exit()


    def __init__(self):
        #Main function
        self.flag=0
        self.window = gtk.Window()
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.windowx,self.windowy = self.window.get_position()
        self.window.set_size_request(1360,720)
        self.window.maximize()
        self.window.show()
        self.fixed = gtk.Fixed()
        self.window.connect("destroy",self.destroy)
        self.calendar = gtk.Calendar()
        self.calendar.connect("day_selected",self.changedate)
        self.scrollwindow = gtk.ScrolledWindow()
        self.filecontent = gtk.TextView()
        self.filecontent.set_size_request(1000, 650)
        self.scrollwindow.set_shadow_type(type=gtk.SHADOW_ETCHED_IN)
        self.scrollwindow.add(self.filecontent)
        self.scrollwindow.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        self.fixed.put(self.calendar,30,30)
        self.fixed.put(self.scrollwindow,300,30)
        try:
            self.inpfile = open("Posts/" + self.datetostring(self.calendar.get_date()) + ".txt","r")
            self.filecontent.get_buffer().set_text(self.inpfile.read())
            self.inpfile.close()
        except:
            self.filecontent.get_buffer().set_text("")
        finally:
            self.inpfile = open("Posts/" + self.datetostring(self.calendar.get_date()) + ".txt","w")
        self.window.add(self.fixed)
        self.window.show_all()
    def main(self):
        gtk.main()

if __name__ == "__main__":
    base= Base()
    base.main()
