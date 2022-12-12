from skimage import io
import matplotlib.pyplot as plt
import datetime

class Fotografia:
    __slots__ = ['_foto','_fotografo','_data','_proprietario']

    _q_fotos = 0

    def __init__(self,foto,fotografo,data,proprietario):
        self._foto = io.imread(foto)
        self._fotografo = fotografo
        self._data = data
        self._proprietario = proprietario
        Fotografia._q_fotos += 1

    def mostrar_fotografia(self):
        plt.imshow(self._foto)
        plt.show()
        
    def propriedades(self):
        print(f'Tamanho da foto:{self._foto.shape}\n\
Fotógrafo:{self._fotografo}\nData:{self._data}')

    @staticmethod
    def get_quantidade_fotos():
        return _q_fotos
    
    @property
    def get_foto(self):
        return self._foto

    @get_foto.setter
    def set_foto(self,f):
        self._foto = f

    @property
    def get_fotografo(self):
        return self._fotografo

    @get_fotografo.setter
    def set_fotografo(self,f):
        self._fotografo = f
        
    @property
    def get_data(self):
        return self._data

    @get_data.setter
    def set_data(self,d):
        self._data = d

    @property
    def get_proprietario(self):
        return self._proprietario

    @get_proprietario.setter
    def set_proprietario(self,p):
        self._proprietario = p

class Pessoa:
    __slots__ = ['_nome','_sobre','_cpf']
    def __init__(self,nome,sobre,cpf):
        self._nome = nome
        self._sobre = sobre
        self._cpf = cpf

    @property
    def get_nome(self):
        return self._nome

    @get_nome.setter
    def set_nome(self,n):
        self._nome = n

    @property
    def get_sobrenome(self):
        return self._sobre

    @get_sobrenome.setter
    def set_sobrenome(self,s):
        self._sobre = s

    @property
    def get_cpf(self):
        return self._cpf

    @get_cpf.setter
    def set_cpf(self,c):
        self._cpf = c
    
    def __str__(self):
        return f'{self._nome} {self._sobre}'

f1 = 'f.png'

fotog = Pessoa('Lazaro','Oliveira',12345678910)
propri = Pessoa('Kennedy','Camilo',21345678910)

foto = Fotografia(f1,fotog,datetime.datetime.now(),propri)

foto.mostrar_fotografia()

foto.propriedades()
