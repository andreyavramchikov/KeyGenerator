from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Key(models.Model):

    NOT_ISSUED = u'NOT_ISSUED'
    ISSUED = u'ISSUED'
    REPAID = U'REPAID'
    STATUS_CHOICES = (
        (NOT_ISSUED, u'NOT_ISSUED'),
        (ISSUED, u'ISSUED'),
        (REPAID, u'REPAID')
    )

    value = models.CharField(max_length=4, unique=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=NOT_ISSUED)

    def __unicode__(self):
        return '{}'.format(self.value)


class UserKey(models.Model):
    key = models.ForeignKey(Key)
    session = models.CharField(max_length=255)

    def __unicode__(self):
        return '{}'.format(self.key.value)




