from studente import Studente


class Scuola:
    def __init__(self) -> None:
        self._studenti: list[Studente] = []

    def aggiungi_studente(self, studente: Studente) -> None:
        self._studenti.append(studente)

    def cerca_per_cognome(self, cognome: str) -> list[Studente]:
        cognome_cercato = cognome.casefold()
        return [
            studente
            for studente in self._studenti
            if studente.cognome.casefold() == cognome_cercato
        ]

    def cerca_per_eta(self, eta: int) -> list[Studente]:
        return [studente for studente in self._studenti if studente.eta == eta]

    def conta_studenti(self) -> int:
        return len(self._studenti)