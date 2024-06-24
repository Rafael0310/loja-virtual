from dataclasses import dataclass

@dataclass
class Cliente:
    cpf: int
    nome: str
    endereco: str
    