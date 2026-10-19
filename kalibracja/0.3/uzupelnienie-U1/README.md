# U1 — status przygotowania

**Stan: 2026-10-19.** Trwa przygotowanie po zatwierdzeniu korpusu; nie rozpoczęto ocen U1.
Korpus wybrano deterministycznie. Właściciel zatwierdził sześć publikacji
2026-10-19 o 16:36:25 +02:00 oraz przyjął ograniczenie różnorodności wydawców.
Wejście nie jest jeszcze dopuszczone do ocen. Start wymaga osobnego polecenia.

Właściciel zatwierdził limit trzech publikacji jednego rzeczywistego wydawcy.
Decyzję zapisano przed wyborem. Pozostałych kryteriów nie zmieniono.
Zestaw obejmuje dwóch wydawców, po trzy publikacje, co ogranicza różnorodność
redakcyjną; nie jest próbą reprezentatywną.

| Element | Stan |
| --- | --- |
| Potwierdzona zamknięta pula | 25 publikacji; co najmniej dwóch kandydatów dla każdego profilu. |
| Udokumentowane wyłączenia | 102 zachowane bez usuwania historii. |
| Wpisy nierozstrzygnięte | 37 niewłączonych z konkretnymi warunkami; nie uznano ich za zakazane ani definitywnie niekwalifikujące się. |
| Pełny algorytm | 10 206 kombinacji, 798 dopuszczalnych przypisań; niezależne potwierdzenie minimum. |
| Korpus zatwierdzony | Sześć różnych publikacji pokrywających P1–P6; kontrola kolizji zakończona. Wybór i kolejność bez zmian. |
| Materiały główne | Pełne publikacje, materiały centralne, dostępne źródła i historia wersji zachowane prywatnie. |
| Pakiet do przeglądu | Neutralne instrukcje, kontekst, manifesty i sumy; osobna dokumentacja koordynatora. |
| Biblioteka do ocen | Nie potwierdzono kompletności. Z 12 otwartych pozycji trzy zamknięto w określonym zakresie; pozostaje osiem kwestii praw i jedna pozyskania urzędowego źródła. |
| Dokładny snapshot | Niepotwierdzony w środowisku wykonawczym. |
| Izolacja 12 instancji | Niepotwierdzona; próba utworzenia sandboxa zakończona odmową systemową. |
| Prototyp interfejsu plików | 8 testów syntetycznych przeszło; nie zastępują testów rzeczywistego środowiska, kontekstu i mediów. |
| Uruchomienia | 0 z 12; brak ocen, porównań i wyników. |

Nie wykonano nowych wyszukiwań puli i nie dodano kandydatów. Zachowano
poprzednie materiały oraz aktualne rejestry v2. Dobór nie korzystał z dawnych
ocen ani przewidywanych werdyktów. Historyczna niewykonalność przy limicie
dwóch dotyczyła potwierdzonej puli; po zatwierdzeniu limitu trzech wybór jest
wykonalny. Nierozstrzygniętych wpisów nie przeklasyfikowano.

Zamknięcie trzech pozycji dotyczy dokumentacji odsyłaczy i podstawy prawnej;
nie oznacza odzyskania nieodczytanych stron ani uzyskania praw do oprogramowania.
Wszystkie materiały centralne są zachowane. Uzupełnienia i decyzje zachowano
prywatnie wraz z wcześniejszą historią. Pełne zamrożenie wejścia pozostaje zablokowane.

Przed startem trzeba zamknąć istotne braki biblioteki i podstaw wykorzystania,
potwierdzić integralność i kompletność całego wejścia,
udokumentować dostępny dokładny model/snapshot oraz jednakowe
ustawienia i narzędzia, sprawdzić egzekwowaną izolację kontekstu, plików i
wszystkich kanałów sieciowych, a następnie uzyskać osobną zgodę na start.
Brak pakietu lub środowiska nie jest wynikiem o jakości publikacji ani metody.
Zatwierdzenie korpusu jest zapisane i nie wymaga ponowienia dla niezmienionego
wyboru. Nie przyjęto wariantu API; ewentualna zmiana powierzchni wykonawczej
wymaga osobnej decyzji. Zatwierdzenie korpusu nie jest zgodą na rozpoczęcie ocen.

Przygotowanie nie zmienia metodologii ani skilla, nie rozpoczyna B2,
nie modyfikuje wcześniejszych wyników, wydań, materiałów 0.4 ani laboratoriów B2.
Zmiany są przeznaczone do osobnej gałęzi i roboczego PR, bez scalenia.
Publiczny zakres obejmuje wyłącznie ten opis, protokół i test kompletności.
Prywatne rejestry, nazwy publikacji, kopie, manifesty i materiały pozostają poza
repozytorium. Zbiorczego checkpointu nie przekazuje się oceniającym.

- [Protokół U1-1.3](protokol.md).
- [Oficjalne wydanie v0.3.0](../../../wydania/v0.3.0.md).
- [Standard 0.3](../../../metodologia/0.3/standard.md).
