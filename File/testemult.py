# Importação da biblioteca pytest
import pytest
# importação das funções da biblioteca criada para verificação de multimos "Verificanum"
from verificanum import multiplos_ambos, multiplos_vazio, multiplos5, multiplos7


class test_multiplos:
    def setup_method(self):
        pass
    
    def test_multiplos5(self):
        resultado1 = multiplos5()
        assert resultado1 == 'fizz'
        
        with pytest.raises(ValueError):
            print("Por favor digite um número natural")

    def test_multiplos7(self):
        resultado2 = multiplos7()
        assert resultado2 == 'buzz'
        
        with pytest.raises(ValueError):
            print("Por favor digite um número natural")
    
    def test_multiplos_ambos(self):
        resultado3 = multiplos_ambos()
        assert resultado3 == 'fizzbuzz'
        
        with pytest.raises(ValueError):
            print("Por favor digite um número natural")
    
    def test_multiplos_vazio(self):
        resultado4 = multiplos_vazio()
        assert resultado4 == 'miss'
        
        with pytest.raises(ValueError):
            print("Por favor digite um número natural")
       
