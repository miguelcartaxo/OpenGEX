# OpenGEX Blender Exporter

This contains an Export plugin for OpenGEX files. 

Uses python 3. Tested with Blender 4.5.

## Installation

To install go to Blender Preferences -> Addons -> "Install from disk..." and select the export_ogex.zip file. If that zip does not exist you could created from the export_ogex folder, it has the same contents.

## Materials

To export materials they must be set up with the `Principled BSDF` shader. The following parameters are currently exported:

* `Base Color` is exported as `diffuse` in the OGEX Material
* `Specular` is exported as `specular`
* `Roughness` is exported as `roughness`
* `Metallic` is exported as `metalness` 
* `Emission` is exported as `emission`. Note that using a separate Emission shader with a Shader Mix is not supported currently.
* `Alpha` is exported as `opacity`. 
* `Normal` is exported as `normal`. Bump/displacement maps are not exported, you must bake these before exporting.

If there are Image textures connected directly to these paramers they will be included in the ogex material.

## Limitations

* UV transforms are ignored in textures.

## Blender debugging setup

- Download VS Code;
- Install python 3, specific version will depend on Blender's python version;
- Install VS Code pythons extension. Go to View -> Extensions, search for python;
- Download https://github.com/AlansCodeLog/blender-debugger-for-vscode ;
- Create a folder to put the unzip debugger plugin. Should be <path_to_chosen_folder>/addons/<plugin_folder>, copy the unzipped folder;
- In Blender, go to Edit -> Preferences -> Addons and search for Debugger for VS Code and enable it;
- Enable Developer Extras in Blender, Edit -> Preferences -> Interface -> Developer Extras;
- A new Experimental tab should appear on the right, go to Experimental and enable Extensions Debug;
- Search by pressing F3, and run Start Debug Server for VS Code, this will make the blender process look for VS code attach;
- In VS Code, open the *installed* plugin folder, go to Run and Debug tab and create a new configuration;
- A launch.json file will be created. Change the contents of the "configuration" attribute to the following:

```
{
    "name": "Python: Attach",
    "type": "python",
    "request": "attach",
    "port": 5678, //careful, this used to be 3000 in older versions of vscode and this addon
    "host": "localhost"
}
```

More info in https://github.com/AlansCodeLog/blender-debugger-for-vscode.
