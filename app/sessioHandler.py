from .models import Empleado, Cliente

def getLoggedEmpleado(req):
    return Empleado.objects.filter(usuario=req.user.id)[0]

def getLoggedCliente(req):
    return Cliente.objects.filter(usuario=req.user.id)[0]