from Cuenta import Cuenta
import json
from Fecha import Fecha

class DBCuentas:
  def __init__(self, json_file):
    self.db = json.load(json_file)

  def get_cuenta(self, username, password):
    
    for user in self.db['users']:
      # print(user['username'])
      if str(user['username']) == str(username):
        # print(user['password'])
        # print(type(str(user['password'])))
        if str(user['password']) == str(password):
          # print('Entroooo')
          fecha_ultima = user['fecha_ultima_transaccion']
          return Cuenta(
            user['username'],
            user['saldo'],
            Fecha(fecha_ultima['day'],fecha_ultima['month'],fecha_ultima['year']),
            user['monto_retirado_ultimo_dia'],
            user['monto_depositado_ultimo_dia']
          )
    return None