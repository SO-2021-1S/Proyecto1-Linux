import os
from pathlib import Path
from typing import Any
from django import template
from subprocess import getoutput

register = template.Library()

@register.simple_tag
def name(request):
  return request.GET.get('Name', '')

@register.simple_tag
def type(request):
  return request.GET.get('Tipo', '')

@register.simple_tag
def permits(request):
  return request.GET.get('Permisos', '')

@register.simple_tag
def showpermits(request, rutashow):
  if request.GET.get('Name', '')=='':
    comando = "ls -l %s" % os.path.join(rutashow, request.GET.get('Nombre', ''))
    out = getoutput(comando, shell=True)
    

  return request.GET.get('Permisos', '')