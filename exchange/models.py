from django.db import models

STATUS = (
    ('NEW', 'NEW'),
    ('PROCESSING', 'PROCESSING'),
    ('FINISHED', 'FINISHED'),
    ('UNFINISHED', 'UNFINISHED'),
)


class ToDo(models.Model):
    title = models.CharField(max_length = 200)
    notes = models.TextField(null = True, blank = True)
    deadline = models.DateField(null = True, blank = True)
    status = models.CharField(choices = STATUS, max_length = 200, default = 'NEW')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

