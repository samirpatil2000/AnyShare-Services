from django.db import models


class UsersGroups(models.Model):

    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    group = models.ForeignKey("account.Group", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " - " + self.group.name