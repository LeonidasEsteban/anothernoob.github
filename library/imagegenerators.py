from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, Adjust

class Suggestion_thumb(ImageSpec):
    processors = [ResizeToFill(256, 256),Adjust(brightness = 0.5, contrast = 0.9)]
    format = 'JPEG'
    options = {'quality': 80}

register.generator('library:suggestion_thumb', Suggestion_thumb)