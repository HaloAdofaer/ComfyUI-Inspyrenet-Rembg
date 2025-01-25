from .Inspyrenet_Rembg import InspyrenetRembg, InspyrenetRembgAdvanced, InspyrenetRembgBlack

NODE_CLASS_MAPPINGS = {
    "InspyrenetRembg" : InspyrenetRembg,
    "InspyrenetRembgAdvanced" : InspyrenetRembgAdvanced,
    "InspyrenetRembgBlack" : InspyrenetRembgBlack,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InspyrenetRembg": "Inspyrenet Rembg",
    "InspyrenetRembgAdvanced": "Inspyrenet Rembg Advanced",
    "InspyrenetRembgBlack": "Inspyrenet Rembg Black",
}
__all__ = ['NODE_CLASS_MAPPINGS', "NODE_DISPLAY_NAME_MAPPINGS"]
