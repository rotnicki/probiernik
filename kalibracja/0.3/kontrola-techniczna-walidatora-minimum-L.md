# Kontrola techniczna poprawki walidatora: minimum L

**Data:** 13 listopada 2026 r.
**Zakres:** `skill/scripts/validate_0_3.py` i `tests/test_validate_0_3.py`
**Status:** poprawka techniczna; bez zmiany znaczenia metodologii ani kryteriów
**Wykonanie:** Grok Bot (Badacz) na polecenie Mikołaja Rotnickiego
**Podstawa:** master `38babd2231c6ea2af786913c7c6040423b27a88d`
**Wynik:** kontrola zakończona powodzeniem

## Błąd

Walidator 0.3 nie sprawdzał, czy ogólna ocena L równa się najniższej ocenie L
istotnych grup odbiorców objętych obietnicą artykułu
(`lowest_significant_group_l_score`). Reguła ta wynika ze standardu 0.3 (§6.5)
i jest zapisana w walidatorze, ale nigdy nie była wykonywana.

Wynik z ogólną oceną L = 4 przy minimum L grup równym 3 przechodził kontrolę
z komunikatem „OK”. Analogiczna kontrola dla H działała poprawnie.

## Przyczyna

Dwie linijki kontroli znajdowały się na samym końcu pliku, po instrukcji
`raise SystemExit(main())`. Program kończył działanie przed dojściem do nich,
więc był to martwy kod. Python nie zgłaszał przy tym żadnego błędu.

Błąd ujawniono podczas badania U1 (gałąź
`research/u1-przygotowanie-2026-10-19`, robocze zgłoszenie nr 11). Kandydacka
poprawka opisana w protokole U1 nie została wtedy wprowadzona do gałęzi głównej.

## Poprawka

- kontrolę przeniesiono do funkcji `validate_language_caps`, bezpośrednio za
  analogiczną kontrolę minimum H;
- usunięto martwe linijki po `raise SystemExit(main())`;
- dodano test regresyjny `test_result_l_must_equal_lowest_group_l_score`.
  Test ustawia ogólne L = 4 przy minimum L grup równym 3 i wymaga błędu
  `scores.L: musi równać się minimum L istotnych grup objętych obietnicą`.

Treść komunikatu i sama reguła są takie same jak w dotychczasowym, niewykonywanym
kodzie. Nie zmieniono standardu, kotwic, schematów ani szablonów.

## Kontrole wykonane po zmianie

| Kontrola | Wynik |
| --- | --- |
| Wszystkie testy regresyjne | 96/96 zaliczonych |
| Nowy test na kodzie sprzed poprawki | niezaliczony (błąd nie był zgłaszany) |
| Nowy test po poprawce | zaliczony |
| Przypadek L = 4 przy minimum L grup = 3 | przed: „OK”; po: błąd `scores.L` |
| Kompilacja walidatora | poprawna |
| `git diff --check` | bez błędów |

## Wpływ na wyniki

Nie są znane wyniki, których dotyczyłby ten błąd:

- audyt U1 stwierdził 0 naruszeń tej relacji w 12 wynikach;
- dwa przebiegi A/B oceny artykułu „Dostępnik o zaufaniu do AI I” (26 października
  2026 r.) przechodzą walidację zarówno przed poprawką, jak i po niej.

Zgodnie z zasadą z [WERSJONOWANIE.md](../../WERSJONOWANIE.md) wyników
wcześniejszych badań nie przelicza się wstecz.

## Zachowane granice

- zamrożone wydanie `v0.3.0` i jego paczka ZIP pozostają bez zmian; poprawka
  dotyczy wyłącznie gałęzi głównej projektu;
- według [WERSJONOWANIE.md](../../WERSJONOWANIE.md) jest to zmiana rodzaju
  `PATCH` (poprawka techniczna, która nie zmienia znaczenia kryteriów ani
  wyników); nie utworzono jednak znacznika ani wydania `v0.3.1` — decyzja
  wydawnicza pozostaje osobna;
- wersje 0.1 i 0.2 oraz gałąź badania U1 pozostały niezmienione.
