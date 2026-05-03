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
    if not url.startswith(settings.MEDIA_URL):
        return url
        
    relative_path = unquote(url[len(settings.MEDIA_URL):])
    full_path = os.path.join(settings.MEDIA_ROOT, relative_path).replace('/', os.sep).replace('\\', os.sep)
    
    # If original file doesn't exist, try webp
    if not os.path.exists(full_path):
        name, _ = os.path.splitext(full_path)
        if os.path.exists(name + '.webp'):
            full_path = name + '.webp'
            relative_path = os.path.splitext(relative_path)[0] + '.webp'
        else:
            return url # File really doesn't exist
            
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
            
    return f"{settings.MEDIA_URL}{thumb_relative.replace(os.sep, '/')}"

@register.filter
def resolve_url(url):
    """Ensures the URL points to a file that actually exists (handles .webp fallback)"""
    if not url:
        return ""
    
    url = str(url)
    if not url.startswith(settings.MEDIA_URL):
        return url
        
    relative_path = unquote(url[len(settings.MEDIA_URL):])
    full_path = os.path.join(settings.MEDIA_ROOT, relative_path).replace('/', os.sep).replace('\\', os.sep)
    
    if os.path.exists(full_path):
        return url
        
    # Try webp fallback
    name, _ = os.path.splitext(full_path)
    if os.path.exists(name + '.webp'):
        return f"{settings.MEDIA_URL}{os.path.splitext(relative_path)[0]}.webp"
        
    return url

@register.filter
def resolve_urls(url_list):
    """Applies resolve_url to a list of URLs"""
    if not url_list:
        return []
    return [resolve_url(url) for url in url_list]
