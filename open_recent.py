import sublime
import sublime_plugin
import os

# Plugin to provide access to the history of accessed files, based on
# https://gist.github.com/gists/1133602 by jbjornson

HISTORY_SETTINGS_FILE = 'SublimeMRU.sublime-settings'
HISTORY_MAX_ENTRIES = 100


def get_history():
    """load the history using sublime's built-in functionality for accessing settings"""
    return sublime.load_settings(HISTORY_SETTINGS_FILE)


def save_history(history):
    """save the history using sublime's built-in functionality for accessing settings"""
    history = clean_history(history)
    sublime.save_settings(HISTORY_SETTINGS_FILE)


def clean_history(history):
    """clean the history of files that no longer exist"""
    for historytype in ['closed', 'opened']:
        file_history = history.get(historytype, [])
        missing_files = []
        for filename in file_history:
            if not os.path.exists(filename):
                missing_files.append(filename)

        for filename in missing_files:
            while filename in file_history:
                file_history.remove(filename)

        history.set(historytype, file_history)

    return history


class OpenRecentlyClosedFileEvent(sublime_plugin.EventListener):
    """class to keep a history of the files that have been opened and closed"""

    def on_close(self, view):
        self.add_to_history(view, 'closed', 'opened')

    def on_load(self, view):
        self.add_to_history(view, 'opened', 'closed')

    def add_to_history(self, view, add_to_setting, remove_from_setting):
        filename = os.path.normpath(view.file_name()) if view.file_name() else None
        if filename != None:
            history = get_history()
            add_to_list = history.get(add_to_setting, [])
            remove_from_list = history.get(remove_from_setting, [])

            # remove this file from both of the lists
            while filename in remove_from_list:
                remove_from_list.remove(filename)
            while filename in add_to_list:
                add_to_list.remove(filename)

            # add this file to the top of the "add_to_list" (but only if the file actually exists)
            if os.path.exists(filename):
                add_to_list.insert(0, filename)

            # write the history back (making sure to limit the length of the histories)
            history.set(add_to_setting, add_to_list[0:HISTORY_MAX_ENTRIES])
            history.set(remove_from_setting, remove_from_list[0:HISTORY_MAX_ENTRIES])

            save_history(history)


class OpenRecentlyClosedFileCommand(sublime_plugin.WindowCommand):
    """class to either open the last closed file or show a quick panel with the file access history (closed files first)"""

    def run(self, show_quick_panel=False):
        self.reload_history()
        if show_quick_panel:
            self.window.show_quick_panel(self.display_list, self.open_file, True)
        else:
            self.open_file(0)

    def reload_history(self):
        # get the file history (put the list of closed files first)
        history = get_history()
        self.file_list = history.get('closed', []) + history.get('opened', [])

        # prepare the display list with file name and path separated
        self.display_list = []
        for filePath in self.file_list:
            self.display_list.append([os.path.basename(filePath), os.path.dirname(filePath)])

    def open_file(self, index):
        if index >= 0 and len(self.file_list) > index:
            self.window.open_file(self.file_list[index])
