#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import Functions as fn
import threading
import datetime

from Functions import os, GLib


def setMessage(label, message):
    label.set_markup("<i>" + message + "</i>")


def setProgress(prog, value):
    prog.set_fraction(value)


def skel_check(self):
    passes = True
    text = self.treeView.get_model()
    if len(text) >= 1:
        for item in text:
            if not "/etc/skel" in item[0]:
                passes = False
        if passes == True:

            if self.switch.get_active() == True:
                setMessage(self.label_info1, "Running Backup")
                t1 = threading.Thread(target=processing,
                                    args=(self, text, self.label_info1, self.progressbar1))
                t1.daemon = True
                t1.start()
            else:
                setMessage(self.label_info1, "Running Skel")
                t1 = threading.Thread(target=skel_run, args=(self, text,))
                t1.daemon = True
                t1.start()
        else:
            fn.MessageBox(self, "Failed!!", "It looks like your out of the /etc/skel directory")
    else:
        button_toggles(self, True)

def skel_run(self, cat):
    count = cat.__len__()
    if(count > 0):
        prog = (count/count)/count
        self.ecode = 0
        for item in cat:
            # print(item[0])
            GLib.idle_add(setProgress, self.progressbar1, self.progressbar1.get_fraction() + prog)
            old = item[0]
            new = old.replace("/etc/skel", fn.home)
            if os.path.isdir(old):
                fn.copy_func(old,  os.path.split(new)[0], True)
            if os.path.isfile(old):
                fn.copy_func(old, new)
            fn.permissions(new)
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setMessage,self.label_info1, "Idle ...")
    GLib.idle_add(setProgress, self.progressbar1, 0)


# ===========================================
#		RESTORE BACKUP FUNCTION
# ===========================================
def restore_item(self):
    backup_path = fn.home + "/" + fn.bd + "/" + self.backs.get_active_text() + "/"
    treeselect = self.treeView2.get_selection()
    (model, pathlist) = treeselect.get_selected_rows()
    if len(pathlist) > 0:
        GLib.idle_add(setProgress, self.progressbar, 0.1)

        GLib.idle_add(self.progressbar.set_pulse_step, 0.2)
        timeout_id = None
        timeout_id = GLib.timeout_add(100, do_pulse, None, self, self.progressbar)

        for path in pathlist :
            tree_iter = model.get_iter(path)
            value = model.get_value(tree_iter,0)
            file_path = backup_path + value
        if value.__len__() > 0:
            if os.path.isfile(file_path):
                fn.copy_func(file_path, fn.home + "/" + value.split("-backup")[0])
                fn.permissions(fn.home + "/" + value.split("-backup")[0])
            elif os.path.isdir(file_path):
                dirs = fn.home + "/" +  value.split("-backup")[0]
                # old_dir = fn.home + "/" + value
                GLib.idle_add(setMessage,self.label_info, "Removing Existing Destination Folder ...")
                fn.subprocess.call(["rm", "-rf", dirs])
                GLib.idle_add(setMessage,self.label_info, "Copying " + value + " to " + value.split("-backup")[0])
                fn.copy_func(file_path, dirs, True)
                fn.permissions(dirs)

    GLib.source_remove(timeout_id)
    timeout_id = None
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setMessage,self.label_info, "Idle ...")
    GLib.idle_add(setProgress, self.progressbar, 0)
# ===========================================
#		DELETE BACKUP FUNCTION
# ===========================================
def Delete_Backup(self):
    count = os.listdir(fn.home + "/" + fn.bd).__len__()

    if count > 0:
        GLib.idle_add(setMessage,self.label_info, "Removing ...")
        GLib.idle_add(setProgress, self.progressbar, 0.3)
        for filename in os.listdir(fn.home + "/" + fn.bd):
            if filename == self.backs.get_active_text():
                fn.shutil.rmtree(fn.home + "/" + fn.bd + "/" + filename)
        GLib.idle_add(refresh, self)
        GLib.idle_add(refresh_inner, self)
        GLib.idle_add(setProgress, self.progressbar, 1)
        GLib.idle_add(fn.show_in_app_notification,self, "Config backups cleaned.")
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setMessage,self.label_info, "Idle ...")
    GLib.idle_add(setProgress, self.progressbar, 0)


def Delete_Inner_Backup(self):
    count = os.listdir(fn.home + "/" + fn.bd).__len__()

    if count > 0:
        GLib.idle_add(setMessage,self.label_info, "Removing ...")
        GLib.idle_add(setProgress, self.progressbar, 0.3)
        treeselect = self.treeView2.get_selection()

        for filename in os.listdir(fn.home + "/" + fn.bd + "/" + self.backs.get_active_text()):
            (model, pathlist) = treeselect.get_selected_rows()
            for path in pathlist :
                tree_iter = model.get_iter(path)
                value = model.get_value(tree_iter,0)
                if filename == value:
                    # print(value)
                    if os.path.isdir(fn.home + "/" + fn.bd + "/" + self.backs.get_active_text() + "/" + filename):
                        fn.shutil.rmtree(fn.home + "/" + fn.bd + "/" + self.backs.get_active_text() + "/" + filename)
                    elif os.path.isfile(fn.home + "/" + fn.bd + "/" + self.backs.get_active_text() + "/" + filename):
                        os.unlink(fn.home + "/" + fn.bd + "/" + self.backs.get_active_text() + "/" + filename)

        GLib.idle_add(refresh_inner, self)
        GLib.idle_add(setProgress, self.progressbar, 1)
        GLib.idle_add(fn.show_in_app_notification,self, "Config backups cleaned.")
        GLib.idle_add(setMessage,self.label_info, "Idle ...")
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setProgress, self.progressbar, 0)

def Flush_All(self):
    count = os.listdir(fn.home + "/" + fn.bd).__len__()

    if count > 0:
        count = ((count/count)/count)
        GLib.idle_add(setMessage,self.label_info, "Deleting Backup")
        for filename in os.listdir(fn.home + "/" + fn.bd):
            if os.path.isdir(fn.home + "/" + fn.bd + "/" + filename):
                GLib.idle_add(setProgress, self.progressbar, self.progressbar.get_fraction() + count)
                fn.shutil.rmtree(fn.home + "/" + fn.bd + "/" + filename)


        GLib.idle_add(fn.show_in_app_notification,self, "Backups directory has been cleaned.")
        GLib.idle_add(refresh, self)
        GLib.idle_add(refresh_inner, self)
        GLib.idle_add(setProgress, self.progressbar, 0)
    GLib.idle_add(button_toggles, self, True)
    GLib.idle_add(setMessage,self.label_info, "Idle ...")
# ===========================================
#		REFRESH FUNCTION
# ===========================================
def refresh(self):
    if not os.path.exists(fn.home + "/" + fn.bd):
        os.makedirs(fn.home + "/" + fn.bd)

    self.backs.get_model().clear()
    BACKUPS_CATS = []

    for filename in os.listdir(fn.home + "/" + fn.bd):
        if os.path.isdir(fn.home + "/" + fn.bd + "/" + filename):
            BACKUPS_CATS.append(filename)

    for item in BACKUPS_CATS:
        self.backs.append_text(item)

    self.backs.set_active(0)


def refresh_inner(self):
    count = os.listdir(fn.home + "/" + fn.bd).__len__()
    active_text = "".join([str(self.backs.get_active_text()), ""])

    if count > 0:
        if os.path.isdir(fn.home + "/" + fn.bd + "/" + active_text):
            self.store2.clear()

            for filename in os.listdir(fn.home + "/" + fn.bd + "/" + active_text):
                self.store2.append([filename])

    else:
        self.store2.clear()


def bash_upgrade(self):

    now = datetime.datetime.now()
    GLib.idle_add(setMessage,self.label_info1, "Running Backup")

    fn.check_backups(now)

    if os.path.isfile(fn.home + '/.bashrc'):
        fn.copy_func(
            fn.home + '/.bashrc', fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.bashrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))
        fn.permissions(fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.bashrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))

    GLib.idle_add(setMessage,self.label_info1, "Upgrading Bashrc")

    if os.path.isfile("/etc/skel/.bashrc"):
        fn.copy_func("/etc/skel/.bashrc", fn.home + "/.bashrc")
        fn.permissions(fn.home + "/.bashrc")
        GLib.idle_add(setMessage,self.label_info1, ".bashrc upgrade done")

        GLib.idle_add(fn.show_in_app_notification,self, "bashrc upgraded")
    else:
        GLib.idle_add(fn.MessageBox,self,
            "Failed!!", "bashrc upgrade failed, you dont have a .bashrc in skel")

    fn.source_shell(self)

    GLib.idle_add(setMessage,self.label_info1, "Idle ...")
    GLib.idle_add(refresh,self)
    GLib.idle_add(button_toggles,self,True)

def button_toggles(self, state):
    self.btn2.set_sensitive(state)
    self.btn5.set_sensitive(state)
    self.btn9.set_sensitive(state)
    self.btn4.set_sensitive(state)
    self.btn10.set_sensitive(state)
    self.btn11.set_sensitive(state)
    self.btn12.set_sensitive(state)
    self.browse.set_sensitive(state)
    self.remove.set_sensitive(state)

def do_pulse(data, self, progress):
    progress.pulse()
    return True

def processing(self, active_text, label, progress):
    now = datetime.datetime.now()

    fn.check_backups(now)

    GLib.idle_add(setProgress, progress, 0.1)

    GLib.idle_add(self.progressbar.set_pulse_step, 0.2)
    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self, progress)

    # ============================
    #       CONFIG
    # ============================
    GLib.idle_add(setMessage,label, "Backing up .config")
    fn.copy_func(fn.home + '/.config', fn.home + '/' + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.config-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"), True)
    fn.permissions(fn.home + '/' + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.config-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"))

    # GLib.idle_add(setProgress, self, 0.3)
    GLib.source_remove(timeout_id)
    timeout_id = None

    GLib.idle_add(setProgress, progress, 0.5)
    # ============================
    #       LOACAL
    # ============================
    GLib.idle_add(setMessage,label, "Backing up .local")
    fn.copy_func(fn.home + '/.local', fn.home + '/' + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.local-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"), True)
    fn.permissions(fn.home + '/' + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.local-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"))

    GLib.idle_add(setProgress, progress, 0.7)
    # ============================
    #       BASH
    # ============================

    if os.path.isfile(fn.home + '/.bashrc'):
        GLib.idle_add(setMessage,label, "Backing up .bashrc")
        fn.copy_func(
            fn.home + '/.bashrc', fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.bashrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))
        fn.permissions(fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.bashrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))

    GLib.idle_add(setProgress, progress, 0.8)
    # ============================
    #       ZSH
    # ============================
    if os.path.isfile(fn.home + '/.zshrc'):
        GLib.idle_add(setMessage,label, "Backing up .zshrc")
        fn.copy_func(
            fn.home + '/.zshrc', fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.zshrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))
        fn.permissions(fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.zshrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))
    GLib.idle_add(setProgress, progress, 0.9)

    # ============================
    #       CONKY
    # ============================
    if os.path.exists(fn.home + '/.lua'):
        GLib.idle_add(setMessage,label, "Backing up .lua")
        fn.copy_func(fn.home + '/.lua', fn.home + '/' + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.lua-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"), True)
        fn.permissions(fn.home + '/' + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + '/.lua-backup-' +
                now.strftime("%Y-%m-%d %H:%M:%S"))

    if os.path.isfile(fn.home + '/.conkyrc'):
        GLib.idle_add(setMessage,label, "Backing up .cokyrc")
        fn.copy_func(
            fn.home + '/.conkyrc', fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.conkyrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))
        fn.permissions(fn.home + "/" + fn.bd + "/Backup-" + now.strftime("%Y-%m-%d %H") + "/.conkyrc-backup-" +
            now.strftime("%Y-%m-%d %H:%M:%S"))

    GLib.idle_add(setProgress, progress, 1.0)

    GLib.idle_add(setMessage, label, "Done")


    if not active_text == "BACKUP":
        pass
        GLib.idle_add(setMessage, label, "Running Skel")

        GLib.idle_add(skel_run, self, active_text)
    else:
        GLib.idle_add(button_toggles,self,True)
        GLib.idle_add(setMessage,label, "Idle...")
        GLib.idle_add(setProgress,progress,0)


    GLib.idle_add(refresh, self)
    GLib.idle_add(refresh_inner, self)