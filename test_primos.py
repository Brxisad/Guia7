import pytest
from primos import es_primo

def test_es_primo_numero_pequeno():
    assert es_primo(2) is True
    assert es_primo(4) is False

def test_es_primo_numero_grande():
    assert es_primo(17) is True
    assert es_primo(20) is False
