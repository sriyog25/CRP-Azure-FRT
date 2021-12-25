from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('student/student_register/', include('portal.urls')),
    path('student/student_login/',include('portal.urls')),
    path('student/student_login/usd/',include('portal.urls')),
    path('logout/',include('portal.urls')),
    path('student/student_login/dispstu/', include('portal.urls')),
    path('company/company_register/', include('portal.urls')),
    path('company/company_login/', include('portal.urls')),
    path('company/company_login/ccd/',include('portal.urls')),
    path('company/company_login/jp/', include('portal.urls')),
    path('company/company_login/jd/', include('portal.urls')),
    path('company/company_login/viewpos/', include('portal.urls')),
    path('student/student_login/applyjob/',include('portal.urls')),
    path('student/student_login/applyjob/<str:opt>/',include('portal.urls')),
    path('company/company_login/selectstu/', include('portal.urls')),
    path('company/company_login/selectstu/<str:opt>/',include('portal.urls')),
]
