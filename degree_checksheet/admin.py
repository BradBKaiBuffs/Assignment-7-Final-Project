from django.contrib import admin

# customizes the name of the admin site
class ChecksheetAdminSite(admin.AdminSite):
    title_header = "Checklist Admin"
    site_header = "Checklist administration"
    index_title = "Checklist site admin"