#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

# ============Functions============
import Functions as fn
import autostart
import desktopr
import fish
import distro
import fixes
import lightdm
import login
import lxdm
import neofetch
import os
import sddm
import services
import shell
import termite
import template
import themer
import user
import zsh_theme
#import polybar
#import slim
#import Gtk_Functions
#import oblogout
#import skelapp

# =============GUI=================
import Autostart_GUI
import Desktopr_GUI
import Fixes_GUI
import Grub_GUI
import Login_GUI
import Arcolinuxmirrors_GUI
import Neofetch_GUI
import Pacman_GUI
import Privacy_GUI
import Termite_GUI
#import Template_GUI
import Utilities_GUI
import Services_GUI
import Shell_GUI
import Themer_GUI
import User_GUI
#import Oblogout_GUI
#import Slimlock_GUI
#import Polybar_GUI
#import GTK_GUI
#import SkelApp_GUI

def GUI(self, Gtk, Gdk, GdkPixbuf, base_dir, os, Pango):  # noqa

    #debug = True
    debug = False

    # =======================================================
    #                       App Notifications
    # =======================================================

    hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.notification_revealer = Gtk.Revealer()
    self.notification_revealer.set_reveal_child(False)

    self.notification_label = Gtk.Label()

    pb_panel = GdkPixbuf.Pixbuf().new_from_file(base_dir + '/images/panel.png')
    panel = Gtk.Image().new_from_pixbuf(pb_panel)

    overlayFrame = Gtk.Overlay()
    overlayFrame.add(panel)
    overlayFrame.add_overlay(self.notification_label)

    self.notification_revealer.add(overlayFrame)

    hbox0.pack_start(self.notification_revealer, True, False, 0)

    # ==========================================================
    #                       CONTAINER
    # ==========================================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    vbox.pack_start(hbox, True, True, 0)
    self.add(vbox)

    # ==========================================================
    #                    INITIALIZE STACK
    # ==========================================================
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
    stack.set_transition_duration(350)

    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    #vboxStack9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack11 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack12 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack13 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack14 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack15 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack16 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack17 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack18 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack19 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack20 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack21 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack22 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vboxStack23 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ==========================================================
    #                AUTOSTART
    # ==========================================================

    if debug:
        print("Autostart_GUI")

    Autostart_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack13, autostart,
                      fn, base_dir)

    # ==========================================================
    #                DESKTOP
    # ==========================================================

    if debug:
        print("Desktopr_GUI")

    Desktopr_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack12, desktopr,
                     fn, base_dir, Pango)

    # # ==========================================================
    # #               FIXES
    # # ==========================================================

    if debug:
        print("Fixes_GUI")

    Fixes_GUI.GUI(self, Gtk, vboxStack19, fn, fixes)

    # ==========================================================
    #                 GRUB
    # ==========================================================

    if debug:
        print("Grub_GUI")

    if fn.check_package_installed("arcolinux-grub-theme-vimix-git"):
        Grub_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack4, fn)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Grub")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack4.pack_start(hbox31, False, False, 0)
        vboxStack4.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("<b>We did not find the application arcolinux-grub-theme-vimix-git</b>\n\
<b>First activate the ArcoLinux repos in the Pacman tab</b>\n\
Then you can choose all kinds of wallpapers\n\
We will reload the ATT automatically")

        if fn.check_systemd_boot():
            ls.set_markup("<b>We believe you are on a system that uses systemd boot</b>\n\
<b>Grub can not be used</b>")

        install_arco_vimix = Gtk.Button(label="Install the grub Vimix theme and ATT will reboot automatically")
        install_arco_vimix.connect("clicked", self.on_click_install_arco_vimix_clicked)
        if fn.check_systemd_boot():
            vboxStack4.pack_start(ls, True, False, 0)
        else:
            vboxStack4.pack_start(ls, True, False, 0)
            vboxStack4.pack_start(install_arco_vimix, False, False, 0)

    # ==========================================================
    #                         LOGIN
    # ==========================================================

    if debug:
        print("Login_GUI")

    Login_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack22, sddm, lightdm, lxdm, os, fn, login)

    # ==========================================================
    #                 MIRRORLIST ARCOLINUX
    # ==========================================================

    if debug:
        print("Arcolinuxmirrors_GUI")

    if fn.file_check("/etc/pacman.d/arcolinux-mirrorlist"):
        Arcolinuxmirrors_GUI.GUI(self, Gtk, vboxStack16, fn)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("ArcoLinux Mirrorlist")
        lbl1.set_name("title")
        hbox31.pack_start(lbl1, False, False, 0)

        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)

        lbl2 = Gtk.Label()
        lbl2.set_markup("First install the ArcoLinux Mirrors and ArcoLinux keys\n\
Then you will be able to set the mirrors of ArcoLinux")

        vboxStack16.pack_start(hbox31, False, False, 0)
        vboxStack16.pack_start(hbox41, False, False, 0)
        vboxStack16.pack_start(lbl2, True, False, 0)


    # # ==========================================================
    # #               NEOFETCH
    # # ==========================================================

    if debug:
        print("Neofetch_GUI")

    if fn.file_check(fn.neofetch_config):
        Neofetch_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack8, neofetch, fn)
    else:
        hbox31 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox41 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl1 = Gtk.Label(xalign=0)
        lbl1.set_text("Neofetch Editor")
        lbl1.set_name("title")
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        hbox41.pack_start(hseparator, True, True, 0)
        hbox31.pack_start(lbl1, False, False, 0)
        vboxStack8.pack_start(hbox31, False, False, 0)
        vboxStack8.pack_start(hbox41, False, False, 0)
        ls = Gtk.Label()
        ls.set_markup("If you install <b>Neofetch</b> and the <i>ArcoLinux themes</i> you can customize <b>Neofetch</b>")
        vboxStack8.pack_start(ls, True, False, 0)

    # ==========================================================
    #                 PACMAN
    # ==========================================================

    if debug:
        print("Pacman_GUI")

    if fn.file_check(fn.pacman):
        Pacman_GUI.GUI(self, Gtk, vboxStack1, fn)

    # ==========================================================
    #                 PRIVACY - HBLOCK
    # ==========================================================

    if debug:
        print("Privacy_GUI")

    Privacy_GUI.GUI(self, Gtk, vboxStack3, fn)

    # ==========================================================
    #                      SERVICES
    # ==========================================================

    if debug:
        print("Services_GUI")

    Services_GUI.GUI(self, Gtk, vboxStack14, fn)


    # ==========================================================
    #                        SHELLS
    # ==========================================================

    if debug:
        print("Shell_GUI")

    Shell_GUI.GUI(self, Gtk, vboxStack23, zsh_theme, fish, base_dir,GdkPixbuf, fn)

    # ==========================================================
    #                        TEMPLATE
    # ==========================================================

    #Template_GUI.GUI(self, Gtk, vboxStack21, fn)

    # # ==========================================================
    # #               TERMINALS - TERMITE CONFIG
    # # ==========================================================

    if debug:
        print("Termite_GUI")

    Termite_GUI.GUI(self, Gtk, vboxStack7, termite, GdkPixbuf, base_dir)

    # # ==========================================================
    # #               TERMINAL FUN
    # # ==========================================================

    if debug:
        print("Utilities_GUI")

    Utilities_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack20, fn)

    # ==========================================================
    #                 THEMES
    # ==========================================================

    if debug:
        print("Themer_GUI")

    Themer_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack10, themer, fn, base_dir)

    # # ==========================================================
    # #                USER
    # # ==========================================================

    if debug:
        print("User_GUI")

    User_GUI.GUI(self, Gtk, GdkPixbuf, vboxStack18, user, fn)

    # ==========================================================
    #                   ADD TO WINDOW
    # ==========================================================

    stack.add_titled(vboxStack13, "stack13", "Autostart")  # Autostart

    stack.add_titled(vboxStack12, "stack12", "Desktop")  # Desktop installer

    stack.add_titled(vboxStack19, "stack19", "Fixes")  # Fixes

    stack.add_titled(vboxStack4, "stack1", "Grub")  # Grub config

    stack.add_titled(vboxStack22, "stack22", "Login")  # Lightdm config

    stack.add_titled(vboxStack16, "stack16", "Mirrors")  # mirrors

    if not fn.distr == "xerolinux":
        stack.add_titled(vboxStack8, "stack4", "Neofetch")  # Neofetch config

    stack.add_titled(vboxStack1, "stack6", "Pacman")  # Pacman config

    stack.add_titled(vboxStack3, "stack2", "Privacy")  # Privacy

    if not fn.distr == "xerolinux":
        stack.add_titled(vboxStack14, "stack14", "Services")  # services

    stack.add_titled(vboxStack23, "stack23", "Shells")  # shell

    #stack.add_titled(vboxStack21, "stack21", "Template")  # template

    stack.add_titled(vboxStack7, "stack8", "Terminals")  # Termite themes

    stack.add_titled(vboxStack20, "stack20", "Terminal Fun") # lolcat and others

    stack.add_titled(vboxStack10, "stack11", "Themes")  # Theme changer

    stack.add_titled(vboxStack18, "stack18", "User")  # user

    stack_switcher = Gtk.StackSidebar()
    stack_switcher.set_name("sidebar")
    stack_switcher.set_stack(stack)

    # =====================================================
    #                       LOGO
    # =====================================================

    ivbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-stock.png'), 45, 45)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    # =====================================================
    #               RESTART/QUIT BUTTON
    # =====================================================

    def on_quit(self):
        os.unlink("/tmp/att.lock")
        Gtk.main_quit()
        print("Thanks for using ArchLinux Tweak Tool")
        print("Report issues to make it even better")
        print("---------------------------------------------------------------------------")

    lbl_distro = Gtk.Label(xalign=0)
    lbl_distro.set_markup("Working on\n" + fn.change_distro_label(distro.id()))
    btnReloadAtt = Gtk.Button(label="Reload ATT")
    btnReloadAtt.set_size_request(100,30)
    btnReloadAtt.connect('clicked', self.on_reload_att_clicked)
    btnReStartAtt = Gtk.Button(label="Restart ATT")
    btnReStartAtt.set_size_request(100,30)
    btnReStartAtt.connect('clicked', self.on_refresh_att_clicked)
    btnQuitAtt = Gtk.Button(label="Quit ATT")
    btnQuitAtt.set_size_request(100,30)
    btnQuitAtt.connect('clicked', on_quit)

    # =====================================================
    #               SUPPORT LINK
    # =====================================================
    pE = Gtk.EventBox()

    pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/support.png'), 58, 58)
    pimage = Gtk.Image().new_from_pixbuf(pbp)

    pE.add(pimage)

    pE.connect("button_press_event", self.on_social_clicked)
    pE.set_property("has-tooltip", True)

    pE.connect("query-tooltip", self.tooltip_callback,
               "Support or get support")

    # =====================================================
    #                      PACKS
    # =====================================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)

    hbox1.pack_start(pE, False, False, 0)
    hbox2.pack_start(lbl_distro, False, False, 0)
    hbox5.pack_start(btnReloadAtt, False, False, 0)
    hbox3.pack_start(btnReStartAtt, False, False, 0)
    hbox4.pack_start(btnQuitAtt, False, False, 0)

    #ivbox.pack_start(image, False, False, 0)
    ivbox.pack_start(stack_switcher, True, True, 0)

    ivbox.pack_start(hbox1, False, False, 0)
    ivbox.pack_start(hbox2, False, False, 0)
    ivbox.pack_start(hbox5, False, False, 0)
    ivbox.pack_start(hbox3, False, False, 0)
    ivbox.pack_start(hbox4, False, False, 0)

    vbox1.pack_start(hbox0, False, False, 0)
    vbox1.pack_start(stack, True, True, 0)

    hbox.pack_start(ivbox, False, True, 0)
    hbox.pack_start(vbox1, True, True, 0)

    stack.set_hhomogeneous(False)
    stack.set_vhomogeneous(False)
