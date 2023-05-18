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
class MontoNoEsNumeroPositivo(Exception):
  pass


class NoHayCuentaSeleccionada(Exception):
  pass


class CajeroSinFondosSuficientes(Exception):
  pass


class ExedeElLimiteDeRetiroDiario(Exception):
  pass


class ExedeElLimiteDeDepositoDiario(Exception):
  pass


class NoAlcanzaAlMinimoDeDepositoDiario(Exception):
  pass


class NoAlcanzaAlMinimoDeRetiroDiario(Exception):
  pass


def isNumber(num):
  return isinstance(5, numbers.Number)


def isPositiveNumber(num):
  if isNumber(num):
    return num > 0
  return False


class Cajero:
  intentos_contraseña = 3
  db_json_filename = 'datos.json'
  max_retiro_diario = 3000
  min_retiro_diario = 0
  max_deposito_diario = 3000
  min_retiro_diario = 0
  saldoCaja = 10000

  def __init__(self, cuenta: Cuenta):
    self.cuenta: Cuenta = cuenta

  def get_cuenta(self) -> Cuenta:
    return self.cuenta

  def depositar(self, monto) -> bool:
    if isPositiveNumber(monto):
      return False
      raise MontoNoEsNumeroPositivo()

    self.cuenta.incrementar_saldo(monto)
    return True

  def retirar(self, monto):
    if isPositiveNumber(monto):
      return False
      raise MontoNoEsNumeroPositivo()

    self.cuentaSeleccionada.decrementar_saldo(monto)
    return True


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
