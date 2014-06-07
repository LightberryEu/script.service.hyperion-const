# Copyright (C) 2014 lightberry.eu
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
import subprocess, os
import xbmcaddon

__author__ = "Tomek (lightberry.eu)"
__url__ = "http://lightberry.eu"
__addonname__ = "Hyperion Constant"
__svn_url__ = ""
__credits__ = "Hyperion Constant plugin written and maintained by lightberry.eu"
__icon__ = "./icon.png"

__settings__ = xbmcaddon.Addon()
__addondir__ = __settings__.getAddonInfo('path')

delayTime = 5000
msgLine = ""
exceptionLine = ""

colors = {'black': '000000',
          'navy': '001F3F',
          'blue(full)': '0000FF',
          'blue': '0074D9',
          'aqua': '7FDBFF',
          'teal': '39CCCC',
          'olive': '3D9970',
          'green(full)': '00FF00',
          'green': '2ECC40',
          'lime': '01FF70',
          'yellow': 'FFDC00',
          'orange': 'FF851B',
          'red(full)': 'FF0000',
          'red': 'FF4136',
          'maroon': '85144B',
          'fuchsia': 'F012BE',
          'purple': 'B10DC9',
          'white': 'FFFFFF',
          'silver': 'DDDDDD',
          'gray': 'AAAAAA'}

if (__settings__.getSetting('customColor') == 'false'):
    if os.uname()[1] == "raspbmc":
        hyperion = "hyperion-remote --color "
    elif os.uname()[1] == "OpenELEC":
        hyperion = "/storage/hyperion/bin/hyperion-remote.sh --color "
    else :
        hyperion = "hyperion-remote --color "

    command = hyperion + colors[__settings__.getSetting('constColor')]
else:
    R = int(float(__settings__.getSetting('customColorR')))
    G = int(float(__settings__.getSetting('customColorG')))
    B = int(float(__settings__.getSetting('customColorB')))
    command = "hyperion-remote --color " + '{:02x}{:02x}{:02x}'.format(R, G, B)

subprocess.check_call(command, shell=True)



