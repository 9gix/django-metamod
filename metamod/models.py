from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

LOCK_TIMEOUT = getattr(settings, 'LOCK_TIMEOUT', 3600)

class Moderation(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_pk = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    moderated_by = models.ForeignKey(User)
    moderated_at = models.DateTimeField()

    status = models.ForeignKey('ModerationStatus')

    locked_at = models.DateTimeField()

    @property
    def is_locked(self):
        if self.locked_at:
            if (datetime.today() - self.locked_at).seconds < LOCK_TIMEOUT:
                return True
        return False

class ModerationStatus(models.Model):
    # Approved, Rejected, Spam, Pending, Deleted, Incomplete, etc...
    status = models.CharField(max_length=20)

class Action(models.Model):
    # Approve, Reject, Spam, Ignore, Flag, etc...
    name = models.CharField(max_length=20)
    slug = models.SlugField()
