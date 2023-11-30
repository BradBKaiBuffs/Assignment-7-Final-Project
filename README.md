# Assignment #7: Final Project
## Description:
This is a website that focuses on the degree checklist for a bachelor's degree. The example checklist is for a Computer Science degree. 
Navigate to the checklist and it will prompt a sign in as a user. An example user has been prepared under user account section. The checklist uses cripsy forms and submitting a completed form will result in a PDF download and a CSV export of the results in the base directory of the degree_checklist file structure.
## Notes:
### User accounts
- Admin account to use for this site: **admin02**
- Password: **Checklist1!**
- Staff account: **Staff02**
- Password: **Checklist1!**

### Packages that are required:
- django-crispy-forms
- crispy-bootstrap4
- django-configurations
- reportlab
- djangorestframework
- matplotlib
- dj_database_url
  
## Baseline implementations:
- **Chapter 1**
- *Basic Views* in checksheet.views.py
- *URL Mapping* in checksheet.urls.py
- *Templates* in checksheet.views.py
- *Routing* in checksheet.views.py
- **Chapter 2**
- *Working with Databases* as shown in checklist.html
- *SQL* 
- *Django Models* in checksheet.models.py
- *Django Migrations* 
- **Chapter 3 and 11**				
- *Class-Based Views*	in record_management.views.py		
- *Function-Based Views* in checksheet.views.py
- *Django Template Language* in home.html
- *Template Filters* seen in home.html		
- **Chapter 4 and 10**				
- *Django Admin*
- **Chapter 5**				
- *Static Files* seen in degree_checksheet.py		
- *Static Urls* seen in degree_checksheet.py			
- **Chapter 6 and 7**				
- *Django Forms Classes* seen in checksheet.forms.py
- *Django ModelForm Class* seen in checksheet.models.py
- *Form data validation and retrieval* see in checksheet.forms.py		
- **Chapter 8**
- *File Upload* seen in upload.html			
- **Chapter 9**
- *Sessions* 
- **Chapter 13**
- *PDF Generation* seen in checklist.html
- *CSV Generation(export)* seen in checklist.html
- *Graphs and Visualizations* seen in graph.html
- **Chapter 14**
- *unittest in Django* in checksheet.tests.py
- *Testing Models* in checksheet.tests.py
- **Chapter 15**
- *python-dotenv or **django-configurations*** seen in degree_checksheet.settings.py
- *django-crispy-forms* seen in Checklist.html 	

## Good implmentations:
- **Chapter 4 and 10**
- *Customize Admin interface* seen at Django Admin webpage
- *Customize ModelAdmin classes* seen in checksheet.adminconfig.py
- **Chapter 5**
- *Use front-end framework (bootstrap)* seen in base.html
- *dj-database-url* in degree_checklist settings.py
- **Chapter 8**
- *Serving Media Files* seen in base.html
- *Passwords and Auth* seen in Django Admin webpage
## Better implementations:
- **Chapter 4 and 10**
- *Add custom view to admin interface* seen in Django Admin webpage
- **Chapter 8**
- *ModelForm and File Uploads* seen in admin/upload.html

## Best implementations:
- **Chapter 12**
- *Django Admin manage users* seen in Django Admin webpage
- *Django REST Framework* seenin checksheet.api_views.py
