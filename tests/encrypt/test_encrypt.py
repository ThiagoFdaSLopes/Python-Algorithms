from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Teste com tipos incorretos para key e message
    with pytest.raises(TypeError):
        encrypt_message("thiago", "thiago") == "tipo inválido para key"
        encrypt_message(1223, "img") == "tipo inválido para message"

    # Teste com key ímpar
    assert encrypt_message("thiago", 3) == "iht_oga"

    # Teste com key par
    assert encrypt_message("abcdefghi", 4) == "ihgfe_dcba"

    # Teste Com Key maior que mensagem
    assert encrypt_message("abcdefghi", 90) == "ihgfedcba"
