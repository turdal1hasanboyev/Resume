from django.contrib import admin

from resume.models import Education, AwardCertification, Skill, Experience, Interest, Account


admin.site.register(Education)
admin.site.register(AwardCertification)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Interest)
admin.site.register(Account)
