from django.shortcuts import render

from .models import Education, AwardCertification, Skill, Experience, Interest, Account


def index(request):
    education = Education.objects.all()
    award_certification = AwardCertification.objects.all()
    skill = Skill.objects.all()
    experience = Experience.objects.all()
    interest = Interest.objects.all()
    
    user = Account.objects.get(id=1)

    context = {
        "education": education.order_by('-id'),
        "award_certification": award_certification.order_by('-id'),
        "skill": skill.order_by('-id'),
        "experience": experience.order_by('-id'),
        "interest": interest.order_by('-id'),
        "user": user
    }

    return render(request, 'index.html', context)
