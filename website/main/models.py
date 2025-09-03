from django.db import models as m
from django.contrib.auth import get_user_model


User = get_user_model()


class Ticket(m.Model):
    """
    Ticket model for main app
    
    Fields:
        title (str): Ticket title
        slug (str): Ticket slug by title
        text (str): Ticket text
        type (str --> choice): Ticket type
        owner (str): Ticket owner
        answer (str): Ticket answer
        created (datetime): Ticket created time
        answered (datetime): Ticket answered time
        is_answer (bool): Is Ticket answered
    """

    TYPE_CHOICES = {
        "objection": "Objection",
        "suggestion": "Suggestion",
        "appreciation": "Appreciation",
        "user_report": "User Report",
        "bug_report": "Bug Report",
    }

    title = m.CharField(max_length = 64)
    slug = m.CharField(max_length = 128)
    text = m.TextField(max_length = 1024)
    type = m.CharField(max_length = 64, choices = TYPE_CHOICES)
    owner = m.ForeignKey(User, related_name = "ticket", on_delete = m.CASCADE)
    answer = m.TextField(max_length = 1024)
    created = m.DateTimeField(auto_now_add = True)
    answered = m.DateTimeField(auto_now = True)
    is_answer = m.BooleanField(default = False)


    def save(self, *args, **kwargs):
        if self.answered:
            self.is_answer = True

        super(Ticket, self).save(*args, **kwargs)
        