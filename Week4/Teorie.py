"""
Principiile Testarii:

1. Testarea arata prezenta defectelor, nu absenta lor
    - Faptul ca nu exista bug-uri, nu inseamna ca ele nu exista deloc

2. Testarea timpurie (Eearly testing)
    - Cu cat testarea incepe mai repede, cu atat posibilitatea de aparitie a bug-urilor este mai mica.

3. Testarea exhaustiva nu este posibila
    - Adica nu este posibil sa testam toata functionalitatea si toate combinatiile valide si nevalide de testare.

4. Testarea este dependenta de context
    - Riscul asociat fiecarui tip de aplicatie este diferit, prin urmare nu este suficient sa utilizezi aceeasi metoda,
    tehnica, tip de testare pentru a testa toate tipurile de aplicatii.

5. Gruparea Defectelor (Clustering)
    - In timpul tetarii, se poate intampla ca majoritatea bug-urilor  sa fie legate de un numar mic de module dezvoltate
    de catre developeri

6. Paradoxul pesticidelor (Pesticide Paradox)
    - Principiul paradoxului pesticidelor spune ca, daca acelasi set de cazuri de testare sunt executate din nou si
    din nou pe parcursul perioadei de test, autnci aceste seturi de teste nu sunt suficient de capabile sa identifice noi
    defecte.

    Se refera mai ales la cazurile cand re-testam un bug.

7. Absenta erorii este o aberatie
    - Daca software-ul este testat complet si daca nu se gasesc defecte inainte de lansare, atunci putem spune ca
    softwareul este 99% fara defecte.

Testarea de API vine in intampinarea principiului 2 al testarii - introducerea testarii cat mia devreme salveaza timp.

Cand ar putea sa fie utila testarea API ?
    - Pentru a detecta defectele din testare cat mai devreme
    - Ofera posibilitatea automatizarii (investesti mai mult la inceput sa dezvolti tetele automate, higher time cost,
    dar nu mai consumi ulterior resurse in rularea testelor, prin reducerea unei persoane care practic ruleaza testele
    manual)
    - Asigura adaptabilitatea testarii in functie de platforma. De exemplu cu acelasi API poti testa o aplicatie care
    ruleaza atat pe Windows cat si pe Linux, Android, IOS
    - Este time efficient, eficienta timpului investit pentru ca API-urile pot sa fie folosite in testare fara sa fie
    o interfata grafica (GUI) dezvoltat complet

Termeni utilizati in testarea API:
    - Interoperabilitate este procesul care faciliteaza ca mai multe aplicatii sa comunice intre ele desi sunt instalate
    pe diferite platforme (Windows,Linux, Android, IOS)
    - Autenficare si autorizare. Exemplu: Daca am o pagina personala de facebook, atunci poate sa fie considerat faptul ca
    sunt si autorizat sa vad pozele personale.
    - Endpoint. Este un termen foarte folosit si utilizat in orice request pe care il facem. Este URL-ul complet pe care
    il apelam cand utilizam orice request.
    - Idempotent/Indempotency este interactiunea client-server in care clientul indiferent de cate ori apeleaza
    endpoint-ul serverul ii intoarce mereu acelasi raspuns.

 Mecanisme de OAuth:
    Este un standard de autorizare de tip open-standard si permite unui serviciu sa foloseasca alt serviciu fara sa mai
    ceara detalii de autentificare (user si parola) ci doar pe baza unui token care este generat in momentul login-ului
    apoi acel token este folosit pe tot parcursul interactiunii celor doua servicii

    De ce este mai secure un token ?
        - Nu trimiti un plain text user si parola -> mai putine contexte in care cineva neautorizat poate accesa serviciul
        - Token are de regula un timp de expirare dupa care este necesara reautentificarea
        - Dirverse tipuri de autorizare nu pot sa fie identificate prin token, administrator, moderator, user, etc.
        - Token-ul este criptat cu un Key

    Diferenta intre criptare si hashing:

    A cripta inseamna a transformare un mesaj oarecare intr-un sir de caractere ce poate sa fie trimite in siguranta
    mai departe. Pentru criptare se foloseste un key unic, daca ai keya unica pentru a cripta mesajul, il poti si decripta
    cu aceeasi key. Rezulta ca este un proces reversibil

    A hashui inseamna a transformare un mesaj oarecare intr-un sir de caractere, actiunea este ireversibila.
    Exemplu, parola este salvata hasuit pe server iar cand cineva se autentifica atunci sistemul de autentificare
    compara cele doua hash-uri

Pentru a definii body-ul corpul requestului de API avem doua tipuri de date. XML si JSON

Mic de studiu de caz:
                JSON                                                         XML
                JSON este un tip de data                                     XML date un tip de data
                JSON accepta: string, numere, boolean                        XML accepta doar stringuri
                structura arborescente                                       structura arborescenta
                parcurgerea este mai lenta                                   parcurgerea este mai rapida


Coduri de raspuns HTTP ( Status Codes HTTP )
    - Status Codes sunt generate de catre Server ca raspuns al unui request dinspre client
    - Compus din 3 cifre
    - Impartite in 5 clase, prima cifra determina clasa din care fac parte:
        1xx Informational - Rquestul a fost primit, continua procesarea
        2xx Success - Requestul a fost receptionat cu success, inteles si acceptat ca format
        3xx Redirect - Actiuni ulterioare trebuie procesate pentru a finaliza requestul cerut initial
        4xx Eroare de client - Requestul contine o sintaxa gresita sau nu poate sa fie procesata
        5xx Eroare de server - Serverul a esuat in procesa requestul primit

    - ultimele doua cifre definesc semnificatia raspunsului. Cate un exemplu din fiecare categoria:
        102 - Processing, Exemplu: Atunci cand trimit un alt request inainte si asteptam un raspuns, faptul ca intoarce
              102 inseamna ca inca asteapta sa procese requestul initial. Practic, acest tip de mesaj informeaza
              clientul ca request-ul lui NU a fost esuat, ci in continuare este procesat dar dureaza mai mult timp.
        200 - OK - Raspunsul standard ca requestul a fost procesat. De regula intors dupa un request de tip GET
        201 - Created - Request a fost procesat cu success, de regula intors dupa un POST
        301 - Movdem Permanently - Atat acest request cat si cele viitoare sunt redirectionate catre alt endpoint.
        401 - Unauthorized - Nu esti autorizat sa accesezi acel tip de endpoint.
        404 - Not Found - Nu gaseste resursa specificata
        503 - Service Unavailable - Serviciul nu este disponibil, poate aparea in urma unui crash al aplicatiei.


Modele principale de HTTP:

    GET - Aceasta metoda este folosita pentru a prelua informatiile care sunt transmise de catre server folosind PUT sau POST.
    Nu are un body, un corp, (JSON), Executia cu success a codului intoarce codul 200
    POST - Aceasta metoda este folosita pentru a crea o inregistrare folosint un body (JSON). Execute cu success intoarce
    codul 201
    PUT - Aceasta metoda este folosita pentru update-ul unei inregistrari care este deja prezenta. Executia cu success
    intoarce codul 200 sau 201.
    PATCH - Aceasta metoda este folosita pentru a solicita modificarea doar anumitor parti din inregistrare, ca o
    peticire. Executia cu success intoarce codul 200 sau 2-1.
    DELETE - Aceasta metoda este folosita pentru a sterge inregistrarea. Executia cu success intaorce 200.

POSTMAN un HUI pentru trimiterea requesturilor si primirea raspunsurilor HTTP

"""