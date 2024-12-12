# rhino-layer-template-importer
A Python-based utility script for Rhino 3D that automates the importing of layered structures from a template `.3dm` file.

This Python script streamlines the process of importing layered structures from a template `.3dm` file into your current Rhino 3D environment. By automating the creation of layers and nested sublayers, it ensures that complex layer hierarchies can be quickly and reliably reproduced, maintaining consistency across multiple projects and files.

## What Does This Script Do?

- **Load a Template File**: The script reads a selected `.3dm` file containing a predefined layer structure.

- **Automated Process**: With a single file selection, all desired layers are imported without the need for manual recreation.

## How to Use the Command

1. **Select a Template File**:  
   After running the script, you will be prompted to select a `.3dm` file containing the desired layer structure. Navigate to your template file and confirm.

2. **Automatic Layer Creation**:  
   The script will read the template file and automatically create all layers and sublayers in your current Rhino document. Once completed, a success message will appear for each newly created layer.

3. **Review the Result**:  
   Check the **Layers** panel in Rhino. You should see the recreated hierarchy, with layers and sublayers matching those in the template.

4. **Redraw the Views**:  
   The script will refresh your views automatically, ensuring the new layers are immediately visible and ready for use.

## How to Use the Script

### Method 1 Run the Python Script in Rhino

1. Type `_RunPythonScript` in the command line.
2. Browse to the location where you saved the script and select it.

### Method 2 Creating a Button or Alias for Easy Access (Optional)

If you plan to use this script frequently, you can create a button or an alias for quick access.

#### Creating a Toolbar Button

1. **Right-click** on an empty area of the toolbar and select **New Button**.
2. In the **Button Editor**:

   - **Left Button Command**:
     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\2pt_move.py"
     ```
     Replace `FullPathToYourScript` with the actual file path where you saved the script.
   - **Tooltip and Help**: Add a description for the button's functionality.
   - **Set an Icon (Optional)**: You can assign an icon to the button for easier identification.

#### Creating an Alias

1. Go to **Tools > Options** and select the **Aliases** tab.
2. **Create a New Alias**:

   - **Alias**: Choose a short command name, e.g., `m2`.
   - **Command Macro**:
     ```plaintext
     _-RunPythonScript "FullPathToYourScript\2pt_move.py"
     ```
     Again, replace `FullPathToYourScript` with the actual path.

3. **Use the Alias**: Type the alias (e.g., `m2`) into the command line and press **Enter** to run the script.
