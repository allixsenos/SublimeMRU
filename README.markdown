# Sublime Text 2 plugin: SublimeMRU

A "Most Recently Used" implementation, to quickly reopen recently closed files.

## Using

This plugin exposes the commands "Open recently closed file" and "Open recently closed files (panel)" in the File menu.

It also automatically binds to `ctrl+shift+t` on Windows and Linux, and `super+shift+t` on OSX. The panel version is bound to `ctrl+alt+shift+t` and `super+ctrl+shift+t`.

I've heard some people dislike plugins auto-binding stuff, so I'm open to removing the autobinding if enough people protest.


## Installing

First, you need to have `git` installed and in your `$PATH`. Afterwards you may need to restart Sublime Text 2 before the plugin will work.

### OSX

    $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    $ git clone git://github.com/allixsenos/SublimeMRU.git SublimeMRU

### Linux (Ubuntu like distros)

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone git://github.com/allixsenos/SublimeMRU.git SublimeMRU

### Windows 7:

    Copy the directory to: "C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages"

### Windows XP:

    Copy the directory to: "C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages"


## Credits

Based on and inspired by https://gist.github.com/gists/1133602 by jbjornson
