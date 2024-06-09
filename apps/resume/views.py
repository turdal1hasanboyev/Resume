from django.shortcuts import render
from .models import Education, AwardCertification, Skill, Experience, Interest
from ..account.models import Account


def index(request):
    education = Education.objects.all().order_by('-id')
    award_certification = AwardCertification.objects.all().order_by('-id')
    skill = Skill.objects.all().order_by('-id')
    experience = Experience.objects.all().order_by('-id')
    interest = Interest.objects.all().order_by('-id')
    user = Account.objects.get(id=1)

    context = {
        "education": education,
        "award_certification": award_certification,
        "skill": skill,
        "experience": experience,
        "interest": interest,
        "user": user
    }

    return render(request, 'index.html', context)
