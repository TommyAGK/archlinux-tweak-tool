#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import Functions as fn

def GUI(self, Gtk, GdkPixbuf, vboxStack4, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Grub Themes")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)

    # ==========================================================
    #                       GRUB
    # ==========================================================

    hbox10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    label10 = Gtk.Label("Grub timeout in seconds")
    self.scale = Gtk.Scale().new(Gtk.Orientation.HORIZONTAL)
    self.scale.set_draw_value(True)
    self.scale.set_value_pos(Gtk.PositionType.BOTTOM)
    self.scale.set_range(0, 30)
    self.scale.set_digits(0)
    self.scale.set_inverted(False)
    self.scale.set_size_request(200, 10)
    self.scale.set_tooltip_text("Seconds")
    btnsave = Gtk.Button(label="Save")
    btnsave.connect("clicked", self.on_clicked_grub_timeout)
    hbox10.pack_start(label10, False, False, 10)
    hbox10.pack_end(btnsave, False, False, 10)
    hbox10.pack_end(self.scale, False, False, 10)

    hbox11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label11 = Gtk.Label("Import image")
    self.tbimage = Gtk.Entry()
    btnsearch = Gtk.Button(label=". . .")
    btnsearch.connect("clicked", self.on_choose_wallpaper)
    hbox11.pack_start(label11, False, False, 10)
    hbox11.pack_start(self.tbimage, True, True, 10)
    hbox11.pack_start(btnsearch, False, False, 10)

    hbox12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    label12 = Gtk.Label()
    label12.set_text("Select a wallpaper and apply")
    btnimport = Gtk.Button(label="Import selected image")
    btnimport.connect("clicked", self.on_import_wallpaper)
    hbox12.pack_end(btnimport, False, False, 10)
    hbox12.pack_start(label12, False, True, 10)

    hbox13 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    btnremove = Gtk.Button(label="Remove wallpaper")
    btnremove.set_size_request(180, 0)
    btnremove.connect("clicked", self.on_remove_wallpaper)
    hbox13.pack_end(btnremove, False, False, 10)

    scrolled = Gtk.ScrolledWindow()
    scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
    wallpaper_list = fn.get_grub_wallpapers()
    self.grub_theme_combo = Gtk.ComboBoxText()
    self.pop_themes_grub(self.grub_theme_combo, wallpaper_list, True)
    self.fb.set_valign(Gtk.Align.START)
    self.fb.set_max_children_per_line(6)
    self.fb.set_selection_mode(Gtk.SelectionMode.SINGLE)
    self.fb.connect("child-activated", self.on_grub_item_clicked)
    scrolled.add(self.fb)
    self.grub_theme_combo.connect("changed", self.on_grub_theme_change)

    hbox16 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    install_rebornos_grub = Gtk.Button(label="Install original grub theme of RebornOS - autoreboot")
    install_rebornos_grub.connect("clicked", self.on_click_install_orignal_grub_rebornos)
    hbox16.pack_end(install_rebornos_grub, False, False, 10)

    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    grub_apply = Gtk.Button(label="2. Choose and apply wallpaper")
    grub_apply.connect("clicked", self.on_set_grub_wallpaper)
    grub_reset = Gtk.Button(label="Reset to default Vimix wallpaper")
    grub_reset.connect("clicked", self.on_reset_grub_wallpaper)
    grub_reset_grub = Gtk.Button(label="Reset to the original grub theme")
    grub_reset_grub.connect("clicked", self.on_reset_grub)
    grub_reset_vimix = Gtk.Button(label="1. Apply the Vimix theme")
    grub_reset_vimix.connect("clicked", self.on_reset_grub_vimix)
    hbox9.pack_end(grub_reset_grub, False, False, 0)
    hbox9.pack_end(grub_apply, False, False, 0)
    hbox9.pack_end(grub_reset_vimix, False, False, 0)

    vboxStack4.pack_start(hbox3, False, False, 0) #title
    vboxStack4.pack_start(hbox4, False, False, 0) #seperator
    vboxStack4.pack_start(hbox10, False, False, 0) #scale
    vboxStack4.pack_start(hbox11, False, False, 0) #import
    vboxStack4.pack_start(hbox12, False, False, 0) #select wallpaper
    vboxStack4.pack_start(hbox13, False, False, 0) #select wallpaper
    vboxStack4.pack_start(scrolled, True, True, 0) #Preview
    vboxStack4.pack_end(hbox9, False, False, 0)# Buttons
    if fn.distr == "rebornos":
        vboxStack4.pack_end(hbox16, False, False, 0)# Buttons

