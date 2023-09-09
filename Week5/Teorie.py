"""
TEST CASE

Un test case este o multime de pasi pe care un tester ii parcurge pentru a vedea daca o anumita functionalitate
dintr-o aplicatie este implementata corect sau nu.

Continuul unui test case:
    - Descrierea testului
    - Preconditii (daca e cazul)
    - Pasii de urmat + rezultatele asteptate la fiecare pas.
    - Test Data - Datele cu care opereaza testul (daca este cazul)
    - Rezultatul final asteptat
    - Note si informatii utile (daca este cazul)

Dupa parcugerea pasilor de urmat, rezultatul final actual este apoi comparat cu rezultatul final asteptat.
In cazul in care cele doua sunt identice, restul a trecut, altfel testul a esuat.

Exemplu de testcase:

    Descriere: Login cu user si pass corecte

    Preconditie: Contul sa fie creat

    Pasi: - deschidem browserul la pagina <www.ceva.com>
          - introducem username-ul in input-ul corespunzator
          - introducem password-ul in input-ul corespunzator
          - Test Data: username: user123, password: admin1234
          - facem click pe butonul de login

    Rezultatul final asteptat: se afiseaza pagina corespunzatoare unui login reusit.

    Rezultatul final actual: identic cu cel rezultatul final asteptat
"""