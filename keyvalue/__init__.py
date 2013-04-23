from django.db import connection

from utils import reload

if "keyvalue_store" in connection.introspection.table_names():
    reload()