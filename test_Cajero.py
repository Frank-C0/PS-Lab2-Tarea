import unittest
from Cajero import Cajero
from Usuarios import Usuario

class TestTypeCheck(unittest.TestCase):
  def setUp(self):
    self.usuario_test = Usuario('UserTest', '12345', 3000)
    self.cajero = Cajero(self.usuario_test)

  def test_deposito_normal(self):
    saldo_inicial = self.cajero.cuenta.saldo
    monto_a_depositar = 100
    
    self.cajero.depositar(monto_a_depositar)
    self.assertEqual(self.cajero.cuenta.saldo, saldo_inicial+monto_a_depositar)
  
  def test_deposito_limitado(self):
    saldo_inicial = self.cajero.cuenta.saldo
    monto_a_depositar = 2000
    
    self.cajero.depositar(monto_a_depositar)
    self.assertEqual(self.cajero.cuenta.saldo, saldo_inicial+monto_a_depositar)
    
    saldo_inicial = self.cajero.cuenta.saldo
    monto_a_depositar = 2000
    
    self.cajero.depositar(monto_a_depositar)
    self.assertEqual(self.cajero.cuenta.saldo, self.cajero.cuenta.saldo)

  def test_deposito_incorrecto(self):
    saldo_inicial = self.cajero.cuenta.saldo
    monto_a_depositar = 2000
    
    self.cajero.depositar(monto_a_depositar)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestTypeCheck)
  unittest.TextTestRunner(verbosity=2).run(suite)