from django.contrib.admin.apps import AdminConfig


class ChecksheetAdminConfig(AdminConfig):
    default_site = 'checksheet_admin.admin.ChecksheetAdmin'
