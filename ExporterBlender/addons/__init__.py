# =============================================================
# 
#  Open Game Engine Exchange
#  http://opengex.org/
# 
#  Export plugin for Blender
#  by Eric Lengyel
#    updated for blender 2.80 by Joel Davis
#    updated with some fixes by Miguel Cartaxo
#
#  Version 2.9
# 
#  Copyright 2017, Terathon Software LLC
# 
#  This software is licensed under the Creative Commons
#  Attribution-ShareAlike 3.0 Unported License:
# 
#  http://creativecommons.org/licenses/by-sa/3.0/deed.en_US
# 
# =============================================================

import bpy

from .ExportOpenGEX import OpenGexExporter


def menu_func(self, _):
    self.layout.operator(OpenGexExporter.bl_idname, text="Original OpenGEX (.ogex)")


def register():
    bpy.utils.register_class(OpenGexExporter)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)
    return


def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)
    bpy.utils.unregister_class(OpenGexExporter)
    return
