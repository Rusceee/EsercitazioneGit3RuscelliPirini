from dataclasses import dataclass


@dataclass
class Studente:
    nome: str
    cognome: str
    eta: int
    citta_residenza: str

    @property
    def classificazione(self) -> str:
        if self.eta < 14:
            return "Non classificato"
        if self.eta <= 15:
            return "Biennio"
        return "Triennio"

    def __str__(self) -> str:
        return (
            f"{self.nome} {self.cognome}, {self.eta} anni, "
            f"residente a {self.citta_residenza} ({self.classificazione})"
        )