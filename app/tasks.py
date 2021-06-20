from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x, y):
    x = str(x)
    y = str(y)
    return x + y