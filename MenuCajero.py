import os
import sys
from Cajero import Cajero


class MenuCajero:
  #asdafasdf
  def __init__(self):
    self.estado = False
    self.cajero: Cajero = Cajero()


#iniciar menu

  def start(self):
    # seleccionar usuario al empesar
    self.printMenu()
    #capturar usuario
    print(self.cajero.hay_cuenta_seleccionada())
    while False:  #metodo que retorne verdadero si existe la cuenta.
      nom = input("Su usuario es: ")
      passw = input("Ingrese su contraseña : ")
      self.cajero.seleccionarCuenta(nom, passw)

    self.cajero.seleccionarCuenta("Frank", '12345')
    print(self.cajero.hay_cuenta_seleccionada())
    self.menu()

  def menu(self):

    # self.clear()
    self.estado = True

    while self.estado:

      self.printMenu()
      opcion = int(input("Su opción es: "))  # verificaciones

      if self.verificarNumero(opcion):

        if opcion == 1:
          monto = input("Ingrese monto : ")
          if self.cajero.depositar(monto):
            print("Deposito exitoso")  # comprobar que se haya depositado
          else:
            print("Deposito fallido")
          #self.depositar()
        elif opcion == 2:
          monto = input("Ingrese monto : ")
          #verificar que la cuenta y cajero contiene el monto
          if self.cajero.retirar(monto):
            print("Retiro exitoso")
          else:
            print("Retiro fallido")
          #self.retiro()
        elif opcion == 3:
          self.cajero.get_cuenta_seleccionada()

        elif opcion == 4:
          self.estado = False

        elif opcion == 0:
          self.estado = False
          #self.clear())
          self.printMenu()
        #print("Programa finalizado")
        else:
          print("No existe esa opcion")
          #opcion = input("Su opción es: ")

  def verificarNumero(self, num):
    #Comprueba que sea positivo.

    if num >= 0:
      return True
    else:
      return False

  def clear():
    # if os.name == "posix":
    #     os.system ("clear")
    # elif os.name == ("ce", "nt", "dos"):
    #     os.system ("cls)
    pass

  def printMenu(self):
    if self.estado:
      print(""" Bienvenido al cajero automatico
            *******Menú********
            
            0- Seleccionar cuenta
            
            1- Depositar
            
            2- Retirar

            3- Ver saldo

            4- Salir """)
    else:
      print(""" Bienvenido al cajero automatico
            *******Menú********
            1- Ingrese usuario:
            
            """)
