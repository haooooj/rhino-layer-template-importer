"""hao with GPT4"""
import rhinoscriptsyntax as rs
import Rhino
import System
import os

def create_layers_recursively(doc, template_layers, created_layers, parent_id):
    """
    Recursively create layers whose ParentLayerId == parent_id.
    template_layers: dict {GUID: File3dmLayer}
    created_layers: dict {GUID: Rhino.DocObjects.Layer.Id} of created layers
    parent_id: GUID or System.Guid.Empty for root layers
    """
    for layer_id, template_layer in template_layers.items():
        if template_layer.ParentLayerId == parent_id:
            # Create a new Rhino layer
            new_layer = Rhino.DocObjects.Layer()
            new_layer.Name = template_layer.Name
            new_layer.Color = template_layer.Color
            new_layer.PlotColor = template_layer.PlotColor
            new_layer.LinetypeIndex = template_layer.LinetypeIndex
            new_layer.IsVisible = template_layer.IsVisible
            new_layer.IsLocked = template_layer.IsLocked

            # If this layer has a parent (not the root), set the ParentLayerId
            if parent_id != System.Guid.Empty:
                # The parent's layer must exist in created_layers to set parent
                # Find which created layer has this parent_id
                # Actually, we know parent's layer Id because we stored it in created_layers
                # created_layers maps template layer Id to doc layer's Id
                # We need to find which template layer corresponded to parent_id
                # Let's invert created_layers or store a separate mapping of parent's template Id to doc layer Id

                # Actually, we know the parent's template_layer is the one with Id=parent_id
                # We can look it up: parent's doc layer Id is in created_layers[parent_id]
                parent_doc_layer_id = created_layers[parent_id]
                new_layer.ParentLayerId = parent_doc_layer_id

            # Add the layer to the doc
            layer_index = doc.Layers.Add(new_layer)
            if layer_index < 0:
                print("Failed to add layer '{}'.".format(template_layer.FullPath))
            else:
                # Store the created layer's Id so children can reference it
                created_layers[layer_id] = doc.Layers[layer_index].Id
                print("Added layer '{}'.".format(template_layer.FullPath))

                # Recursively create sublayers of this layer
                create_layers_recursively(doc, template_layers, created_layers, layer_id)

def import_layers_from_file(template_file):
    # Check if the file exists
    if not os.path.exists(template_file):
        print("Template file not found:", template_file)
        return

    # Load the template file using File3dm
    file_3dm = Rhino.FileIO.File3dm.Read(template_file)
    if file_3dm is None:
        print("Failed to read the template file.")
        return

    doc = Rhino.RhinoDoc.ActiveDoc

    # Build a dictionary of template layers keyed by their Id
    template_layers = {layer.Id: layer for layer in file_3dm.Layers}

    # Dictionary to store created layers: {template_layer_id: doc_layer_id}
    created_layers = {}

    # First, create all root layers (those with ParentLayerId == System.Guid.Empty)
    create_layers_recursively(doc, template_layers, created_layers, System.Guid.Empty)

    # Redraw views
    doc.Views.Redraw()

def main():
    # Prompt user to select the template file
    filter = "Rhino 3D Models (*.3dm)|*.3dm||"
    template_file = rs.OpenFileName("Select the layer template file", filter)
    if template_file:
        import_layers_from_file(template_file)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
