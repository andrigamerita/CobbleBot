# CobbleBot
Minecraft Bot/Macro designed to create Cobblestone (Lava/Water) stairs to grief servers efficiently.

---

## Native Python version
It can be found in the "Source/Python" folder. 

### Dependencies/Installation
The [_mouse_](https://github.com/boppreh/mouse) and [_keyboard_](https://github.com/boppreh/keyboard) libraries are required for it to work.

Download and install them (running `setup.py install` as admin) from the mentioned repos or from **PyPI**:
    pip install mouse
    pip install keyboard

### How to use
1. In your Minecraft world/server, create a platform like the one in [this picture](), pointing at the central block.
2. Run the script (in a terminal window, `python CobbleBotPython.py` on Windows or `python3 CobbleBotPython.py` on Linux)
3. Wait for it to finish! Note that the focus must remain on the Minecraft window with no open menus (like inventory or options) for the Bot to work.

You must also keep in mind that, with the Bot default settings (that is, no switches used)

### Command-line switches
* -b, --block, Specifies how many blocks have already been generated. Default is 0. Useful if you start the Bot, then stop it, and want to continue using it later on the same cobblestone stairs.
* -c, --click, Specifies the button that acts as the Place/Interact in Minecraft; default is Right Mouse (MouseRight).
* -l, --lava, Specifies the button that selects Lava in the hotbar; default is Numrow 8 (eight).
* -w, --water, Specifies the button that selects Water in the hotbar; default is Numrow 9 (nine).

#### Customizing inputs
TODO.

---

## License
CobbleBot is licensed under the GPLv3 license. You should have received a copy of it along with this program. If not, visit [gnu.org](https://www.gnu.org/licenses/gpl-3.0.en.html).

You are allowed to run this program, read the source code, create modified copies, and share original or modified copies, as long as every original copyright notice is kept and the software uses the same (or similar) license as the original. This also means you can't use my code in software released under a proprietary license.

Copyright (C) 2020, OctoAndri