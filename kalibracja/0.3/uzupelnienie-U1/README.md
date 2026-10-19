# U1 — badanie zakończone z udokumentowanymi odstępstwami

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

Następny krok dla 0.4: naprawić i sprawdzić odbiór oraz walidatory w osobnej
zmianie, następnie przygotować porównywalną serię sześciu przypadków po dwie
oceny innej rodziny AI, z jawnymi ustawieniami i zamrożonym wejściem.
To rekomendacja po U1; nie uruchomiono kolejnej serii.

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
