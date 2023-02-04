from django.contrib import admin
from .models import Activity, Candidate, Vacancy, Education, Post, Employer

# Register your models here.
admin.site.register(Activity)
admin.site.register(Candidate)
admin.site.register(Vacancy)
admin.site.register(Education)
admin.site.register(Post)
admin.site.register(Employer)
