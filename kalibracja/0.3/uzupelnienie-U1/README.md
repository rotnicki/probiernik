# U1 — badanie w toku

**Stan: 2026-10-19.** Właściciel zlecił pełną serię: sześć zatwierdzonych
publikacji, po dwie oceny, łącznie 12 nowych agentów Work. Start zlecono
2026-10-19 o 18:05:22 +02:00. Zmianę warunków U1-1.4 zapisano przed ocenami.

Repozytorium i archiwum są zgodne z zapisanym stanem. Korpus zatwierdzony,
wybrany deterministycznie, pozostaje bez zmian: dwaj wydawcy po trzy
publikacje. Nie wykonano nowych wyszukiwań puli. Wszystkie materiały centralne
są zachowane. Dziewięć otwartych pozycji pomocniczych zachowano jako jawne
ograniczenia; osiem kwestii praw nie zostało uznanych za zakaz ani zgodę.

Agenci zaczynają bez historii koordynatora (`fork_turns="none"`) i dziedziczą
jednakową konfigurację. Nie otrzymują wcześniejszych ocen, dokumentacji doboru
ani wyników innych agentów. Organizacyjne rozdzielenie kontekstów i wyników
nie jest techniczną blokadą dostępu do wspólnych plików. Dokładny snapshot:
`not_available`; identyczność snapshotu wszystkich ocen nie jest potwierdzona.

| Element | Stan |
| --- | --- |
| Zatwierdzone publikacje | 6; identyfikatory, profile i kolejność bez zmian. |
| Kompletne odebrane oceny | 0 z 12; pierwszych 12 zamknięć nie dało odzyskiwalnych pakietów. |
| Porównania A/B | 0 z 6. |
| Walidacja wyników | Zgłoszona przez 12 instancji; koordynator nie może potwierdzić jej bez pełnych wyników. |
| PR #11 | Roboczy; bez scalenia. |

Utratę wyników i zmianę odbioru zapisano w U1-1.5. Przewidziane w protokole
pojedyncze ponowienia techniczne użyją tego samego zamrożonego wejścia.
Nie odtwarza się ocen z podsumowań; seria pozostaje niekompletna.

Badanie nie zmienia metodologii ani skilla, nie rozpoczyna B2 i nie modyfikuje
wcześniejszych wyników, wydań, materiałów 0.4 ani laboratoriów B2. Zmiany
publiczne obejmują te same trzy pliki. Kopie publikacji, metryki, pełne wyniki,
manifesty i dokumentacja doboru pozostają prywatne. Zbiorczego checkpointu
nie przekazuje się oceniającym.

Poprzedni status i warunki U1-1.3 zachowano w historii Git w commicie
`f225f31d47f0261674e0cef377b9c51f497128d7`.

- [Protokół U1-1.5 i historia zmian warunków](protokol.md).
- [Oficjalne wydanie v0.3.0](../../../wydania/v0.3.0.md).
- [Standard 0.3](../../../metodologia/0.3/standard.md).
