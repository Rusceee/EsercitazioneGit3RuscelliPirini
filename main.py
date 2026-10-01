from scuola import Scuola
from studente import Studente


def mostra_menu() -> None:
    print("\n=== GESTIONALE SCUOLA ===")
    print("1. Aggiungi studente")
    print("2. Cerca studente per cognome")
    print("3. Cerca studente per età")
    print("4. Mostra conteggio totale studenti")
    print("0. Esci")


def main() -> None:
    scuola = Scuola()

    while True:
        mostra_menu()
        scelta = input("\nSeleziona un'opzione (0-4): ").strip()

        if scelta == "1":
            print("\n--- AGGIUNGI STUDENTE ---")
            nome = input("Inserisci il nome: ").strip()
            cognome = input("Inserisci il cognome: ").strip()
            
            while True:
                try:
                    eta = int(input("Inserisci l'età: "))
                    if eta < 0:
                        print("L'età non può essere negativa.")
                        continue
                    break
                except ValueError:
                    print("Inserisci un numero intero valido per l'età.")

            citta = input("Inserisci la città di residenza: ").strip()

            studente = Studente(
                nome=nome,
                cognome=cognome,
                eta=eta,
                citta_residenza=citta
            )
            scuola.aggiungi_studente(studente)
            print(f"\nStudente '{nome} {cognome}' aggiunto con successo!")

        elif scelta == "2":
            print("\n--- CERCA PER COGNOME ---")
            cognome = input("Inserisci il cognome da cercare: ").strip()
            risultati = scuola.cerca_per_cognome(cognome)

            if risultati:
                print(f"\nTrovati {len(risultati)} studenti con cognome '{cognome}':")
                for s in risultati:
                    print(f"- {s}")
            else:
                print(f"\nNessun studente trovato con cognome '{cognome}'.")

        elif scelta == "3":
            print("\n--- CERCA PER ETÀ ---")
            while True:
                try:
                    eta = int(input("Inserisci l'età da cercare: "))
                    break
                except ValueError:
                    print("Inserisci un numero intero valido.")

            risultati = scuola.cerca_per_eta(eta)

            if risultati:
                print(f"\nTrovati {len(risultati)} studenti con età {eta}:")
                for s in risultati:
                    print(f"- {s}")
            else:
                print(f"\nNessun studente trovato con età {eta}.")

        elif scelta == "4":
            totale = scuola.conta_studenti()
            print(f"\nTotale studenti attualmente registrati: {totale}")

        elif scelta == "0":
            print("\nUscita dal programma. Arrivederci!")
            break

        else:
            print("\nOpzione non valida. Riprova.")


if __name__ == "__main__":
    main()