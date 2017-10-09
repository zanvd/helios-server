from django.contrib import admin
from .models import Election, ElectionLog, VoterFile, Voter, CastVote, AuditedBallot, Trustee

admin.site.register(Election)
admin.site.register(ElectionLog)
admin.site.register(VoterFile)
admin.site.register(Voter)
admin.site.register(CastVote)
admin.site.register(AuditedBallot)
admin.site.register(Trustee)
