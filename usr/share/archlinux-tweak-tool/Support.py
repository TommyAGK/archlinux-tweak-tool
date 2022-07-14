#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import gi
import os
import Functions as fn
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

base_dir = os.path.dirname(os.path.realpath(__file__))


class Support(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Credits - Support Development", parent, 0)
        # self.add_buttons(Gtk.STOCK_OK,Gtk.ResponseType.OK)

        self.set_size_request(550, 100)
        # self.set_resizable(False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        box = self.get_content_area()
        box.pack_start(vbox, False, False, 0)

        label = Gtk.Label()
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.CENTER)
        label.set_markup("Big thanks to <b>Brad Heffernan</b> who was the driving force behind the ArchLinux Tweak Tool.\n\
After his departure <b>Cameron Percival</b> and <b>Erik Dubois</b> kept developing this easy and efficient tool.\n\n\
You can receive support via <b>Discord channel</b>.\n\
You can support the project with providing code, fixes, ideas, ... via github.\n\
You can give support via donations.\n\
Nowadays the goal of the app is to bridge all Arch Linux based systems.\n\n\
IT is all Arch Linux\n\
the right setting - the right config - the right application - at the right place")

        label2 = Gtk.Label()
        label2.set_justify(Gtk.Justification.CENTER)
        label2.set_markup("Support <b>ArcoLinux</b> - support this app")

        logo = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/archlinux-tweak-tool.png'), 100, 100)
        logo_image = Gtk.Image().new_from_pixbuf(logo)



        ghE = Gtk.EventBox() #github
        discE = Gtk.EventBox() #discord

        donatE = Gtk.EventBox() #paypal
        pbdisc = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/donate.png'), 54, 54)
        ppimage = Gtk.Image().new_from_pixbuf(pbdisc)
        donatE.add(ppimage)
        donatE.connect("button_press_event", self.on_support_click, "https://www.arcolinux.info/donation/")
        donatE.set_property("has-tooltip", True)
        donatE.connect("query-tooltip", self.tooltip_callback, "Different ways to support")

        patreonE = Gtk.EventBox() #patreon
        pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/patreon.png'), 48, 48)
        pimage = Gtk.Image().new_from_pixbuf(pbp)
        patreonE.add(pimage)
        patreonE.connect("button_press_event", self.on_support_click, "https://www.patreon.com/arcolinux")
        patreonE.set_property("has-tooltip", True)
        patreonE.connect("query-tooltip", self.tooltip_callback, "Support ArcoLinux on Patreon")

        paypalE = Gtk.EventBox() #paypal
        pbpp = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/paypal.png'), 54, 54)
        ppimage = Gtk.Image().new_from_pixbuf(pbpp)
        paypalE.add(ppimage)
        paypalE.connect("button_press_event", self.on_support_click, "https://www.paypal.com/paypalme/arcolinuxpaypal")
        paypalE.set_property("has-tooltip", True)
        paypalE.connect("query-tooltip", self.tooltip_callback, "Donate to this project via paypal")


        discordE = Gtk.EventBox() #paypal
        pbdisc = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/discord.png'), 54, 54)
        ppimage = Gtk.Image().new_from_pixbuf(pbdisc)
        discordE.add(ppimage)
        discordE.connect("button_press_event", self.on_support_click, "https://discord.gg/R2amEEz")
        discordE.set_property("has-tooltip", True)
        discordE.connect("query-tooltip", self.tooltip_callback, "Get ATT support on Discord")

        githubE = Gtk.EventBox() #paypal
        pbghub = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/github.png'), 54, 54)
        ppimage = Gtk.Image().new_from_pixbuf(pbghub)
        githubE.add(ppimage)
        githubE.connect("button_press_event", self.on_support_click, "https://github.com/arcolinux/archlinux-tweak-tool-dev")
        githubE.set_property("has-tooltip", True)
        githubE.connect("query-tooltip", self.tooltip_callback, "Donate time and code to this project")


        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        hbox.pack_start(label, True, True, 10)
        hbox2.pack_start(donatE, False, False, 10)
        hbox2.pack_start(githubE, False, False, 10)
        hbox2.pack_start(patreonE, False, False, 0)
        hbox2.pack_start(paypalE, False, False, 10)
        hbox2.pack_start(discordE, False, False, 10)
        hbox3.pack_start(hbox2, True, False, 0)

        vbox.pack_start(logo_image, False, False, 10)
        vbox.pack_start(hbox, False, False, 10)

        vbox.pack_end(hbox3, False, False, 10)
        vbox.pack_end(hbox1, False, False, 0)
        vbox.pack_end(label2, False, False, 10)

        self.show_all()

    def on_support_click(self, widget, event, link):
        t = fn.threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()
        # print("CLICKED")
        # self.weblink(link)

    def weblink(self, link):
        if fn.check_package_installed("firefox"):
            fn.subprocess.call(["sudo", "-H", "-u", fn.sudo_username, "bash", "-c", "firefox --new-tab " + link], shell=False)
        else:
            if fn.check_package_installed("chromium"):
                fn.subprocess.call(["sudo", "-H", "-u", fn.sudo_username, "bash", "-c", "chromium " + link], shell=False)
            else:
                fn.subprocess.call(["sudo", "-H", "-u", fn.sudo_username, "bash", "-c", "exo-open --launch webbrowser " + link], shell=False)

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True
