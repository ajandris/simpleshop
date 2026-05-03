from django import template
import os
from PIL import Image
from django.conf import settings
from urllib.parse import unquote

register = template.Library()

@register.filter
def thumbnail(url, width=400):
    if not url:
        return ""
    
    url = str(url)
    # Ensure url starts with MEDIA_URL
    if not url.startswith(settings.MEDIA_URL):
        return url
        
    relative_path = url[len(settings.MEDIA_URL):]
    relative_path = unquote(relative_path) # Decode URL encoding
    
    # Get the absolute file path
    full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
    # Ensure it uses os.sep
    full_path = full_path.replace('/', os.sep).replace('\\', os.sep)
    
    if not os.path.exists(full_path):
        return url
        
    name, ext = os.path.splitext(relative_path)
    thumb_relative = f"{name}_thumb{ext}"
    thumb_full = os.path.join(settings.MEDIA_ROOT, thumb_relative).replace('/', os.sep).replace('\\', os.sep)
    
    if not os.path.exists(thumb_full):
        try:
            img = Image.open(full_path)
            img.thumbnail((int(width), int(width)), Image.Resampling.LANCZOS)
            img.save(thumb_full)
        except Exception as e:
            print("Thumbnail generation error:", e)
            return url
            
    # Return the URL for the thumbnail
    # Convert os.sep to forward slash for URL
    thumb_relative_url = thumb_relative.replace(os.sep, '/')
    return f"{settings.MEDIA_URL}{thumb_relative_url}"
