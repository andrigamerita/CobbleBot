# CobbleBot
Minecraft Bot/Macro designed to create Cobblestone (Lava/Water) stairs to grief servers efficiently.

---

## Native Python version (3.8.3, for Windows and GNU/Linux)
It can be found in the "Source/Python" folder. 

### Dependencies/Installation
The [_mouse_](https://github.com/boppreh/mouse) and [_keyboard_](https://github.com/boppreh/keyboard) libraries are required for it to work.

Download and install them (running `setup.py install` as admin) from the mentioned repos or from **PyPI**:
```pip install mouse```,
```pip install keyboard```

### How to use
1. In your Minecraft world/server, create a platform like the one in [this picture](https://raw.githubusercontent.com/andrigamerita/CobbleBot/master/Doc/Img/Platform-1.png), and point at the central block.
2. Run the script (in a terminal window, `python CobbleBotPython.py` on Windows or `python3 CobbleBotPython.py` on Linux)
3. Wait for it to finish! Note that the focus must remain on the Minecraft window with no open menus (like inventory or options) for the Bot to work.

You must also keep in mind that, with the Bot default settings (that is, no switches used), the Place/Interact button, the Hotbar 8 button, and the Hotbar 9 button, must be set (respectively) to: Right Mouse button, Number row 8, and Number row 9. 
A Lava and a Water bucket must also be present (respectively) in the Slot 8 and Slot 9 of the hotbar.

### Command-line switches
* `-b`, `--block`, `[number 0-255]`, Specifies how many blocks have already been generated. Default is 0. Useful if you start the Bot, then stop it, and want to continue using it later on the same cobblestone stairs.
* `-c`, `--click`, `[button]`, Specifies the button that acts as the Place/Interact in Minecraft; default is Right Mouse (MouseRight).
* `-l`, `--lava`, `[button]`, Specifies the button that selects Lava in the hotbar; default is Numrow 8 (eight).
* `-w`, `--water`, `[button]`, Specifies the button that selects Water in the hotbar; default is Numrow 9 (nine).

#### Customizing [button] inputs
* Mouse: Left and Right mouse buttons are supported. More info: [Official Mouse API](https://github.com/boppreh/mouse#api).
⋅⋅* `MouseLeft`: Left mouse button
⋅⋅* `MouseRight`: Right mouse button
* Keyboard: Every key should be supported. See the [Official Keyboard API](https://github.com/boppreh/keyboard#api) for a more in-depth explanation.
⋅⋅* Letter buttons: the corresponding letter. (Example: button "A" is `a`)
⋅⋅* Number row buttons: the corresponding number, written in letters. (Example: button "5" is `five`)
⋅⋅* Any button through scancodes. (Example: Spacebar is `57`)
⋅⋅* ...

### Known issues
* On GNU/Linux, there might be some problems installing the mouse and keyboard modules, and that may cause the script to be partially or completely unusable. That's a problem regarding python and the OS.
* Also on GNU/Linux, the script must be run as root, or with sudo, due to a limitation of the libraries.

---

## License
CobbleBot is licensed under the GPLv3 license. You should have received a copy of it along with this program. If not, visit [gnu.org](https://www.gnu.org/licenses/gpl-3.0.en.html).

You are allowed to run this program, read the source code, create modified copies, and share original or modified copies, as long as every original copyright notice is kept and the software uses the same (or similar) license as the original. This also means you can't use my code in software released under a proprietary license.

Copyright (C) 2020, OctoAndri