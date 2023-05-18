from Cuenta import Cuenta
from DataBaseJSONCuentas import DBCuentas
import numbers


# class Cajeroo:
#   def hay_cuenta_seleccionada(self):
#     pass
#   def seleccionarCuenta(self, username, password)->Cuenta:
#     pass
#   def get_cuenta_seleccionada(self)->Cuenta:
#     pass
#   def depositar(self, monto)->bool:
#     pass
#   def retirar(self, monto)->bool:
#     pass
class MONTO_NO_NUMERICO(Exception):
  pass
class MONTO_NEGATIVO(Exception):
  pass
class CUENTA_ERRONEA(Exception):
  pass
class CAJERO_SIN_FONDO(Exception):
  pass
class LIMITE_DE_RETIRO_DIARIO_EXCEDIDO(Exception):
  pass
class LIMITE_DE_DEPOSITO_DIARIO_EXCEDIDO(Exception):
  pass
class ERROR_MINIMO_DE_DEPOSITO(Exception):
  pass
class ERROR_MINIMO_DE_RETIRO(Exception):
  pass


def isNumber(num):
  return isinstance(5, numbers.Number)

class Cajero:
  max_retiro_diario = 3000
  min_retiro_diario = 0
  max_deposito_diario = 3000
  min_retiro_diario = 0
  saldoCaja = 10000

  def __init__(self, cuenta: Cuenta):
    if isinstance(cuenta, Cuenta) or cuenta is None:
      raise CUENTA_ERRONEA()
      
    self.cuenta: Cuenta = cuenta

  def get_cuenta(self) -> Cuenta:
    return self.cuenta

  def depositar(self, monto):
    if isNumber(monto):
      raise MONTO_NO_NUMERICO()
      if monto < 0:
        raise MONTO_NEGATIVO()
          if monto < min_retiro_diario:
            raise ERROR_MINIMO_DE_DEPOSITO
    
    self.cuenta.incrementar_saldo(monto)

  def retirar(self, monto):
    if isNumber(monto):
      raise MONTO_NO_NUMERICO()
      if monto < 0:
        raise MONTO_NEGATIVO()
          if monto < min_retiro_diario:
            raise ERROR_MINIMO_DE_DEPOSITO

    self.cuentaSeleccionada.decrementar_saldo(monto)


# class CajeroVerificado(Cajeroo):
#   def __init__(self):
#     self.cajero = Cajero()
#   def hay_cuenta_seleccionada(self):
#     return self.cajero.hay_cuenta_seleccionada()
#   def seleccionarCuenta(self, username, password)->Cuenta:
#     return self.cajero.seleccionarCuenta(username,password)
#   def get_cuenta_seleccionada(self)->Cuenta:
#     return self.cajero.get_cuenta_seleccionada()
#   def depositar(self, monto)->bool:
#     return self.cajero.depositar()
#   def retirar(self, monto)->bool:
#     if(monto)
#     return self.cajero.retirar
