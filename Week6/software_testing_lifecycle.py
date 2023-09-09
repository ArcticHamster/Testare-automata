"""
SDLC = Software Development Lifecycle
STLC = Software Testing Lifecycle

Etape SDLC:
1. Concept
2. Creare cerintelor de business
3. Dezvoltare
4. STLC:
    a) Test Planning
    b) Test monitoring and control
    c) Test analysis
    d) Test design
    e) Test Implementation
    f) Test execution
    g) Test completion
5. Lansare

Etapele STLC:

1. Test planning
O etapa administrativa, pregatitoare a intregului proces de testare, care presupune planificarea activitatilor de
testare si a procesului de testare:
    - alocarea de relouri ( cine o sa faca testarea ? )
    - test plan ( un document care sa descrie felul in care se va desfasura testarea )
    - definim criteriile de intrare ( entry criteria ) si criteriile de iesire ( exit criteria )
    - se evalueaza riscurile DE PROIECT si se mitigheaza daca e cazul
    - se evalueaza criteriile de intrare pentru a verifica daca putem sa mergem la etapa urmtoare a testarii

Criterii de intrare ( entry criteria ) = conditii care trebuie indeplinite pentru a putea incepe procesul de testare
( toate riscurile - sau macar cele majore - au fost mitigate, cerintele de business sunt definite clar, rolurile sunt
alocate, planul de testare este scris si agreat cu toata lumea )

Criterii de iesire ( exit criteria ) = conditii care trebuie indeplinite pentru a putea finaliza procesul de testare
( sa executam toate testele sau un anumit procentaj specific, am ajuns la deadline, am terminat bugetul, nu am
mai gasit bug-uri de o severitate mare sau foarte mare intr-un anumit interval de timp, nu am mai gasit bug-uri deloc
intr-un anumit interval de timp )

2. Test monitoring and control
- este o etapa continua care incepe o data cu etapa de planning si se termina o data cu etapa de inchidere
- rolul acestei etape de a monitoriza in permanenta proiectul pentru a ne asigura ca indeplinim obiectivele, ca livram
produsul la timp si ca nu eista anumite riscuri care ar putea perturba cursul proiectului.
- daca exista situatii neplacute care s-au reprodus sau urmeaza sa se reproduca se iau masuri de control pentru a putea
sa readucem proiectul intr-o zona de siguranta.
- de regula se indeplindeste prin trimiterea unor rapoarte de status periodice ( test status raport ) - generat sa fie
zilnic, saptamanal, fie lunar si trimise team lead-ului si respectiv project managerului sau prin sedinte zilnic
standup in mediile Agile

3. Test analysis
Este o etapa in care:
a) se analizaeza cerintele de business pentru a evaluea daca sunt corecte si complete. Scopul acestei analize
(testarea statica) este de asogira gasirea timpurie a bug-urilor si asigurarea unui proces de testare calitativ
b) se definesc conditiile de testare ( ce testam ) plecand de la cerintele de business definite anterior

4. Test design
- se scriu cazurile de testare ( cum testam ) plecand de la conditiile de testare definite anterior
- se identifica datele de testare necesare ( credentiale, coduri, utilizatori, tabele populate, etc )

5. Test Implementation
- este o etapa administrativa, pregatitoare a etapei de executie in care ne asiguram ca avem toate informatiile necesare
pentru a putea incepe executarea testelor
- in aceasta etapa ne asiguram ca avem credentiale ( user si parola ), acces, mediu de testare pregatit si functional,
se creaza datele de testare identificate in etapa anterioara ( ex: daca la test design am identificat ca am un test
de filtrare de useri, in etapa de implementation fie o sa imi creez userii pentru filtrare, fie o sa ii import dintr-un
fisier extern )

Suita de teste = o grupare de teste care au acelasi obiectiv ( teste functionale, teste de regresie,
teste non-functionale, test blackbox, test whitebox, teste specifice unui release, etc )
Suitele de teste poarta un nume diferite in functie de aplicatia pe care o folosim pentru testare ( zephyr - test cycle,
test rail - test suite, testlink - test plan, practi test - test library ? )

6. Test execution
- se executa testele definite in etapa de analiza
- se raporteaza rezultatele  testelor intr-un tool de gestiune a testarii ( exemple de tool-uri: zephyr, alm, testrail,
practitest, testlink, asana, bugzilla )
- se deschid rapoarte de bug petnru testele pentru care rezultatul asteptat nu coincide cu cel actual
- in urma fixarii bug-urilor se face retestare si testarea de regresie
- se genereaza rapoarte de status ( daily status reports ) care sunt trimise periodic catre team leader si project
manager

7. Test completion
- se evalueaza criteriile de iesire
- se inchide bug-urile reziduale neinchise
- se arhiveaza materialele de testare ( in practica nu prea exista aceasta etapa )
- se genereaza rapoarte de inchidere a testarii ( test summary raprot / test completion report ) si se trimit catre
stakeholders
- se creaza un test report = un document care contine rezultatul tuturor activitatilor desfasurate in timpului
procesului de testare ( care au fost testarii implicati, care au fost cerintele de business acoperite, functionalitati
care au fost in scope / not in scope, cate teste un executat, cate au fost passed si cate failed, cate bug-uri am gasit,
cate mai sunt deschise, daca au fost identificate riscuri DE PRODUS, lessons learned, good practices )



"""