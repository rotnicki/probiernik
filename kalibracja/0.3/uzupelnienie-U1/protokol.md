# U1 — badanie uzupełniające oficjalną metodologię 0.3

**Wersja protokołu:** U1-1.2 — 2026-10-19; zatwierdzony limit trzech publikacji wydawcy

**Podstawa dokumentacji:** master `38babd2231c6ea2af786913c7c6040423b27a88d`

**Metodologia:** oficjalne, zamrożone wydanie `v0.3.0`

**Commit znacznika:** `853404df15f05ba769d2440644a14fd0c77ec2e3`
**Status:** przygotowanie do przeglądu; nie rozpoczęto ocen. Wybrano sześć
publikacji; korpus oczekuje na zatwierdzenie. Wejście nie jest dopuszczone do
ocen: pozostają udokumentowane braki biblioteki i niepotwierdzone warunki
wykonawcze. Zatwierdzenie korpusu i start są osobnymi decyzjami właściciela.

## 1. Cel i ograniczenia

U1 sprawdza stosowanie doprecyzowań T2 i S11–S15 oraz granic słabiej pokrytych
we wcześniejszych badaniach. Nie zakłada, że metodologia wymaga zmiany.
U1 jest badaniem uzupełniającym oficjalną 0.3, a nie rozpoczęciem B2
ani zatwierdzeniem zmian metodologicznych do 0.4.

Historyczny polski pilotaż i B1 poprzedzały wdrożenie T2 i S11–S15.
Wyników B1 nie traktuje się jako bezpośredniego potwierdzenia działania tych
późniejszych doprecyzowań. Dawnych ocen nie przelicza się.

Sześć publikacji nie stanowi próby reprezentatywnej. Badanie nie mierzy
częstości błędów w polskich publikacjach, nie porównuje rodzin AI i nie
ustanawia niezależnego wzorca prawdziwości. Zgodność dwóch ocen może oznaczać
także ten sam błąd. Niezaobserwowanie granicy nie oznacza jej poprawności.

Właściciel 2026-10-19 zatwierdził zwiększenie limitu z dwóch do trzech
publikacji jednego rzeczywistego wydawcy. Decyzję zapisano i zahaszowano
przed wyborem. Pozostałe kryteria pozostają bez zmian. Zachowano wcześniejsze
rejestry i historię decyzji. Wybrany zestaw obejmuje tylko dwóch rzeczywistych
wydawców, po trzy publikacje; ogranicza to różnorodność redakcyjną i możliwość
uogólniania obserwacji. Zgoda na limit nie jest zatwierdzeniem korpusu ani startu.

## 2. Pytania badawcze

1. Czy C i J otrzymują liczbę albo `nd` z właściwej przyczyny, również przy
   przywołaniu normy, oczekiwaniach uczestników i szerokiej obietnicy poradnika?
2. Czy `nd` jest stosowane zgodnie ze standardem w różnych wymiarach,
   a nie jako zastępstwo braku danych lub dowodów?
3. Czy test minimalnej uczciwej poprawki rozdziela `srednie` i `duze`?
4. Czy uzasadnienia A–L dotyczą właściwego przedmiotu, a wspólna obserwacja
   ma osobno opisane skutki?
5. Czy grupy odbiorców oraz wiedza konieczna i pomocna są tworzone spójnie?
6. Czy rekonstrukcja wersji historycznej ma rzeczywisty, osobny dowód,
   zamiast tylko daty publikacji lub bieżącego SHA-256?
7. Czy brak rdzenia, brak dowodów zewnętrznych i brak danych pomocniczych
   prowadzą do różnych, uzasadnionych decyzji o rozstrzygalności?
8. Czy wszystkie cztery przesłanki krytyczności są sprawdzane bez obniżenia progu?
9. Czy oceniający dopuszcza `rzetelny`, nie szukając sztucznie zastrzeżeń?

Publikacje sondują granice; nie mają oczekiwanych werdyktów, znaczenia
problemów ani wartości `nd`. Nie trzeba uzyskać każdego rodzaju wyniku.

## 3. Projekt i role

Dokładnie sześć publikacji, po dwie niezależne oceny A/B, łącznie 12 ocen.
Jedna rodzina AI: ChatGPT; bez ludzi jako oceniających. Każda ocena ma osobną,
świeżą i odizolowaną instancję, która ocenia tylko jedną publikację.
Wszystkie używają tego samego dokładnie udokumentowanego modelu, snapshotu,
ustawień, narzędzi, instrukcji, metodologii i wspólnej biblioteki źródeł.

Koordynator przygotowuje wejście i kontroluje technikę, ale nie wykonuje
żadnej z dwunastu ocen. Po ich zamknięciu porównuje wyniki. Właściciel
zatwierdza korpus i start; nie wystawia ocen ani nie zastępuje AI przy
rozbieżności. Oceniający sam tworzy mapę twierdzeń; nie otrzymuje jej od
koordynatora. Dwa przebiegi wewnętrzne jednej analizy nie zastępują A/B.

## 4. Profile korpusu

| Profil | Widoczna cecha kwalifikacyjna, bez oceny rzetelności |
| --- | --- |
| P1 | Wąskie wyjaśnienie prawne: określony obowiązek, zakres, wyjątek lub norma. |
| P2 | Przedstawione doświadczenia, potrzeby, wypowiedzi lub badania użytkowników. |
| P3 | Instrukcja techniczna: konkretne kroki, kod lub konfiguracja interfejsu/usługi. |
| P4 | Poradnik o jawnej szerokiej obietnicy lub obejmujący wiele zadań i ról. |
| P5 | Materiał z historią wersji: wskazana wcześniejsza zachowana treść, nie tylko data aktualizacji. |
| P6 | Publikacja z głównym wnioskiem opartym na wskazanym zewnętrznym raporcie, danych lub załączniku. |

P5 nie przesądza, że dowód historyczny będzie wystarczający w ocenie.
P6 nie wymaga niedostępności artefaktu. Wszystkie znalezione dostępne materiały
centralne trzeba dostarczyć; nie wolno ich ukrywać dla uzyskania braku
rozstrzygnięcia. Jedna publikacja może kwalifikować się do kilku profili,
ale w korpusie występuje tylko raz.

## 5. Wyszukiwanie i kwalifikacja

Przed pierwszym zapytaniem zapisuje się i haszuje prywatny
`plan-wyszukiwania.json`: treść i kolejność zapytań, nazwę narzędzia,
dostawcę, parametry, limity, kryteria, kanonizację i algorytm wyboru.
Narzędzie: `search_service_web_run`, pole `system2_search_query`,
odpowiedź `long`, bez filtrów domeny i daty. Dostawcę bazowej wyszukiwarki
zapisuje się jako `not_available`, jeżeli usługa go nie ujawnia.

| Profil | Zapytanie 1 | Zapytanie 2 |
| --- | --- | --- |
| P1 | dostępność cyfrowa obowiązki ustawa WCAG | dostępność cyfrowa prawo wyjaśnienie |
| P2 | dostępność cyfrowa badanie użytkowników wyniki | dostępność cyfrowa potrzeby uczestnicy badania |
| P3 | dostępność cyfrowa instrukcja konfiguracja | dostępność formularza instrukcja kod |
| P4 | dostępność cyfrowa kompleksowy poradnik | dostępność cyfrowa poradnik dla projektantów programistów |
| P5 | dostępność cyfrowa poradnik wersja aktualizacja | dostępność cyfrowa publikacja poprzednia wersja |
| P6 | dostępność cyfrowa raport dane załącznik | dostępność cyfrowa artykuł wyniki pełny raport |

Pierwotny plan obejmował dokładnie 12 zapytań w kolejności P1–P6, po dwa. Z każdej
odpowiedzi rejestruje się pierwszych 10 różnych adresów albo wszystkie,
jeżeli zwrócono mniej. Zachowuje się pełną odpowiedź, czas, kolejność i
referencje. Bez paginacji, dopisywania zapytań i poszerzania domen po
poznaniu puli. Otwieranie wyników i ich własnych odnośników służy wyłącznie
kwalifikacji, ustaleniu tożsamości, praw i materiałów, nie dodawaniu kandydatów.

Osobno zatwierdzono i wykonano Q13–Q18. Historyczne plany, odpowiedzi i decyzje
pozostają niezmienne; nie wykonuje się ponownie zachowanych zapytań.

| Zapytanie | Profil | Dokładna treść |
| --- | --- | --- |
| Q13 | P3 | dostępność formularzy HTML etykiety instrukcja |
| Q14 | P3 | dostępność przycisków klawiatura przykład kodu |
| Q15 | P3 | dostępność obrazów tekst alternatywny poradnik HTML |
| Q16 | P5 | "dostępność cyfrowa" "historia zmian" |
| Q17 | P5 | "dostępność" "wersja 1.0" "wersja 2.0" |
| Q18 | P5 | "dostępność cyfrowa" "wersje archiwalne" |

Limity uzupełnienia: jedno wykonanie każdego zapytania, odpowiedź `long`,
pierwsze 10 różnych URL, najwyżej 60 pozycji dodatkowych, bez paginacji,
filtrów daty/domeny i dopisywania zapytań. Połączony zapis Q01–Q18 zawiera
18 wykonanych zapytań i 148 różnych adresów przed ustaleniem tożsamości.
Nie jest to liczba zakwalifikowanych publikacji.

Zatwierdzono również jedną turę archiwalną. Jej jedynym źródłem nowych
kandydatów jest sekcja „Resources” polskiej części wykazu tłumaczeń W3C WAI.
Przed sprawdzaniem kandydatów utrwala się plan, cały wykaz, datę, adresy
i sumy. Rozpatruje się wszystkie różne adresy rosnąco według kanonicznego URL,
najwyżej 20 publikacji. Więcej niż 20 adresów blokuje turę przed kwalifikacją;
nie wybiera się ręcznie części wykazu. Odczytany wykaz zawierał 16 adresów.

Dla każdego adresu sprawdza się bieżącą publikację i wykaz Internet Archive.
Po usunięciu dokładnych powtórzeń zapisu, w porządku od najstarszej daty,
rozpatruje się najwyżej 10 różnych zachowanych kopii. Zachowuje się żądanie,
pełną otrzymaną listę, sposób uporządkowania, odpowiedzi i błędy. Niedostępny
wykaz nie uprawnia do wyboru dogodnych kopii ani do twierdzenia, że archiwum
nie zawiera żadnego zapisu.

W razie potrzeby używa się historii właściwego polskiego pliku w oficjalnym
repozytorium wskazanym przez wydawcę: najwyżej 20 ostatnich zapisów i najwyżej
10 różnych wersji treści. Historia angielskiego oryginału nie zastępuje historii
polskiej publikacji. Zapis redakcyjny w Git nie dowodzi publikacji na stronie
w dniu commita. Obie podstawy dowodu dokumentuje się osobno.

Dowód wcześniejszej treści zawiera tożsamość, język, datę lub oznaczenie wersji,
stabilny identyfikator, dokładny adres zapisu, objęty zakres i ograniczenia.
Sprawdza się tekst, rozwijane sekcje, ilustracje, tabele oraz kod. Rozdziela
się datę publikacji, aktualizacji, archiwizacji, zapisu Git i własnego pobrania.
Bieżąca kopia i jej SHA-256 nie dowodzą treści historycznej. Wcześniejsza kopia
nie musi różnić się znaczeniowo; opis różnic nie jest oceną ich poprawności.

Ta tura nie dopuszcza nowych wyszukiwań ogólnych, innych wykazów wydawców
ani kolejnej tury bez osobnej decyzji. Nowe wpisy łączy się z zachowaną pulą,
z pełnym pochodzeniem i wyłącznie udokumentowanym usuwaniem duplikatów.
Brak kompletnej kwalifikacji lub dopuszczalnego przypisania nadal blokuje wybór.

Domknięcie kwalifikacji obejmuje wyłącznie zachowaną pulę 164 adresów,
bez nowych wyszukiwań ani kandydatów. Odczyt znanej strony, jej załączników,
wskazanego repozytorium, licencji lub regulaminu nie jest kolejną turą
pozyskiwania. Wcześniejszych planów, odpowiedzi i decyzji nie nadpisuje się.
Wyniki kontroli możliwości przypisania dotyczą wyłącznie potwierdzonej puli;
nierozstrzygnięte przypadki nie dowodzą niemożliwości całego pierwotnego wykazu.

Warunki włączenia:

- samodzielna publikacja po polsku, której głównym tematem jest dostępność;
- 300–5000 słów treści głównej; liczba słów to tokeny rozdzielone białym
  znakiem po oddzieleniu nawigacji, reklam i elementów niezwiązanych;
- pełna treść, centralne tabele, ilustracje i kod możliwe do odczytu i zachowania;
- wiarygodnie ustalona tożsamość i co najmniej jeden profil;
- brak kolizji z wcześniejszymi korpusami;
- udokumentowana podstawa prawna zachowania i udostępnienia pełnego wejścia
  instancjom w zakresie badania.

Nie wyklucza się ze względu na spodziewany wynik, reputację autora, datę
publikacji ani brak ideału. W kwalifikacji wolno przeczytać tylko tyle
treści, ile potrzeba do ustalenia cech, długości, zależności i praw.
Nie sprawdza się prawdziwości twierdzeń ani wielkości potencjalnych problemów.
Każde wyłączenie ma konkretną, neutralną przyczynę i dowód lokalizacji.

Pula wymaga co najmniej dwóch zakwalifikowanych kandydatów dla każdego
profilu oraz możliwości przypisania sześciu różnych publikacji przy limicie
trzech na wydawcę. Jeżeli warunki nie są spełnione, wybór zatrzymuje się
i przedstawia brak właścicielowi. Nie rozszerza się automatycznie wyszukiwania.

Stan domknięcia z 2026-10-19: formalnie zamknięto pulę wyboru obejmującą
25 potwierdzonych publikacji z aktualnych rejestrów v2. Zachowano udokumentowane
wyłączenia 102 wpisów. Pozostałe 37 pozostaje niewłączone z konkretnymi
nierozstrzygniętymi warunkami zapisanymi prywatnie; nie uznano ich za zakazane
ani definitywnie niekwalifikujące się. Nie dodano kandydatów i nie ponowiono
wyszukiwań puli. Dalsze pozyskanie dotyczy wyłącznie materiałów wybranych
przypadków i potrzebnych źródeł. Historyczny brak rozwiązania przy limicie
dwóch nie jest przenoszony na nowy limit ani na wszystkie nierozstrzygnięte wpisy.

## 6. Tożsamość i kontrola kolizji

Prywatnie porównuje się wyłącznie dane identyfikujące: URL i aliasy, tytuł,
autora/podpis, wydawcę oraz identyfikator wersji. Źródła wykluczeń obejmują
polski pilotaż P01–P05, pierwotny i końcowy korpus B1 z podmianami i wszystkimi
rezerwami, również nieuruchomionymi, oraz zachowany korpus B2.
Nie wykorzystuje się dawnych wyników do doboru.

Kanonizacja: ustalone przekierowania i deklarowany canonical przy zgodnej
tożsamości; małe litery hosta; usunięcie portu domyślnego, fragmentu oraz
parametrów `utm_*`, `fbclid`, `gclid`, `msclkid`; pozostałe pary
zapytania sortowane. Zachowuje się wielkość liter ścieżki, parametry
funkcjonalne i końcowy ukośnik, chyba że przekierowanie potwierdza równoważność.
Sama różnica URL nie wyklucza duplikatu, przedruku lub aktualizacji tej samej
publikacji. Porównuje się także tytuł, autorstwo i zakres treści.

Niedostępny wymagany prywatny wykaz lub nierozstrzygnięta tożsamość publikacji
blokuje wybór. Nie publikuje się wykazów kolizji ani wcześniejszych manifestów.
Rejestr zachowuje źródło tożsamości, datę kontroli i decyzję, bez ocen.

## 7. Deterministyczny wybór

Po formalnym zamknięciu puli wyboru utrwala się potwierdzone publikacje
oraz oddzielne rejestry wyłączeń i warunków nierozstrzygniętych. Dla każdej pary
profil–publikacja oblicza się SHA-256 bajtów UTF-8 dokładnego ciągu:

`probiernik-U1-korpus-v1|<profil>|<kanoniczny_URL>`

Rozpatruje się pełne przypisania w kolejności P1, P2, P3, P4, P5, P6:
jedna publikacja na profil, sześć różnych tożsamości, najwyżej trzy tego
samego rzeczywistego wydawcy. Wybiera się leksykograficznie najmniejszą
krotkę par `(skrót, kanoniczny_URL)` spośród wszystkich dopuszczalnych
przypisań. Nie wystarczy sześć niezależnych minimów, gdy łamią limit wydawcy
lub powtarzają publikację. Remis rozstrzyga kanoniczny URL.

Wybrane publikacje porządkuje się według
`SHA-256("probiernik-U1-kolejnosc-v1|<kanoniczny_URL>")`, następnie URL,
i nadaje neutralne ID U1-01–U1-06. Profile, skróty wyboru i uzasadnienia
doboru pozostają w przestrzeni koordynatora. Oceniający nie otrzymują
informacji o spodziewanym rodzaju przypadku. Determinizm dotyczy zachowanej
puli; nie zakłada się, że wyszukiwarka zwróci ją ponownie po czasie.

Po wyborze nie podmienia się publikacji, ponieważ nie dała oczekiwanej
granicy. Nie ma automatycznej rezerwy. Błąd techniczny przed startem wymaga
udokumentowania i osobnej decyzji, nie cichego przesunięcia rankingu.

W przygotowaniu z 2026-10-19 sprawdzono wszystkie 10 206 pełnych kombinacji.
798 spełniało warunki; wybrano minimum zgodnie z powyższą regułą. Niezależny
przegląd uporządkowany potwierdził ten sam zestaw. Sprawdzono wszystkie warunki
przypisania i kolizje z zachowanymi wykazami wcześniejszych korpusów.
Nie wykorzystano wcześniejszych ocen ani przewidywanych werdyktów.

## 8. Prawa, prywatność i podział przestrzeni

Publiczne repozytorium zawiera tylko ten protokół, objaśnienie statusu i test
kompletności. Nie zawiera list kandydatów, przypisania nazw do przypadków,
kopii publikacji, pełnych źródeł, manifestów prywatnych, metryk wykonania
ani przyszłych analiz.

Materiały U1 przechowuje się prywatnie, osobno od sześciu laboratoriów B2.
Prywatność ani publiczny dostęp nie są same w sobie podstawą kopiowania.
Dla każdego utrwalanego materiału zapisuje się licencję, zgodę lub właściwy
status materiału urzędowego, zakres uprawnienia i dowód. Bez takiej podstawy
nie zapisuje się pełnej chronionej treści. Wątpliwość blokuje jej zamrożenie.

Brak jawnej licencji nie oznacza zakazu wykorzystania. Możliwe uprawnienie
ustawowe sprawdza się w aktualnych źródłach urzędowych dla konkretnego
materiału, potrzebnego zakresu kopii i przekazania do AI. Sam fakt publikacji
w BIP lub finansowania ze środków publicznych nie rozstrzyga praw do każdej
treści redakcyjnej i fotografii. Podstawa dotycząca załącznika nie obejmuje
automatycznie całego towarzyszącego artykułu. Jeżeli zakres praw pozostaje
niejasny, status jest nierozstrzygnięty, a nie „zakazany” lub „kwalifikowany”.
Nie kontaktuje się z autorami bez osobnej zgody.

Przestrzeń koordynatora zawiera rejestry wyszukiwania, profili, kolizji i wyboru.
Przestrzeń oceniającego zawiera wyłącznie neutralną instrukcję, oficjalny
pakiet, jeden przypadek i wspólną bibliotekę źródeł, bez wcześniejszych
raportów, historii tej rozmowy, profili, innych wyników ani połączenia GitHub.
Publicznie można później opublikować tylko bezpieczne agregaty bez możliwości
pośredniego połączenia nazwy publikacji z negatywnym wynikiem.

## 9. Zamrożenie wejścia i biblioteka źródeł

Artefaktem metodologii jest oficjalny
`assess-accessibility-articles-v0.3.0.zip`, SHA-256:
`72b2604d3a9e4581241570c4ca89726e5a8dd7a8e3fd6addafb3a4596b9a6979`.
Sprawdza się jego pochodzenie, integralność ZIP, manifest, licencje i kopie
materiałów. Nie używa się dawnej paczki B1/B2 ani bieżącego skilla jako
zamiennika oficjalnego wydania.

Zachowuje się bez zmian schematy, walidator i identyfikatory `0.3-draft`.
Jest to identyfikator formatu, nie aktualny status metodologii.
Dodatkowe dane badawcze trafiają do osobnych rejestrów, nie do schematów 0.3.

Każdy przypadek otrzymuje pełną publikację, materiały centralne, dostępny
kontekst miejsca i dowody historii wersji. Dla dziesięciu elementów kontekstu
z rozdziału 6.2 standardu dokumentuje się pozyskanie albo rzeczywisty brak;
koordynator nie tworzy za oceniającego profilu, uzasadnień H/L ani mapy twierdzeń.

Bibliotekę przygotowuje się przed startem: wszystkie dostępne materiały
przywołane przez wybrane publikacje oraz źródła pierwotne odpowiadające ich
widocznym tematom — prawo, datowane standardy, dokumentacja technologii,
badania i dane. To pozyskanie zakresu, a nie sprawdzenie zgodności twierdzeń.
Rejestr wskazuje źródło, datę i wersję, objęty zakres, prawa, braki i sumy.
Nie deklaruje się kompletności bez dowodów.

Wszystkie 12 instancji otrzymują bajtowo identyczną bibliotekę, ten sam
pakiet i datę odniesienia. Nie mają otwartego internetu podczas ocen.
Jedynie własna publikacja i oznaczenie przebiegu różnią wejścia przypadków;
A i B danej pary mają identyczne materiały. Brak źródła w pakiecie nie
może być przedstawiony jako wada publikacji. Nie wolno ukrywać dostępnego
artefaktu ani wykorzystywać ograniczenia przygotowania do sztucznego werdyktu.

Manifest wejścia wymienia wszystkie pliki i ich SHA-256 oraz
`raw_bytes`, `rendered_capture` lub `canonical_text`. Normalizacja tekstu
jest jawna i zachowuje pełne znaczenie, kod, kolejność, tabele i podpisy.
Biblioteka i wejście są zamrożone po kontroli; nie dopisuje się źródeł
w środku serii. Nowy istotny brak zatrzymuje przebieg i trafia do koordynatora.
Zmiana wejścia wymaga osobnej decyzji o ponownym zamrożeniu, nie kontynuacji
rzekomo identycznego doświadczenia.

`SHA256SUMS` ma wiersze `<sha256>  <ścieżka względna>` w porządku ścieżek,
UTF-8 i LF. Obejmuje niezmienne wejście i manifest, ale nie siebie ani zmienne
rejestry wykonania. SHA-256 jego bajtów jest identyfikatorem wspólnego wejścia.
Archiwum przestrzeni koordynatora ma odrębną sumę; nie jest wejściem oceniających.

Stan przygotowania do przeglądu: zachowano sześć pełnych publikacji,
materiały centralne, dostępne źródła i dowody historyczne, dziesięć elementów
kontekstu z jawnymi ograniczeniami, neutralną instrukcję, manifesty i sumy.
Oficjalny pakiet zweryfikowano. Przygotowano rozdział dokumentacji koordynatora
i wejścia pojedynczego przypadku. Wspólna biblioteka ma rejestr braków
dodatkowej dokumentacji, praw oraz nieudanych pobrań; nie potwierdzono jej
kompletności do uruchomienia. Kopia do przeglądu nie jest zamrożeniem wejścia
dopuszczonego do ocen. Istotne braki trzeba zamknąć, a następnie zweryfikować
i zatwierdzić sumy całego wejścia przed serią. Nie zmienia to wybranego korpusu
i nie uruchamia automatycznych podmian.

Zbiorczy checkpoint i manifest koordynatora obejmują wszystkie przypadki;
nie przekazuje się ich oceniającym. Każda instancja otrzyma manifest i pliki
wyłącznie własnego przypadku oraz identyczną część wspólną. Źródła wzajemnie
przywoływane pozostają neutralnymi pozycjami biblioteki, bez mapowania do
innych przypadków, profili lub wyników.

## 10. Model i rzeczywista izolacja

Plan obejmuje U1-01-A, U1-01-B, …, U1-06-A, U1-06-B — 12 pustych kontekstów
bez historii, pamięci projektu i wcześniejszych wyników. Kolejność uruchomień
wynika z neutralnych ID, A następnie B; nie porównuje się ich w trakcie serii.

Przed dopuszczeniem startu trzeba udokumentować model i wersję/snapshot
z rzeczywistego środowiska, ustawienie rozumowania, parametry generowania
dostępne lub niedostępne, wersje narzędzi, limity, dostęp do pamięci i politykę
plików. Nie zgaduje się etykiet ani nie uznaje ogólnej nazwy ChatGPT za snapshot.
Zmiana modelu w środku serii blokuje dalsze uruchomienia.

Każda instancja ma tylko wejście read-only oraz własny zapisywalny katalog
wynikowy. Brak sieci, połączenia GitHub, globalnych poświadczeń i dostępu do
przestrzeni koordynatora oraz innych katalogów ocen musi wynikać z
egzekwowanych uprawnień/sandboxa, nie z samej prośby w instrukcji.
Test dostępu wykonuje się na syntetycznych plikach kontrolnych, bez oceny
publikacji: dozwolony odczyt i zapis, niedozwolony odczyt drugiego wyniku,
manifestu koordynatora i sieci. Rejestruje się egzekwowaną konfigurację i wyniki.

Nowa rozmowa ani współdzielony system plików nie potwierdzają izolacji.
Nieznany snapshot lub niepotwierdzone ograniczenie dostępu blokują start,
nawet jeżeli pakiet jest gotowy. To ograniczenia techniczne, nie wynik U1.
Możliwa znajomość publikacji z treningu modelu pozostaje ograniczeniem.

Kontrola przygotowawcza z 2026-10-19 nie potwierdziła dokładnego snapshotu
ani izolacji wszystkich kanałów narzędziowych. Próba utworzenia lokalnego
sandboxa na materiale syntetycznym zakończyła się odmową systemową; pełne
testy dostępu przyszłej instancji nie zostały wykonane. Istnienie narzędzia
sandboxa ani poprawne manifesty nie potwierdzają egzekwowania granic.
Zapisano oddzielnie warunki potwierdzone, niepotwierdzone i niewykonane testy.
Brak odpowiedniego środowiska nie zatrzymał pozostałego przygotowania.

## 11. Dokumentowanie przyszłego przebiegu

Przygotowuje się tylko wzory, rejestr zaplanowanych 12 uruchomień i puste
katalogi. Nie wpisuje się fikcyjnych dat rozpoczęcia/zakończenia ani pozornych
wyników. Kanoniczną `metryka.json` zgodną z wydaniem tworzy dana instancja
przed krytycznym przebiegiem, z rzeczywistym czasem, modelem, zakresem,
środowiskiem, SHA-256 i warunkami izolacji. Wzór nie jest gotową metryką oceny.

Instancja wykonuje pełny proces interpretacyjny i krytyczny według skilla
oraz tworzy `analiza.md`, `wynik.json`, `wyciag-kalibracyjny.json`,
dziennik techniczny i zapis walidacji. Nie zmienia metody.
Przed zamknięciem może naprawiać własną strukturę bez wglądu w inne wyniki.
Koordynator nie poprawia merytorycznej treści zamkniętej oceny.

Walidacja oficjalnym skryptem z katalogu rozpakowanego skilla:

```bash
python3 scripts/validate_0_3.py metric metryka.json
python3 scripts/validate_0_3.py result wynik.json --metric metryka.json
python3 scripts/validate_0_3.py extract wyciag-kalibracyjny.json --result wynik.json
```

Po zamknięciu wynik otrzymuje sumy i niezmienny zapis; czas zakończenia
oraz ujawnione ograniczenia uzupełnia się zgodnie ze standardem.

## 12. Ponowienia i odstępstwa

Dopuszcza się najwyżej jedno ponowienie danej oceny, wyłącznie z
udokumentowanej przyczyny technicznej: przerwania transmisji, uszkodzonych
bajtów, awarii narzędzia lub niekompletnego niewalidowalnego wykonania.
Zachowuje się nieudany przebieg, identyfikator, czas, przyczynę i decyzję.
Nowa instancja nie otrzymuje fragmentów poprzedniej analizy.

Zaskakujący werdykt, rozbieżność, brak oczekiwanego rodzaju przypadku
i niekorzystny wynik nie uzasadniają ponowienia. Błąd znaczeniowy
w poprawnym technicznie wyniku jest przedmiotem porównania, nie awarią.
Druga awaria lub wada wspólnego wejścia blokuje zamknięcie pełnej serii.
Odstępstw nie ukrywa się przez zmianę mianownika.

## 13. Porównanie sześciu par

Porównanie rozpoczyna się dopiero po zamknięciu wszystkich 12 ocen
i ich walidacji. Dla każdej pary powstają oficjalne Markdown i JSON.
Koordynator dopasowuje twierdzenia i problemy semantycznie, nie według numerów,
z relacjami 1:1, 1:wiele, wiele:1, wiele:wiele i jednostronnymi.
Każdy ID z A i B występuje dokładnie raz; relacje złożone mają wspólne
składowe i kategorie `exact`, `adjacent`, `different`, `not_comparable`
zgodnie ze standardem, bez nowej skali.

```bash
python3 scripts/validate_0_3.py comparison porownanie-pary.json --result-a A/wynik.json --result-b B/wynik.json
```

Raportuje się:

- zgodność werdyktu i bezpiecznego polecenia, licznik i mianownik 6 par;
- dokładną zgodność 72 pozycji A–L i zgodność w granicy jednego punktu;
- `nd`/`nd` jako zgodność, `nd`/liczba jako rozbieżność, nie różnicę jednego punktu;
- średnią bezwzględną różnicę i kierunek wyłącznie dla par liczbowych,
  z jawnym mianownikiem, oraz wyniki osobno według wymiaru;
- atomizację, pokrycie i wyniki twierdzeń, problemy, ich grupowanie,
  wielkość, centralność, ryzyko i pewność;
- profile kontekstu i grup, wiedzę konieczną/pomocną oraz grupowe H i L;
- stosowalność C/J, właściwy przedmiot uzasadnień, dowody historyczne,
  rozstrzygalność i każdą przesłankę krytyczności.

Rozdziela się poprawność techniczną (format, identyczne wejście, narzędzia,
izolacja), powtarzalność (zgodność A/B) i trafność (oparcie w dowodach).
Walidator nie ocenia prawdziwości; zgodność nie jest gwarancją trafności.
Sześć par nie uzasadnia progu statystycznego „metoda potwierdzona”.
Miary opisowe nie są średnią A–L wyznaczającą werdykt.

## 14. Pokrycie i zakończenie

Dla każdego celu zapisuje się po porównaniu: zaobserwowany w obu ocenach,
częściowo zaobserwowany, niezaobserwowany lub ograniczony materiałem/techniką.
Osobno notuje się powtarzalność i zgodność zastosowania reguły z dowodami.
Wypełnienie czterech przesłanek nie potwierdza zaobserwowania problemu
krytycznego; brak takiego problemu nie jest niepowodzeniem.

Badanie kończy się proceduralnie po 12 kompletnych zwalidowanych ocenach,
sześciu zwalidowanych porównaniach, kontroli sum i izolacji, rejestrze
odstępstw, macierzy pokrycia i bezpiecznym podsumowaniu.
Przy niewykonalności zapisuje się status niekompletny z rzeczywistymi
licznikami, bez udawania pełnej serii.

Nie dodaje się publikacji ani nie powtarza ocen, aby wymusić wynik.
Niezaobserwowane granice pozostają luką. Ewentualne najmniejsze rozszerzenie
(np. dwie publikacje i cztery oceny) wymaga osobnego uzasadnienia
i zatwierdzenia po U1, nie jest częścią obecnej zgody.

## 15. Pliki i bramki

Publiczne pliki przygotowania:

- `kalibracja/0.3/uzupelnienie-U1/protokol.md` — ten protokół;
- `kalibracja/0.3/uzupelnienie-U1/README.md` — status i nawigacja;
- `tests/test_u1_protocol.py` — kontrola kompletności i granic.

Prywatna przestrzeń koordynatora:

- `plan-wyszukiwania.json`, `dziennik-wyszukiwania.jsonl` i odpowiedzi w `search/`;
- osobny plan Q13–Q18, jego dziennik oraz `archival/`: plan tury archiwalnej,
  wykaz, odpowiedzi, kolejność kopii, historie plików i zakresy dowodów;
- `kandydaci.csv`, `kwalifikacja.csv`, `kontrola-kolizji.json`,
  `wczesniejsze-korpusy-identyfikacja.json`, `korpus.csv`, `wybor-korpusu.json`;
- `srodowisko.json`, `kontrola-izolacji.json`, `rejestr-przebiegow.csv`,
  `rejestr-odchylen.md`;
- `scripts/select_corpus.py`, `scripts/check_inputs.py`.

Neutralne wejście oceniających:

- `START-U1.md`, `manifest-wejscia.json`, `SHA256SUMS`;
- `input/assess-accessibility-articles-v0.3.0.zip` i rozpakowany `input/skill/`;
- `input/U1-01/`–`input/U1-06/`: `materialy.json`,
  `kontekst-miejsca.json`, `braki-materialow.json` oraz materiały M-001 itd.;
- `input/zrodla/`: wspólna biblioteka, rejestr wersji i praw;
- `templates/`: wzory metryk i dzienników, nie wyniki;
- puste katalogi `oceny/U1-01/A/`–`oceny/U1-06/B/`
  i `porownania/U1-01/`–`porownania/U1-06/`.

Dopiero po ocenach powstają cztery kanoniczne pliki każdej oceny,
dzienniki, walidacje i dwa pliki porównania każdej pary, prywatna macierz
pokrycia i podsumowanie. Publiczne `wyniki.md` może powstać dopiero po
zakończeniu i kontroli anonimowości; obecnie go nie tworzy się.

Przed startem muszą być spełnione wszystkie bramki:

1. korpus zatwierdzony osobno przez właściciela;
2. zgodne sumy, oficjalny ZIP i kompletne legalnie utrwalone wejście;
3. brak kolizji i wcześniejszych wyników w wejściu;
4. potwierdzony dokładny model, snapshot i jednakowe narzędzia;
5. egzekwowana i sprawdzona izolacja kontekstu, plików oraz sieci;
6. osobna zgoda na uruchomienie 12 ocen.

Przygotowanie nie jest zgodą na start. Nie scala się PR, nie zmienia master,
metodologii, skilla, wcześniejszych wyników, wydań, materiałów 0.4 ani laboratoriów B2.

## 16. Decyzje, nakład i ryzyka

| Decyzja/rekomendacja | Proste wyjaśnienie i korzyść | Ryzyko | Alternatywa wymagająca osobnej zgody |
| --- | --- | --- | --- |
| Sześć publikacji, 12 świeżych instancji | Mały zakres i brak uczenia się na poprzednim przypadku. | Słabe pokrycie rzadkich granic. | Uzasadnione małe rozszerzenie po wynikach. |
| Zamknięta pula i SHA-256 | Nie wybieramy tekstów pod werdykt. | Zależność od jednorazowych wyników wyszukiwarki. | Nowy wcześniej zatwierdzony plan wyszukiwania. |
| Maksimum trzech publikacji wydawcy, zatwierdzone przed wyborem | Umożliwia pełne przypisanie w potwierdzonej puli. | Tylko dwaj wydawcy, po trzy publikacje; ograniczona różnorodność redakcyjna. | Dalsza zmiana wymaga osobnej decyzji; obecnie nie poszerza się puli. |
| Zamrożone źródła, bez sieci | A i B mają takie same dowody. | Źródła mogą nie wystarczyć dla nieprzewidzianej tezy. | Ponowne przygotowanie i zatwierdzenie całego wejścia, nie cicha aktualizacja. |
| Udokumentowane prawa | Pełne wejście można legalnie zachować. | Mniej dostępnych kandydatów. | Uzyskanie zgody właściciela praw. |
| Twarda izolacja i znany snapshot | Brak dostępu do cudzych wyników i jawny model. | Obecne środowisko może nie spełnić warunków. | Osobne środowisko z egzekwowanym sandboxem, po zatwierdzeniu. |
| Bez progowego „zaliczenia” | Mała zgodność nie udaje dowodu trafności. | Nie uzyskamy prostej pieczęci jakości. | Większe badanie z niezależnym wzorcem, poza U1. |

Szacunek planistyczny, nie wykonane czasy: przygotowanie i prawa 1–3 dni
robocze; 12 ocen około 12–30 godzin pracy instancji; porównania i kontrola
6–12 godzin. Równoległość skraca czas kalendarzowy wyłącznie przy potwierdzonej
izolacji. Koszt zależy od rzeczywistego modelu, tokenów, limitów i planu
usługi; bez tych danych pozostaje `not_available`. Zgoda nie obejmuje
nieuzgodnionych płatnych usług.

Główne ryzyka: brak legalnych kopii, brak profilu historycznego w puli,
niepełna biblioteka, niedostępny snapshot, wspólny system plików, pamięć,
błąd obu ocen, nieporównywalne awarie i pośrednie ujawnienie nazw.
Każde ograniczenie zapisuje się; organizacyjna niewykonalność nie jest
wynikiem o jakości metodologii.

## Dokumenty odniesienia

- [Oficjalny standard 0.3](../../../metodologia/0.3/standard.md).
- [Kotwice](../../../metodologia/0.3/kotwice.md).
- [Szablony 0.3](../../../szablony/0.3/).
- [Instrukcja skilla](../../../skill/SKILL.md).
- [Informacje o wydaniu](../../../wydania/v0.3.0.md).
- [Historyczne podsumowanie B1](../wyniki-B1.md) — tylko dla koordynatora.
- [Status U1](README.md).
