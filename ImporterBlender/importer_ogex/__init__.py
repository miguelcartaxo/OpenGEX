# =============================================================
# 
#  Open Game Engine Exchange
#  http://opengex.org/
# 
#  Import plugin for Blender
#  by Miguel Cartaxo
#
#  Version 2.0
# 
# 
# =============================================================

import bpy

from .ImportOpenGEX import OpenGexImporter

bl_info = {
    "name": "OpenGEX Importer (.ogex)",
    "description": "Terathon Software's OpenGEX Importer",
    "author": "Miguel Cartaxo",
    "version": (2, 0, 0, 0),
    "blender": (4, 5, 2),
    "location": "File > Import-Export",
    "wiki_url": "http://opengex.org/",
    "category": "Import-Export"}

def menu_func(self, context):
    self.layout.operator(OpenGexImporter.bl_idname, text = "OpenGEX (.ogex)")

def register():
    bpy.utils.register_class(OpenGexImporter)
    bpy.types.TOPBAR_MT_file_import.append(menu_func)

def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func)
    bpy.utils.unregister_class(OpenGexImporter)
