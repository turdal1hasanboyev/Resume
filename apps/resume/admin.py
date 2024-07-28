from django.contrib import admin

from apps.resume.models import Education, AwardCertification, Skill, Experience, Interest


admin.site.register(Education)
admin.site.register(AwardCertification)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Interest)
