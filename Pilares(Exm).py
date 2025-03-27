class Empleado():
    def __init__(self, idempleado, nombre):
        self.idempleado = idempleado
        self.nombre = nombre 
    def calculoSalario ():
         pass
class Desarrollador (Empleado):
        def __init__(self, idempleado, nombre, salarioBase, hrsExtra, TarifaExtra):
             super().__init__(idempleado, nombre)
             self.salarioBase = salarioBase
             self.hrsExrtra = hrsExtra
             self.TarifaExtra =  TarifaExtra
        def calculoSalario(self):
             return self.salarioBase + (self.hrsExtra * self TarifaExtra)
            
            