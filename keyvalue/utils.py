from django.conf import settings

from models import Store

def reload():
    for key, default in getattr(settings, "KEYVALUE_KEYS", []):
        if not Store.objects.filter(key=key).count():
            Store(key=key, value=default).save()