from django.shortcuts import render
from os import system
import subprocess

def Home(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
    except:
        ubicacion = ""
    return render(request, "Home.html", {'ubicación': ubicacion})

def CambiarNombre(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae=request.POST["nombrev"]
        namaen=request.POST["nombren"]
        system(f"mv {namae} {namaen}")
        salida="El nombre ha sido actualizado"
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae=""
        namaen=""
        salida=""
    return render(request,"CambiarNombre.html", {"salida":salida,'ubicación': ubicacion})
def CambiarPermisos(request):
    try:
        namae=request.POST["namaewa2"]
        numero=str(request.POST["ichigo"])
        system(f"chmod -R {numero} {namae}")
        salida=subprocess.getoutput(f"ls -l {namae}")
    except:
        namae=""
        salida=""
    return render(request,"CambiarPermisos.html", {'salida':salida})
def CambiarPropietario(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae = request.POST["namaewa3"]
        namae2 = request.POST["ichigo2"]
        system(f"chown -R {namae2} {namae}")
        salida = subprocess.getoutput(f"ls -l {namae}")
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae = ""
        salida = ""
    return render(request,"CambiarPropietario.html", {"salida":salida,'ubicación': ubicacion})
def Copiar(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae=request.POST["nameaa"]
        destino=request.POST["destino"]
        system(f"cp -r {namae} {destino}")
        salida="El archivo fue copiado y pegado correctamente"
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae=""
        destino=""
        salida=""
    return render(request,"Copiar.html", {"salida":salida,'ubicación': ubicacion})
def CrearArchivo(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae=request.GET["aname"]
        system(f"touch {namae}")
        salida="El archivo fue creado con éxito"
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae=""
        salida=""
    return render(request,"CrearArchivo.html", {"salida":salida,'ubicación': ubicacion})
def CrearCarpeta(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae=request.GET["cname"]
        system(f"mkdir {namae}")
        salida="La carpeta  fue creada con éxito"
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae=""
        salida=""
    return render(request,"CrearCarpeta.html", {"salida":salida,'ubicación': ubicacion})
def Eliminar(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae = request.GET["dname"]
        system(f"rm -rf {namae}")
        salida = "La carpeta o archivo fue eliminado con éxito"
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae = ""
        salida = ""
    return render(request,"Eliminar.html", {"salida":salida,'ubicación': ubicacion})
def Mover(request):
    try:
        ubicacion = subprocess.getoutput("pwd")
        namae=request.POST["partida"]
        destino=request.POST["final"]
        system(f"mv {namae} {destino}")
        salida="El archivo fue cortado y movido correctamente"
    except:
        ubicacion = subprocess.getoutput("pwd")
        namae=""
        destino=""
        salida=""
    return render(request,"Mover.html", {"salida":salida,'ubicación': ubicacion})

def VerPermisos(request):
    ubicacion = subprocess.getoutput("pwd")
    try:
	    namae=request.GET["namaewa"]
	    out=subprocess.getoutput(f"ls -l {namae}")
	    salida= f"Los permisos de {namae} son:"
    except:
	    out=""
	    salida=""
    return render(request,"VerPermisos.html", {"salida":salida, "out":out,'ubicación': ubicacion})


def Buscar(request):
    try:
     namaeb=request.GET["bbus"]
     out1=subprocess.getoutput(f"find . -maxdepth 1 -type f | grep {namaeb} -i")
     out2=subprocess.getoutput(f"find . -maxdepth 1 -type d | grep {namaeb} -i")
     tx1="Las carpetas son:"
     tx2="Los archivos son:"
    except:
     namaeb=""
     out1=""
     out2=""
     tx1 = ""
     tx2 = ""
    return render(request,"Buscar.html", {"out1":out1,"out2":out2,"tx1":tx1,"tx2":tx2})