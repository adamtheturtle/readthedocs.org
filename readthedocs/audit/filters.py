"""Filters used in our views."""

from django.utils.translation import ugettext_lazy as _
from django_filters import CharFilter, ChoiceFilter, FilterSet

from readthedocs.audit.models import AuditLog


class UserSecurityLogFilter(FilterSet):

    ip = CharFilter(field_name='ip', lookup_expr='exact')
    project = CharFilter(field_name='log_project_slug', lookup_expr='exact')
    action = ChoiceFilter(
        field_name='action',
        lookup_expr='exact',
        choices=[
            (AuditLog.AUTHN, _('Authentication success')),
            (AuditLog.AUTHN_FAILURE, _('Authentication failure')),
        ],
    )

    class Meta:
        model = AuditLog
        fields = ['ip', 'project', 'action']
