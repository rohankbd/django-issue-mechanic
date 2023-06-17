from django.db import models

class Issue(models.Model):
    INQUEUE = 'INQUEUE'
    ASSIGNED = 'ASSIGNED'
    DISPATCHED = 'DISPATCHED'
    STATUS_CHOICES = [
        (INQUEUE, 'In Queue'),
        (ASSIGNED, 'Assigned'),
        (DISPATCHED, 'Dispatched'),
    ]

    issueID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    location = models.CharField(max_length=255)
    problem = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=INQUEUE
    )

    def __str__(self):
        return f"Issue #{self.issueID}"

class Agents(models.Model):
    agentID = models.AutoField(primary_key=True)
    queue = models.IntegerField(default=0)

    def __str__(self):
        return f"Agent #{self.agentID}"

class Mechanic(models.Model):
    mechanicID = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Mechanic #{self.mechanicID}"

mechanics = Mechanic.objects.all()
for mechanic in mechanics:
    print(f"Mechanic {mechanic.mechanicID} availability: {mechanic.availability}")
