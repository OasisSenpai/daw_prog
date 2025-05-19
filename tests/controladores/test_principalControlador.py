import unittest
from controladores.principalControlador import ControladorPrincipal

class TestControladorPrincipal(unittest.TestCase):
    def setUp(self):
        self.ctrl = ControladorPrincipal()

    def test_atributos_iniciales(self):
        # Compruebo que existan los atributos básicos
        self.assertTrue(hasattr(self.ctrl, 'conexion'))
        self.assertTrue(hasattr(self.ctrl, 'ui'))
        self.assertTrue(hasattr(self.ctrl, 'vistaTabla'))

    def test_mostrar_especialidades_asigna_tablaActual(self):
        # Preparamos datos de prueba
        datos = [('1', 'Especialidad X')]
        # Sobreescribimos métodos estáticos
        from controladores.lib.especialidades import Especialidades
        Especialidades.leer_datos_tabla = staticmethod(lambda c: datos)
        Especialidades.mostrar_datos   = staticmethod(lambda d, ui, tabla: 'especialidades')
        # Ejecutamos
        self.ctrl.conexion = object()
        self.ctrl.mostrar_especialidades()
        # assertEqual
        self.assertEqual(self.ctrl.tablaActual, 'especialidades')

if __name__ == '__main__':
    unittest.main()
