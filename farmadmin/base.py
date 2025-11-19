# farmadmin/base.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    """
    Abstract base model for shared metadata.
    last_update -> auto-updated timestamp.
    last_update_by -> user who last modified the record (nullable).
    """
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="%(class)s_updated"
    )

    class Meta:
        abstract = True
