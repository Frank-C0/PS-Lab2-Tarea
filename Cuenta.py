from Fecha import Fecha
import datetime
class Cuenta:

  def __init__(self, usuario, saldo, fecha_ultima_transaccion:Fecha, monto_retirado_ultimo_dia, monto_depositado_ultimo_dia):
    self.usuario = usuario
    self.saldo = saldo
    self.fecha_ultima_transaccion:Fecha = fecha_ultima_transaccion
    self.monto_retirado_ultimo_dia = monto_retirado_ultimo_dia
    self.monto_depositado_ultimo_dia = monto_depositado_ultimo_dia

    datetime.datetime.now()

  
  
  def __str__(self):
    return f"Cuenta : {self.user}\n Saldo : S/.({self.saldo})"

  def incrementar_saldo(self, monto):
    self.saldo = self.saldo + monto

  def decrementar_saldo(self, monto):
    self.saldo = self.saldo + monto
