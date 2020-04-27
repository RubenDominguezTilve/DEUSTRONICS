from .models import Empleado, Cliente
from .consts import OPERARIO,RESPONABLE,CLIENTE,SUPERUSER
def getLoggedEmpleado(req):
    return Empleado.objects.filter(usuario=req.user.id)[0]

def getLoggedCliente(req):
    return Cliente.objects.filter(usuario=req.user.id)[0]

def getTipoUsuario(req):
    tipo=OPERARIO
    if req.user.groups.filter(name=CLIENTE).exists():
        tipo=CLIENTE

    if req.user.groups.filter(name=OPERARIO).exists():
        tipo=OPERARIO

    if req.user.groups.filter(name=RESPONABLE).exists():
        tipo=RESPONABLE
    if req.user.groups.filter(name=SUPERUSER).exists():
        tipo=SUPERUSER
    return tipo