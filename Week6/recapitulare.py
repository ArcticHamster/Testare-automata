"""
Selector ( sau locator ) = o modalitate ( abstracta ) prin care definim cum poate fi identificat un element din DOM

1. Link Text: un text (exact) care are un link ancorat -> un element cu tag-ul HTML <a>
2. Partial Link Text: un text (parte dintr-un text) care are un link ancorat -> un element cu tag-ul HTML <a>
3. Tag name - tag-ul HTML
4. ID: dupa id-ul elementului
5. Class name - atributul class al unui element
6. Xpath - calea relativa sau absoluta catre un element din DOM
    XPath absolut: /html/body/div/form/div/div[2]/input
    XPath relativ: //input[@id='first-name']
7. CSS - selectors css: input[id='first-name']
"""

"""
Etapele unui Sprint:

a) Planificarea sprintului
    - Eechipa de scrum se intalneste pentru a stabili obiectivele sprintului si a identifica lista de functionalitati
    sau cerinte pe care le va aborda in timpul sprintului
    - durata sprintului este stabilita in avans( de ex, 2 saptamani)
    - se identifica si se estimeaza sarcinile necesare pentru indeplinirea obiectivelor sprintului.

b) Daily Scrum
    - in fiecare zi lucratoare in timpul sprintului, echipa se intalneste intr-o reuniune scurta (15min), numita
    Daily Scrum sau Stand-up meeting
    - fiecare membru raporteaza ce a realizat in ziua precedenta si ce va realizare in ziua respectiva si daca are 
    vreo problema sau obstacol (blocker) 

c) Dezvoltarea
    - echipa lucreaza in mod colaborativ la sarcinile planificate in sprint
    - echipa isi organizeaza activitatile zilnic si lucreaza pentru a atinge obiectivele stabilite
    - in timpul sprintului pot aparea modificari sau ajustari ale cerintelor. Acestea sunt gestionate prin intermediul
    Product Backlog si pot fi luate in conisderare sprintul urmator 

d) Revizuirea sprintului (sau demo)
    - la sfarsitul sprintului, echipa de scrum prezint rezultatele obtinute clientilor sau persoanelor interesate
    - demonstrarea functionalitatilor realizate si feedback-ul colectat ajuta la validarea progresului

e) Retrospectiva
    - dupa revizuirea sprintului, echipa de scrum se intalneste pentru o retrospectiva
    - scopul este de a evalua modul in care a decurs sprintul, de a identifica ce a functionat bine si ce poate sa fie 
    imbunatatit
    - echipa ia decizii asupra modului in care poate imbunatati procesul in viitoarele sprinturi
    
EPIC 
    Epic este o functionalitate mare sau un set de functionalitati care pot fi livrate intr-un singur sprint si care
    trebuie sa fie divizate in story-uri. Epic-urile sunt deoseori folosite pentru a descrie cerinte de nive inalt
    al clientilor sau utilizatorilor
    
USER STORY
    User Story este o descriere scurta si simpla a unei caracteristici sau functionalitati de care are nevoie
    un utilizator sau client. Aceasta este scrisa din perspectiva utilizatorului si trebuie sa fie scrisa intr-un
    limbaj simplu, astfel incat toti membrii echipei de dezvoltare sa inteleaga cerintele

ACCEPTANCE CRITERIA
    Acceptance criteria sunt criteriile care trebuie indeplinite pentru ca o functionalitate sa fie considerata completa
    si testabila. Aceasta sunt definite de obicei in prealabil, inainte ca echipa de dezvoltare sa inceapa sa lucreze
    la o anumita functionalitate si pot include conditii de acceptare, cerinte de performanta, limitari de timp sau
    alte cerinte specifice ale utilizatorilor sau clientului. Aceste criterii sunt folosite pentru a confirma ca 
    functionalitatea este completa si ca respecta cerintele specifice ale utilizatorului sau clientului.

"""

