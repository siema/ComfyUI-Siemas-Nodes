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
    FUNCTION = "main"

    def main(self, width, height, multiplier):

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
    FUNCTION = "main"

    def main(self, value):
        return (int(abs(value)),)
        
class Siema_Str2List_by_Newline:

    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"default": "", "forceInput": True})
            }
        }
        
    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("list",)
    FUNCTION = "main"

    def main(self, string):
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
    FUNCTION = "main"

    def main(self, list, index):
        return (list[index],)
        
class Siema_Create_RNG:

    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "forceInput": True})
            }
        }
        
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("rng",)
    FUNCTION = "main"

    def main(self, seed):

        rng = random.Random()
        rng.seed(seed)

        return (rng,)

    @classmethod
    def IS_CHANGED(self, seed):
        return float("NaN")
        
class Siema_Get_List_Random:

    def __init__(self):
        pass
        
    CATEGORY="Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "rng": (AnyType("*"), {"forceInput": True}),
                "list": ("LIST", {"forceInput": True}),
            }
        }
        
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "main"

    def main(self, list, rng):
        return (rng.choice(list),)

    @classmethod
    def IS_CHANGED(self, list, rng):
        return float("NaN")
        
class Siema_Set_Metadata:

    def __init__(self):
        pass

    CATEGORY="Siemas Nodes"
    OUTPUT_NODE = True
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": ""}),
                "value": ("STRING", {"default": "", "forceInput": True}),
            },
            "hidden": {
                "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }
    RETURN_TYPES = ()
    FUNCTION = "main"
    
    def main(self, name, value, extra_pnginfo):

        if extra_pnginfo is not None and name and value:
            extra_pnginfo[name] = value

        return (None,)

class Siema_String_List:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_1": ("STRING", {"default": "", "forceInput": True}),
            },
            "optional": {
                "string_2": ("STRING", {"default": "", "forceInput": True}),
                "string_3": ("STRING", {"default": "", "forceInput": True}),
                "string_4": ("STRING", {"default": "", "forceInput": True}),
                "string_5": ("STRING", {"default": "", "forceInput": True}),
                "string_6": ("STRING", {"default": "", "forceInput": True}),
                "string_7": ("STRING", {"default": "", "forceInput": True}),
                "string_8": ("STRING", {"default": "", "forceInput": True}),
                "string_9": ("STRING", {"default": "", "forceInput": True}),
            }
        }
    RETURN_TYPES = ("LIST",)
    FUNCTION = "run"

    CATEGORY = "Siemas Nodes"

    def run(self, string_1, string_2=None, string_3=None, string_4=None, string_5=None, string_6=None, string_7=None, string_8=None, string_9=None):

        string_list = [string_1,]

        if string_2 is not None:
            string_list.append(string_2)
        if string_3 is not None:
            string_list.append(string_3)
        if string_4 is not None:
            string_list.append(string_4)
        if string_5 is not None:
            string_list.append(string_5)
        if string_6 is not None:
            string_list.append(string_6)
        if string_7 is not None:
            string_list.append(string_7)
        if string_8 is not None:
            string_list.append(string_8)
        if string_9 is not None:
            string_list.append(string_9)

        return (string_list,)
        
class Siema_Multiple_String_Replace:

    def __init__(self):
        pass

    CATEGORY="Siemas Nodes"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"default": "", "forceInput": True}),
                "find_list": ("LIST", {"forceInput": True}),
                "replace_list": ("LIST", {"forceInput": True}),
            },
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "main"
    
    def main(self, string, find_list, replace_list):

        rcount = min(len(find_list), len(replace_list))
        for i in range(0, rcount):
            string = string.replace(find_list[i], replace_list[i])

        return (string,)
        
class Siema_Data_Select:

    def __init__(self):
        pass

    CATEGORY = "Siemas Nodes"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "should_output_a": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "a_value": (AnyType("*"), {"forceInput": True, "lazy": True}),
                "b_value": (AnyType("*"), {"forceInput": True, "lazy": True}),
            }
        }
        
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("value",)
    FUNCTION = "main"

    def main(self, should_output_a, a_value=None, b_value=None):
        if should_output_a:
            return (a_value,)
        else:
            return (b_value,)

    def check_lazy_status(self, should_output_a, a_value=None, b_value=None):
        if should_output_a:
            return ["a_value"]
        else:
            return ["b_value"]

class Siema_Dict_Set:

    def __init__(self):
        pass
        
    CATEGORY = "Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "value": (AnyType("*"), {"forceInput": True})
            },
            "optional": 
            {
                "dict": (AnyType("*"), {"forceInput": True}),
            }
        }
        
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("dict",)
    FUNCTION = "main"

    def main(self, key, value, dict={}):

        dict[key] = value

        return (dict,)

    @classmethod
    def IS_CHANGED(self, key, value, dict={}):
        return float("NaN")

class Siema_Dict_Get:

    def __init__(self):
        pass
        
    CATEGORY = "Siemas Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dict": (AnyType("*"), {"forceInput": True}),
                "key": ("STRING", {"default": ""})
            }
        }
        
    RETURN_TYPES = (AnyType("*"), AnyType("*"),)
    RETURN_NAMES = ("dict", "value",)
    FUNCTION = "main"

    def main(self, dict, key):
        return (dict, dict[key])

    @classmethod
    def IS_CHANGED(self, dict, key):
        return float("NaN")

NODE_CLASS_MAPPINGS = {
    "Multiply Resolution (Siema)": Siema_Res_Multiply,
    "Absolute Value (Siema)": Siema_Int_Abs,
    "Split String By Lines (Siema)": Siema_Str2List_by_Newline,
    "Get List Item (Siema)": Siema_Get_List,
    "Create RNG (Siema)": Siema_Create_RNG,
    "Get Random List Item (Siema)": Siema_Get_List_Random,
    "Set Metadata (Siema)": Siema_Set_Metadata,
    "String List (Siema)": Siema_String_List,
    "Multiple Replace (Siema)": Siema_Multiple_String_Replace,
    "Data Selector (Siema)": Siema_Data_Select,
    "Dict Set (Siema)": Siema_Dict_Set,
    "Dict Get (Siema)": Siema_Dict_Get,
}
