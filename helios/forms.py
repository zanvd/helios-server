"""
Forms for Helios
"""

from django import forms
from .models import Election
from .widgets import *
from .fields import *
from django.conf import settings
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class ElectionForm(forms.Form):
    short_name = forms.SlugField(
        label=_('Short name'),
        max_length=40,
        help_text=_('No spaces allowed. It will be part of the URL for your election, e.g. my-club-2010.')
    )
    name = forms.CharField(
        label=_('Name'),
        max_length=100,
        widget=forms.TextInput(
            attrs={'size': 60}
        ),
        help_text=_('The pretty name for your election, e.g. My Club 2010 Election.')
    )
    description = forms.CharField(
        label=_('Description'),
        max_length=4000,
        widget=forms.Textarea(
            attrs={'cols': 70, 'wrap': 'soft'}
        ),
        required=False
    )
    election_type = forms.ChoiceField(
        label=_('Type'),
        choices=Election.ELECTION_TYPES
    )
    use_voter_aliases = forms.BooleanField(
        label=_('Use voter aliases'),
        required=False,
        initial=False,
        help_text=_('If selected, voter identities will be replaced with aliases,'
                    ' e.g. "V12", in the ballot tracking center.')
    )
    # use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
    randomize_answer_order = forms.BooleanField(
        label=_('Randomize answer order'),
        required=False,
        initial=False,
        help_text=_('Enable this if you want the answers to questions to appear in random order for each voter.')
    )
    private_p = forms.BooleanField(
        label=_('Private?'),
        required=False,
        initial=False,
        help_text=_('A private election is only visible to registered voters.')
    )
    help_email = forms.CharField(
        label=_('Help email address'),
        required=False,
        initial='',
        help_text=_('An email address voters should contact if they need help.')
    )

    if settings.ALLOW_ELECTION_INFO_URL:
        election_info_url = forms.CharField(
            label=_('Election info download URL'),
            required=False,
            initial='',
            help_text=_('The URL of a PDF document that contains extra election information,'
                        ' e.g. candidate bios and statements.')
        )

    # times
    voting_starts_at = SplitDateTimeField(
        label=_('Voting starts at'),
        help_text=_('UTC date and time when voting begins.'),
        widget=SplitSelectDateTimeWidget,
        required=False
    )
    voting_ends_at = SplitDateTimeField(
        label=_('Voting ends at'),
        help_text=_('UTC date and time when voting ends.'),
        widget=SplitSelectDateTimeWidget,
        required=False
    )


class ElectionTimeExtensionForm(forms.Form):
    voting_extended_until = SplitDateTimeField(
        label=_('Voting extended until'),
        help_text=_('UTC date and time voting extended to.'),
        widget=SplitSelectDateTimeWidget,
        required=False
    )


class EmailVotersForm(forms.Form):
    subject = forms.CharField(
        max_length=80
    )
    body = forms.CharField(
        max_length=4000,
        widget=forms.Textarea
    )
    send_to = forms.ChoiceField(
        label=_('Send To'),
        initial='all',
        choices=[
            ('all', _('All voters')),
            ('voted', _('Voters who have cast a ballot')),
            ('not-voted', _('Voters who have not yet cast a ballot'))
        ]
    )


class TallyNotificationEmailForm(forms.Form):
    subject = forms.CharField(
        label=pgettext_lazy('Email subject label', 'Subject'),
        max_length=80
    )
    body = forms.CharField(
        label=pgettext_lazy('Email body label', 'Body'),
        max_length=2000,
        widget=forms.Textarea,
        required=False
    )
    send_to = forms.ChoiceField(
        label=_('Send to'),
        choices=[
            ('all', _('All voters')),
            ('voted', _('Only voters who cast a ballot')),
            ('none', _('No one -- are you sure about this?'))
        ]
    )


class VoterPasswordForm(forms.Form):
    voter_id = forms.CharField(
        label=_('Voter ID'),
        max_length=50
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
        max_length=100
    )
