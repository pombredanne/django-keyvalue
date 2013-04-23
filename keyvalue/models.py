from django.db import models

KeyField = models.CharField
ObjectField = models.CharField

class Store(models.Model):
    key = KeyField(max_length=255, unique=True)
    value = ObjectField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"%s:%s" % (self.key, self.value)