"""crime_hotspots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from crime_hotspots import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', remoteuser.login, name="login"),
    url(r'^Register1/$', remoteuser.Register1, name="Register1"),
    url(r'^Search_Crime_DataSets/$', remoteuser.Search_Crime_DataSets, name="Search_Crime_DataSets"),
    url(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    url(r'^Add_DataSet_Details/$', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),
    url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    url(r'^Search_Crime/$', serviceprovider.Search_Crime, name="Search_Crime"),
    url(r'^View_Crime_By_Area/$', serviceprovider.View_Crime_By_Area, name="View_Crime_By_Area"),
    url(r'^View_Crime_By_Date/$', serviceprovider.View_Crime_By_Date, name="View_Crime_By_Date"),
    url(r'^View_All_Crime_Prediction_Details/$', serviceprovider.View_All_Crime_Prediction_Details, name="View_All_Crime_Prediction_Details"),
    url(r'^View_Crime_Details/$', serviceprovider.View_Crime_Details, name="View_Crime_Details"),
    url(r'^View_Crime_Found_Ratio/$', serviceprovider.View_Crime_Found_Ratio, name="View_Crime_Found_Ratio"),
    url(r'^View_Search_Ratio/$', serviceprovider.View_Search_Ratio, name="View_Search_Ratio"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
