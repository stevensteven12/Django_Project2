from django.db import models


class LogEntry(models.Model):
    """
    Definition of a log entry
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(blank=False, max_length=10)
    message = models.TextField(blank=False)
