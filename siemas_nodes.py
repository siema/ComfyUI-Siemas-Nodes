import random

class Siema_Res_Multiply:
    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 16, "max": 8192, "forceInput": True}),
                "height": ("INT", {"default": 512, "min": 16, "max": 8192, "forceInput": True}),
                "multiplier": ("FLOAT", {"default": 2.0, "min": 1, "max": 10000}),
            }
        }
        
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width","height",)
    FUNCTION = "multiply"

    def multiply(self, width, height, multiplier):
        adj_width = width*multiplier
        adj_height = height*multiplier
        return (int(adj_width),int(adj_height),)
        
class Siema_Int_Abs:
    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0, "forceInput": True})
            }
        }
        
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("abs_value",)
    FUNCTION = "intabs"

    def intabs(self, value):
        return (int(abs(value)),)
        
class Siema_Str2List_by_Newline:
    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"forceInput": True})
            }
        }
        
    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("list",)
    FUNCTION = "split"

    def split(self, string):
        return (string.splitlines(),)
        
# taken from https://github.com/kenjiqq/qq-nodes-comfyui/tree/main
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False
        
class Siema_Get_List:
    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("LIST", {"forceInput": True}),
                "index": ("INT", {"default": 0})
            }
        }
        
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_list"

    def get_list(self, list, index):
        return (list[index],)
        
class Siema_Get_List_Random:
    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("LIST", {"forceInput": True}),
                "seed": ("INT", {"forceInput": True})
            }
        }
        
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_list_rand"

    def get_list_rand(self, list, seed):
        random.seed(seed)
        return (random.choice(list),)
        
class Siema_Set_Metadata:

    CATEGORY="Siemas Nodes"
    OUTPUT_NODE = True
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING",),
                "value": ("STRING", {"forceInput": True, "default": ""}),
            },
            "hidden": {
                "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }
    RETURN_TYPES = ()
    FUNCTION = "set_metadata"
    
    def set_metadata(self, name, value, extra_pnginfo):
        if extra_pnginfo is not None and name and value:
            extra_pnginfo[name] = value
        return (None,)

NODE_CLASS_MAPPINGS = {
    "Multiply Resolution (Siema)": Siema_Res_Multiply,
    "Absolute Value (Siema)": Siema_Int_Abs,
    "Split String By Lines (Siema)": Siema_Str2List_by_Newline,
    "Get List Item (Siema)": Siema_Get_List,
    "Get Random List Item (Siema)": Siema_Get_List_Random,
    "Set Metadata (Siema)": Siema_Set_Metadata,
}
