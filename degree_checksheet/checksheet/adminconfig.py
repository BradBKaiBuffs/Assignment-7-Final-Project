from django.contrib.admin.apps import AdminConfig

# default site
class ChecksheetAdminConfig(AdminConfig):
    default_site = 'admin.ChecksheetAdminSite'