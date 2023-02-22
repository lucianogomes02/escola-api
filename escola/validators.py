from rest_framework import serializers


def nome_valido(nome: str) -> bool:
    return all([palavra.isalpha() for palavra in nome.split(" ")])


def rg_valido(rg: str) -> bool:
    return len(rg) == 9 and rg.isdigit()


def cpf_valido(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit()
