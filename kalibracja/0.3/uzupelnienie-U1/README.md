# U1 — co pokazało sprawdzenie Probiernika i co poprawiamy

**Gdzie jesteśmy:** sprawdzenie obecnej wersji zostało zakończone. Teraz
wykorzystujemy wyniki do przygotowania konkretnych poprawek. Opublikowaną
wersją pozostaje 0.3.0. Nie wydano 0.3.1 ani 0.4 i nie rozpoczęto nowego badania.

## Co Probiernik już potrafi

Probiernik prowadzi AI przez przeczytanie publikacji, sprawdzenie twierdzeń
i źródeł oraz przygotowanie uzasadnionego wniosku. W zakończonym badaniu
powstało dwanaście pełnych ocen sześciu publikacji. Dwie osobne oceny każdej
publikacji prowadziły do podobnego końcowego wniosku. To pokazuje
powtarzalność w tych przypadkach; nie dowodzi, że wszystkie oceny są trafne.

## Gdzie nadal są problemy

- **Waga problemów:** AI różnie oceniały, czy poprawka zmienia ważną czynność
  czytelnika. Zachowanie tego samego celu nie zawsze oznacza ten sam sposób
  wykonania zadania.
- **Odbiorcy artykułu:** podobny wynik ogólny ukrywał inne założenia o tym,
  komu tekst ma pomóc. Początkujący czytelnik może również korzystać
  z czytnika ekranu; obie te cechy mogą mieć znaczenie.
- **Wymagane dowody:** potwierdzenie, że raport podaje liczbę, jest innym
  ustaleniem niż potwierdzenie poprawności samego pomiaru.
- **Ochrona przed błędem:** jeden agent potraktował dopiero proponowaną
  poprawkę jak zabezpieczenie już dostępne czytelnikowi. Zasady wymagają
  sprawdzenia tego, co rzeczywiście znajduje się w ocenianym artykule.
- **Program i organizacja pracy:** wykryto pomijaną kontrolę wyniku.
  Wcześniej zawiódł również sposób odbioru pierwszych ocen. To odrębne
  problemy od jakości zasad oceny artykułów.

## Co przygotowano po badaniu

20 października przeanalizowano wyniki w odniesieniu do dokładnych zasad,
których używali oceniający. Zapisano dziesięć decyzji i propozycji: dla każdej
podano dowód, co wymaga poprawy, proponowaną zmianę i sposób jej sprawdzenia.
Szczegóły odnoszące się do publikacji pozostają prywatne.

Przygotowana poprawka programu uruchamia pomijaną kontrolę. Przeszła
72 testy; sprawdzono też, że nadal przyjmuje dotychczasowe wyniki i porównania.
Poprawka znajduje się w osobnej kopii do przeglądu. Nie podmieniono
oficjalnego wydania ani wyników badania.

Pozostałe propozycje dotyczą lepszych przykładów i objaśnień dla AI oraz
rozstrzygnięcia dwóch granic: wykorzystania potrzeb użytkowników i zakresu
odtworzenia dawnej publikacji. Te zmiany nie zostały jeszcze wdrożone.

## Co robimy dalej i jak oznaczymy zmianę

Najpierw rozpatrujemy przygotowane poprawki i określamy ich zakres. Naprawa
programu lub objaśnienie zachowujące znaczenie zasad może wejść do 0.3.1.
Zmiana znaczenia kryteriów lub progów jest propozycją do 0.4. Żaden z tych
numerów nie oznacza obecnie nowego wydania.

Plan porównania różnych AI pozostaje osobnym zaplanowanym badaniem. Przed
jego rozpoczęciem trzeba określić dokładną wspólną wersję zasad i sprawdzić
odzyskiwanie wyników po przerwaniu pracy. Samo zakończenie U1 nie uruchamia
następnej serii.

U1 jest nazwą badania wersji 0.3.0. Oznaczenia U1-1.3 i U1-1.6 dotyczą
kolejnych opisów organizacji tego badania.

## Dokładny zapis zakończonego badania

**Stan: 2026-10-19. Ukończono 12 z 12 ocen i 6 z 6 porównań A/B.**
Właściciel zlecił pełną serię 2026-10-19 o 18:05:22 +02:00.
Zmianę warunków U1-1.4 zapisano przed ocenami, zmianę odbioru U1-1.5
przed ponowieniami, a zamknięcie dokumentuje U1-1.6.

Korpus zatwierdzony pozostaje bez zmian: sześć publikacji dwóch wydawców,
po trzy, z zachowaniem identyfikatorów, profili i kolejności.
Nie wykonano nowych wyszukiwań puli. Wszystkie materiały centralne są zachowane.
Dziewięć luk pomocniczych opisano jako ograniczenia; osiem nierozstrzygniętych
podstaw wykorzystania nie zostało uznanych za zakaz ani zgodę.

| Element | Stan końcowy |
| --- | --- |
| Kompletne odebrane oceny | 12 z 12; każda w osobnej nowej instancji R1. |
| Porównania A/B | 6 z 6; pełne dopasowania semantyczne. |
| Oficjalna walidacja | 36/36 kontroli ocen i 6/6 porównań. |
| Zgodność werdyktu i bezpiecznego polecenia | Po 6/6 par. |
| Dokładna zgodność A–L | 62/72 (86,1%), w tym 2 pozycje nd/nd. |
| Pozostałe różnice A–L | 9 różnic jednopunktowych i 1 nd/liczba. |
| Średnia różnica bezwzględna | 9/69 = 0,1304; wyłącznie 69 par liczbowych. |
| Pokrycie pytań protokołu | Macierz wszystkich 9 pytań, wraz z lukami. |
| PR #11 | Roboczy; bez scalenia. |

Pierwsze 12 instancji zgłosiło zamknięcie, ale pełne pakiety utracono
przy odbiorze. Zachowano potwierdzenia i opis awarii; nie rekonstruowano
ocen. Wykonano po jednym dopuszczonym ponowieniu technicznym R1.
Łącznie uruchomiono 24 instancje oceniające; próba obejmuje 12 użytecznych
ocen, nie 24. Wyniki R1 odebrano w całości, sprawdzono 72 sumy artefaktów
i zapisano dopiero po zakończeniu wszystkich dwunastu ocen. Nie poprawiano
ocen w celu zwiększenia zgodności.

Agenci zaczynali bez historii koordynatora (`fork_turns="none"`),
z dziedziczoną konfiguracją, bez nadpisania modelu. Nie otrzymywali wyników
innych ocen ani dokumentacji doboru. Rozdzielenie kontekstów i wyników
nie jest techniczną blokadą dostępu do wspólnych plików. Dokładny model,
snapshot i nieujawnione parametry: `not_available`; identyczność dokładnego
snapshotu wszystkich ocen nie jest potwierdzona. Kanoniczne manifestowane
bajty wejścia pozostały niezmienione. Dwie dodatkowe częściowe kopie mediów
zachowano jako odstępstwo inwentarza, a nie nowe źródła.

Zgodne werdykty ukrywają różnice w stosowalności J, wielkości problemów,
profilach odbiorców i progu potwierdzania twierdzeń. Nie zaobserwowano
werdyktu `rzetelny`, dodatniego przypadku krytyczności ani braku rdzenia.
To luki pokrycia, nie dowód nieprawidłowego działania tych reguł.
Sześć par od dwóch wydawców, bez niezależnego wzorca prawdziwości,
pozwala opisać powtarzalność; zgodność nie potwierdza trafności.

W oficjalnym walidatorze ujawniono niewykonywaną kontrolę minimum L.
Osobny audyt wyników stwierdził 0/12 naruszeń tej relacji. Odnotowano także
rozbieżność kontraktu URI i HTTP(S), formalne korekty metryk, ograniczenia
analizy mediów i niepełny dowód kolejności ustalenia jednego profilu odbiorcy.
Pełny rejestr odstępstw i szczegółowe wyniki pozostają prywatne.

Rekomendację kolejnego kroku z 19 października skorygowano 20 października:
najpierw trzeba przełożyć wyniki U1 na konkretne poprawki, oddzielić zmianę
zasad od naprawy programu i określić ich wpływ na zapisany plan dalszych badań.
To przegląd przygotowanych zmian; nie uruchomiono kolejnej serii.
Nie podmieniono planu B2 nowym badaniem U1.

Badanie nie zmienia metodologii ani skilla, nie rozpoczyna B2 i nie modyfikuje
wcześniejszych wyników, wydań, materiałów 0.4 ani laboratoriów B2. Zmiany
publiczne obejmują te same trzy pliki. Kopie publikacji, metryki, pełne wyniki,
manifesty i dokumentacja doboru pozostają prywatne. Zbiorczego checkpointu
nie przekazuje się oceniającym.

Poprzedni status i warunki U1-1.3 zachowano w historii Git w commicie
`f225f31d47f0261674e0cef377b9c51f497128d7`; warunki U1-1.4 w
`bef9ad1d1a9754300b54dd59118097f3f2442348`, a U1-1.5 w
`945be63f080c85f2004bd85b9cf3e1bcf47966c1`.

- [Protokół U1-1.6 i historia zmian warunków](protokol.md).
- [Oficjalne wydanie v0.3.0](../../../wydania/v0.3.0.md).
- [Standard 0.3](../../../metodologia/0.3/standard.md).

