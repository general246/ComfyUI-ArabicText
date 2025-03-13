"""
@author: ShahKoorosh
@title: ComfyUI-ArabicText
@nickname: ArabicText
@description: A powerful ComfyUI node for rendering text with advanced styling options, including full support for Persian/Farsi and Arabic scripts.
"""

from .ArabicText import ArabicText

NODE_CLASS_MAPPINGS = {
    "ArabicText": ArabicText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ArabicText": "ArabicText",
}
