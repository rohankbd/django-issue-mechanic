from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from random import randint
from .models import Issue, Agents, Mechanic
from myapp import models

@csrf_exempt
def create_issue(request):
    if request.method == 'POST':
        # Extract data from the request body
        userID = request.POST.get('userID')
        location = request.POST.get('location')
        problem = request.POST.get('problem')

        # Create a new issue
        issue = Issue.objects.create(
            userID=userID,
            location=location,
            problem=problem,
            status='INQUEUE'
        )

        # Get the agent with the least number of requests in their queue
        agent = Agents.objects.order_by('queue').first()
        
        # Assign the created issue to the agent
        issue.agent = agent
        issue.save()

        # Increment the agent's queue count by 1
        Agents.objects.filter(agentID=agent.agentID).update(queue=models.F('queue') + 1)

        # Check if there are any available mechanics
        available_mechanics = Mechanic.objects.filter(availability=True)
        
        if available_mechanics.exists():
            # Assign a random mechanic from the available mechanics
            mechanic = available_mechanics[randint(0, available_mechanics.count() - 1)]
            issue.status = 'ASSIGNED'
            issue.mechanic = mechanic
            issue.save()
            agent.queue -= 1
            agent.save()
            mechanic.availability = False
            mechanic.save()
            return JsonResponse({'message': 'Issue created successfully.', 'issueID': issue.issueID, 'agentID': agent.agentID, 'mechanicID': mechanic.mechanicID})
        else:
            return JsonResponse({'message': 'Issue created successfully. No available mechanics at the moment.', 'issueID': issue.issueID, 'agentID': agent.agentID})
    else:
        return JsonResponse({'error': 'Invalid request method.'})

@csrf_exempt
def check_mechanic_availability(request):
    if request.method == 'GET':
        mechanic = Mechanic.objects.filter(availability=True).first()
        if mechanic:
            mechanic.availability = False
            mechanic.save()
            return JsonResponse({'mechanicID': mechanic.mechanicID}, status=200)
        else:
            return JsonResponse({'message': 'No available mechanics.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
