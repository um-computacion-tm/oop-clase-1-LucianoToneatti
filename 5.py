import unittest

class Materia:
    def __init__(self, nombre, profesores, alumnos):
        self.__nombre__= nombre
        self.__profesores__= profesores
        self.__alumnos__= alumnos

    def agregar_alumno(self,alumno):
        self.__alumnos__= alumno

    def obtener_alumnos(self):
        return self.__alumnos__

    def obtener_profesores(self):
        return self.__profesores__
    
    def cambiar_nombre(self, nombre):
        self.__nombre__= nombre


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__


materia_comp = Materia("Computacion", profesores=["Claudio", "Elio"], alumnos=["Camila","Ian"])
profesores_de_comp= materia_comp.obtener_profesores()
alumnos_de_comp= materia_comp.obtener_alumnos()
print("Alumnos de comp: ",alumnos_de_comp)
print("Profesores de comp: ", profesores_de_comp)

class Alumno:
    def __init__ (self,nombre,legajo,edad,email):
        self.__nombre__= nombre
        self.__legajo__= legajo
        self.__edad__= edad
        self.__email__= email
        self.__inacistencias__= 0 #No es un parametro porque es un atributo pero como esta empezando tiene cero faltas
        self.__mentor__= None #No es un parametro porque es un atributo pero como esta empezando no tiene mentor
    
    def agregar_mentor(self,mentor):
        self.__mentor__= mentor

    def cambiar_edad(self,edad):
        self.__edad__= edad # El igual es una asignacion de lo que esta en la derecha sobe lo que esta en la izquierda

    def obtener_edad(self):
        return self.__edad__

alumno= Alumno(nombre="Camila", legajo=1234, edad=20, email="camilaChoque@alumno.um.edu.ar") #Creamos un objeto fuera de la clase 
alumno.agregar_mentor("Claudio")
print("Mentor de ", alumno.__nombre__, " es ",alumno.__mentor__)

alumno_2 = Alumno(nombre="Ian",legajo="345", edad=20, email="ian@alumno.um.edu.ar")
alumno_2.cambiar_edad(25)
print(alumno_2.obtener_edad())


###TEST###TEST###TEST###TEST###TEST###

class TestMateria(unittest.TestCase):

    def test__init__Materia(self):
        materia = Materia(nombre="Computacion", profesores=["Claudio", "Elio"], alumnos=["Camila","Ian"])
        self.assertEqual(materia.__nombre__,"Computacion")
        self.assertEqual(materia.__profesores__, ["Claudio", "Elio"])
        self.assertEqual(materia.__alumnos__, ["Camila","Ian"])

    def test_obtener_profesores(self):
        self.assertEqual(materia_comp.obtener_profesores(), ["Claudio", "Elio"])

    def test_cambiar_nombre(self):
        materia = Materia(nombre="Computacion", profesores= None, alumnos=None)
        materia.cambiar_nombre("Matematicas")
        self.assertEqual(materia.__nombre__,"Matematicas")
        
    def test_agregar_alumno(self):
        materia = Materia(nombre=None, profesores= None, alumnos=None)
        materia.agregar_alumno(alumno)
        self.assertEqual(materia.__alumnos__,alumno)

    def test_obtener_alumnos(self):
        self.assertEqual(materia_comp.obtener_alumnos(), ["Camila","Ian"])



class TestProfesor(unittest.TestCase):

    def test__init__Profesor(self):
        profesor = Profesor(nombre="Claudio", cargo="Profesor", legajo=1234)
        self.assertEqual(profesor.__nombre__, "Claudio")
        self.assertEqual(profesor.__cargo__, "Profesor")
        self.assertEqual(profesor.__legajo__, 1234)

    def test_obtener_nombre(self):
        profesor = Profesor(nombre="Claudio" , cargo=None, legajo=None)
        self.assertEqual(profesor.obtener_nombre(), "Claudio")

    def test_obtener_cargo(self):
        profesor = Profesor(nombre=None,cargo="Profesor", legajo=None)
        self.assertEqual(profesor.obtener_cargo(), "Profesor")

    def test_obtener_legajo(self):
        profesor = Profesor(nombre=None,cargo=None,legajo=1234)
        self.assertEqual(profesor.obtener_legajo(), 1234)




unittest.main()