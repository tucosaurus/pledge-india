from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import User
# Create your models here.
class Pledge(models.Model):
    """Pledge Model"""

    title = models.CharField(_('title'), max_length = 100)
    description = models.TextField(_('description'),null=True)

    class Meta:
        verbose_name = _('pledge')
        verbose_name_plural = _('pledges')

    def __str__(self):
        return self.title

class User_Pledges(models.Model):
    """User Pledges Model"""

    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_taken = models.DateTimeField(_('taken on'), auto_now_add=True)

    def __str__(self):
        return "%s by %s" % (self.pledge.title, self.user.first_name)
