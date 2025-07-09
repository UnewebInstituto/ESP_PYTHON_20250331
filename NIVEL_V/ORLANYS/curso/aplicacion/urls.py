"""
URL configuration for aplicacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from aplicacion.views import saludo
from aplicacion.views import otrosaludo
from aplicacion.views import principal
from aplicacion.views import persona_ingresar
from aplicacion.views import persona_ingresar01
from aplicacion.views import persona_reporte
from aplicacion.views import persona_consultar
from aplicacion.views import persona_consultar01
from aplicacion.views import persona_borrar
from aplicacion.views import persona_borrar01
from aplicacion.views import persona_actualizar
from aplicacion.views import persona_actualizar01
from aplicacion.views import persona_actualizar02
from aplicacion.views import ejemplo01_js
from aplicacion.views import ejemplo02_js
from aplicacion.views import ejemplo03_js
from aplicacion.views import ejemplo01_jq
from aplicacion.views import ejemplo02_jq
from aplicacion.views import ejemplo03_jq
from aplicacion.views import persona_api_json
from aplicacion.views import persona_reporte_api_json


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal),
    path('/', principal),
    path('saludar/', saludo),
    path('saludar1/', otrosaludo),
    path('persona_ingresar/', persona_ingresar),
    path('persona_ingresar01/', persona_ingresar01),
    path('persona_reporte/', persona_reporte),
    path('persona_consultar/', persona_consultar),
    path('persona_consultar01/', persona_consultar01),
    path('persona_borrar/', persona_borrar),
    path('persona_borrar01/', persona_borrar01),
    path('persona_actualizar/', persona_actualizar),
    path('persona_actualizar01/', persona_actualizar01),
    path('persona_actualizar02/', persona_actualizar02),
    path('ejemplo01_js/', ejemplo01_js),
    path('ejemplo02_js/', ejemplo02_js),
    path('ejemplo03_js/', ejemplo03_js),
    path('ejemplo01_jq/', ejemplo01_jq),
    path('ejemplo02_jq/', ejemplo02_jq),
    path('ejemplo03_jq/', ejemplo03_jq),
    path('persona_api_json/', persona_api_json),
    path('persona_reporte_api_json/', persona_reporte_api_json),
]


