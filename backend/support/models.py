from django.conf import settings
from django.db import models



class TicketComment(models.Model):
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE, related_name="ticket_comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ticket_comments")

    def __str__(self):
        return self.text


class Ticket(models.Model):
    TICKET_STATUS = (
        ('o', 'Open'),
        ('c', 'Closed'))
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='tickets')
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True, blank=True, 
        related_name='assigned_tickets')
    status = models.CharField(
        null=True, blank=True,
        max_length=1, 
        choices=TICKET_STATUS, 
        default=TICKET_STATUS[0][0])
    comments = models.ManyToManyField(TicketComment, blank=True, related_name="comments")

    def __str__(self):
        return self.title
  