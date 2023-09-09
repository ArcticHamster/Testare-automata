"""
O metodologie de software development reprezinta o serie de proceduri care descriu felul in care echipa se organizeaza
cu scopul de a crea un produs software.

Exista mai multe metologii de testare:
- Agile
- Waterfall
- V-model

Waterfall = O metodologie de software development care presupune desfasurarea activitatilor in cascada ( adica
rezultatul unei etape reprezinta date de intrare pentru urmatoarea etapa )

Este o metodologie mai rigida care presupune finalizarea unei etape in mod complet inainte de inceperea urmatoarei
etape
    - terminam cerintele de business
    - terminam de facut dezvoltarea
    - terminam de facut testarea
    - lansam produsul

Dezavantaje:
    - daca vrem sa modificam ceva in mijlocul procesului de dezvoltare / testare (adica ne-am razgandit si vrem altceva,
    sau vrem ceva aditional) atunci trebuie sa se creeze un proiect nou care sa urmeze toate etapele anterioare, cu buget
    si timeline separat.
    - feedback-ul din partea clientului este primit la sfarsit si nu o sa avem mult timp de ajustare.

Avantaje:
    - avem buget exact si stim de la inceput cat o sa platim
    - stim exact cum o sa arate produsul inca de la inceput
    - stim cand trebuie sa terminam de creat / testat produsul.

Agile = O metodologie de software development care presupune dezvoltarea produsului pe bucati intr-o serie de
mini-proiectele de dezvoltare
Este o metodolgie mai flexibila care permite schimbari mai rapide si ofera feedback timpuriu

Dezavantaje:
    - nu stim exact cum va arata produsul de la inceput (avem o schimbate dar nu stim exact)
    - daca nu stim cum o sa arate produsul nu stim nici cat o sa ne coste
    - daca nu stim cat de complex o sa fie produsul nu stim exact nici cat va dura
    - daca echipa nu comunica bine si exista conflicte in echipa sansele ca produsul sa esueze cresc considerabil
    - documentatie se creeaza, dar e mai sumara si doar pentru lucruri esentiale, ceea ce face nevoia de comunicare esentiala
    - nu este recomandat atunci cand avem un proiect cu dedline strans sau buget limitat.

Avantaje:
    - este mai flexibil si permite efectuarea de modificari in timpul procesului de software development / testing
    - primim feedback timpuriu legat de functionalitatea produslui si avem o siguranta mai mare asupra calitatii
    finale a produsului din punct de vedere al nevoilor clientului

Elemte ale metodologiei Agile:

    - Backlog = Totalitatea elemtelor care se doresc a fi implementate in cadrul unui proiect.

    - Backlog rafinement = Filtrarea functionalitatilor care nu sunt urgente sau care sunt mai greu de implementat pentru
    beneficiu pe care il aduc si respectiv clarificarea si detalierea functionalitatilor ramanse de implementat.

    - Sprint plannig = Definirea tuturor functionalitatilor care se doresc a fi implementate intr-un sprint.

    - Daily Standup = Sedinta zilnice care au scopul de identifica:
            - la ce s-a lucrat in ziua anterioara
            - la ce lucreaza acum / azi
            - daca exista blockere care ne impiedica sa ne implinim taskurile.

    - Sprint review = O analiza a tuturor functionalitatilor care au fost implementate si respectiv mutarea
    functionalitatilor neimplementate intr-un alt sprint

    - Sprint retrospective = Analiza desfarurarii sprint-ului din punct de vedere al lucrurilor care au fost ok si
    trebuie pastrate si respectiv din punctul de vedere al lucrurilor care nu au fost ok si trebuie imbunatatite.

Sprint = O perioada de timp in care ne asumam sa implementam o serie de functionalitati. De regula se defineste la un
interval de doua, trei saptamani, dar este la latitudinea echipei.

Un proiect implementat in Agile este format dintr-o succesiune de sprint-uri care fiecare implementeaza cate o bucatica
din produs
Rezultatul unui sprint se numste product increment (pentru ca incrementeaza numarul de functionalitati gata de utilizare
pentru produsul nostru)

Kanban - O metodologie de software development care presupune desfasurarea activitatii

Sirul lui fibonacci = 1, 1, 2, 3, 5, 8, 13, 21
"""