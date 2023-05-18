import unittest
from DataBaseJSONCuentas import DBCuentas
import io

class TestDBJSON(unittest.TestCase):

  def setUp(self):
    self.db_cuentas = DBCuentas(io.StringIO('''
{
    "users": [
      {
        "username": "Frank",
        "password": 12345,
        "saldo": 5000,
        "fecha_ultima_transaccion": {
          "day": 17,
          "month": 5,
          "year": 2023
        },
        "monto_retirado_ultimo_dia": 300,
        "monto_depositado_ultimo_dia": 400
      }
    ]
  }
    '''))
  def test_get_user(self):
    cuenta = self.db_cuentas.get_cuenta('Frank', '12345')
    
    self.assertNotEqual(cuenta, None)
    self.assertEqual(cuenta.usuario, 'Frank')
    self.assertEqual(cuenta.saldo, 5000)
    self.assertEqual(cuenta.fecha_ultima_transaccion.day, 17)
    self.assertEqual(cuenta.fecha_ultima_transaccion.month, 5)
    self.assertEqual(cuenta.fecha_ultima_transaccion.year, 2023)
    self.assertEqual(cuenta.monto_retirado_ultimo_dia, 300)
    self.assertEqual(cuenta.monto_depositado_ultimo_dia, 400)
    
    
  def test_get_non_existent_user(self):
    cuenta = self.db_cuentas.get_cuenta('NNNNN', '00000')
    self.assertEqual(cuenta, None)
    
    cuenta = self.db_cuentas.get_cuenta('Frank', '00000')
    self.assertEqual(cuenta, None)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestDBJSON)
  unittest.TextTestRunner(verbosity=2).run(suite)