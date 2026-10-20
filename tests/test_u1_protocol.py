"""Check U1 documentation, closure accounting and preserved boundaries."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
U1 = ROOT / "kalibracja/0.3/uzupelnienie-U1"


class U1ProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = (U1 / "protokol.md").read_text(encoding="utf-8")
        cls.readme = (U1 / "README.md").read_text(encoding="utf-8")

    def test_protocol_sections_are_complete(self):
        numbered = re.findall(r"^## (\d+)\.", self.protocol, re.M)
        self.assertEqual([str(i) for i in range(1, 17)], numbered)

    def test_frozen_release_and_historical_boundary(self):
        for text in (
            "38babd2231c6ea2af786913c7c6040423b27a88d",
            "853404df15f05ba769d2440644a14fd0c77ec2e3",
            "72b2604d3a9e4581241570c4ca89726e5a8dd7a8e3fd6addafb3a4596b9a6979",
            "v0.3.0", "T2 i S11–S15", "0.3-draft",
            "nie traktuje się jako bezpośredniego potwierdzenia",
        ):
            self.assertIn(text, self.protocol)
        self.assertIn("nie zmienia metodologii ani skilla", self.readme)

    def test_design_and_launch_are_separate(self):
        for text in ("łącznie 12 ocen", "ChatGPT", "bez ludzi jako oceniających", "ocenia tylko jedną publikację"):
            self.assertIn(text, self.protocol)
        self.assertIn("18:05:22 +02:00", self.protocol)
        self.assertIn("18:05:22 +02:00", self.readme)
        self.assertIn("nie rozpoczyna B2", self.readme)
        self.assertIn("Nie scala się PR", self.protocol)

    def test_search_is_bounded_and_selection_is_deterministic(self):
        for text in ("dokładnie 12 zapytań", "pierwszych 10 różnych adresów",
                     "co najmniej dwóch zakwalifikowanych kandydatów",
                     "probiernik-U1-korpus-v1|<profil>|<kanoniczny_URL>",
                     "leksykograficznie najmniejszą", "najwyżej trzy",
                     "Nie rozszerza się automatycznie wyszukiwania",
                     "nie podmienia się publikacji", "Nie ma automatycznej rezerwy"):
            self.assertIn(text, self.protocol)
        for profile in range(1, 7):
            self.assertEqual(2, len(re.findall(rf"^\| P{profile} \|", self.protocol, re.M)))

    def test_collision_and_rights_gates(self):
        for text in ("P01–P05", "wszystkimi", "rezerwami", "korpus B2",
                     "blokuje wybór", "Nie wykorzystuje się dawnych wyników",
                     "Prywatność ani publiczny dostęp", "Bez takiej podstawy"):
            self.assertIn(text, self.protocol)

    def test_approved_supplement_preserves_previous_search(self):
        for query in range(13, 19):
            self.assertIn(f"| Q{query} |", self.protocol)
        for text in ("18 wykonanych zapytań", "148 różnych adresów",
                     "nie wykonuje się ponownie zachowanych zapytań",
                     "Nie jest to liczba zakwalifikowanych publikacji"):
            self.assertIn(text, self.protocol)

    def test_archival_acquisition_limits_and_order_are_explicit(self):
        for text in ("sekcja „Resources” polskiej części", "najwyżej 20 publikacji",
                     "Więcej niż 20 adresów blokuje turę", "od najstarszej daty",
                     "najwyżej 10 różnych zachowanych kopii",
                     "najwyżej 20 ostatnich zapisów", "10 różnych wersji treści",
                     "innych wykazów wydawców", "z pełnym pochodzeniem"):
            self.assertIn(text, self.protocol)

    def test_historical_evidence_does_not_infer_deployment_or_quality(self):
        for text in ("Historia angielskiego oryginału nie zastępuje historii",
                     "Zapis redakcyjny w Git nie dowodzi publikacji na stronie",
                     "Bieżąca kopia i jej SHA-256 nie dowodzą treści historycznej",
                     "nie musi różnić się znaczeniowo",
                     "nie jest oceną ich poprawności", "dokładny adres zapisu",
                     "Niedostępny", "nie zawiera żadnego zapisu"):
            self.assertIn(text, self.protocol)

    def test_execution_amendment_is_explicit(self):
        for text in ("U1-1.4", 'fork_turns="none"', "not_available", "Nie jest równoważne izolacji systemowej", "przed pierwszą oceną", "wszystkich 12 ocen", "nie zapisuje się we wspólnych plikach"):
            self.assertIn(text, self.protocol)
        for text in ("12 z 12", "6 z 6", "Korpus zatwierdzony", "bez zmian", "nie jest techniczną blokadą"):
            self.assertIn(text, self.readme)

    def test_final_qualification_does_not_add_candidates(self):
        for text in ("zachowaną pulę 164 adresów", "bez nowych wyszukiwań ani kandydatów",
                     "Wcześniejszych planów, odpowiedzi i decyzji nie nadpisuje się"):
            self.assertIn(text, self.protocol)

    def test_technical_reception_failure_and_retry_are_explicit(self):
        for text in ("U1-1.5", "nie zastępują kompletnych ocen", "po jednym ponowieniu technicznym",
                     "próby R1", "nie utrwala wyników w zwykłych plikach", "Nie rekonstruuje się ocen",
                     "niezmanifestowane częściowe kopie mediów"):
            self.assertIn(text, self.protocol)
        for text in ("pełne pakiety utracono", "24 instancje oceniające",
                     "12 użytecznych", "nie rekonstruowano", "R1"):
            self.assertIn(text, self.readme)

    def test_closure_accounts_for_nd_and_numeric_denominators(self):
        for content in (self.protocol, self.readme):
            for text in ("U1-1.6", "36/36", "6/6", "62/72",
                         "9 różnic jednopunktowych i 1 nd/liczba", "9/69 = 0,1304"):
                self.assertIn(text, content)
        self.assertIn("w tym 2 nd/nd", self.protocol)
        self.assertIn("w tym 2 pozycje nd/nd", self.readme)
        self.assertIn("wyłącznie 69 par liczbowych", self.readme)

    def test_closure_exposes_validation_and_coverage_limits(self):
        for content in (self.protocol, self.readme):
            for text in ("0/12 naruszeń", "profilu", "snapshot", "prywatne"):
                self.assertIn(text, content)
        for text in ("braku rdzenia", "krytyczności", "rzetelny",
                     "zgodność nie potwierdza trafności", "nie uruchomiono kolejnej serii"):
            self.assertIn(text, self.readme)

    def test_statutory_rights_are_checked_and_not_guessed(self):
        for text in ("Brak jawnej licencji nie oznacza zakazu wykorzystania",
                     "uprawnienie", "ustawowe", "aktualnych źródłach urzędowych",
                     "Podstawa dotycząca załącznika nie obejmuje", "nierozstrzygnięty",
                     "Nie kontaktuje się z autorami bez osobnej zgody"):
            self.assertIn(text, self.protocol)

    def test_approved_cap_and_closed_pool_preserve_other_criteria(self):
        for text in ("U1-1.3", "przed wyborem", "z dwóch do trzech",
                     "Pozostałe kryteria pozostają bez zmian", "25 potwierdzonych",
                     "102 wpisów", "Pozostałe 37", "nie uznano ich za zakazane",
                     "10 206", "798", "różnorodność redakcyjną"):
            self.assertIn(text, self.protocol)
        selection = self.protocol.split("## 7. Deterministyczny wybór")[1].split("## 8.")[0]
        self.assertIn("najwyżej trzy", selection)
        self.assertNotIn("najwyżej dwie", selection)
        self.assertIn("Nie wykonano nowych wyszukiwań puli", self.readme)

    def test_runtime_evidence_does_not_claim_success(self):
        for text in ("nie potwierdziła dokładnego snapshotu", "odmową systemową",
                     "testy dostępu przyszłej instancji nie zostały wykonane",
                     "warunki potwierdzone, niepotwierdzone"):
            self.assertIn(text, self.protocol)

    def test_corpus_and_execution_decisions_preserved(self):
        self.assertIn("16:36:25 +02:00", self.protocol)
        self.assertIn("Zatwierdzenie korpusu nie jest zgodą na rozpoczęcie ocen", self.protocol)
        self.assertIn("18:05:22 +02:00", self.protocol)
        for text in (self.protocol, self.readme):
            self.assertIn("f225f31d47f0261674e0cef377b9c51f497128d7", text)
        self.assertIn("Wybór, profile i kolejność pozostają bez zmian", self.protocol)

    def test_scoped_resolution_and_prototype_are_not_full_readiness(self):
        for text in ("12 otwartych pozycji", "Trzy zamknięto", "Osiem kwestii",
                     "jedna kwestia pozyskania", "Pełne zamrożenie wejścia nadal",
                     "nie rzeczywistą izolację", "nie jest\ntestem sieci sandboxa",
                     "Alternatywę API opisano prywatnie, lecz jej nie przyjęto"):
            self.assertIn(text, self.protocol)

    def test_aggregate_checkpoint_is_not_single_assessor_input(self):
        for text in ("Zbiorczy checkpoint", "nie przekazuje się ich oceniającym",
                     "wyłącznie własnego przypadku", "identyczną część wspólną"):
            self.assertIn(text, self.protocol)

    def test_isolation_limitations_are_not_hidden(self):
        amendment=self.protocol.split("## 1.")[0]
        for text in ("Rozdzielenie kontekstów", "nieudostępnianie wyników", "Nie jest równoważne izolacji systemowej", "technicznie dostępne", "not_available", "bez nadpisania modelu"):
            self.assertIn(text, amendment)
        self.assertIn("egzekwowanych uprawnień/sandboxa", self.protocol)
        self.assertIn("historyczne opisy bramek", amendment)

    def test_inputs_are_frozen_without_fabricated_outputs(self):
        for text in ("Nie wpisuje się fikcyjnych dat", "metryka.json",
                     "SHA256SUMS", "puste katalogi", "otwartego internetu podczas ocen",
                     "Brak źródła w pakiecie nie", "nie dopisuje się źródeł"):
            self.assertIn(text, self.protocol)
        self.assertFalse((U1 / "wyniki.md").exists())
        self.assertEqual({"README.md", "protokol.md"},
                         {p.name for p in U1.iterdir() if p.is_file()})

    def test_validation_comparison_and_coverage_are_present(self):
        for text in ("validate_0_3.py metric", "validate_0_3.py result",
                     "validate_0_3.py extract", "validate_0_3.py comparison",
                     "72 pozycji A–L", "wyłącznie dla par liczbowych",
                     "najwyżej jedno ponowienie", "Zaskakujący werdykt",
                     "powtarzalność", "trafność", "niezaobserwowany",
                     "Nie dodaje się publikacji", "status niekompletny"):
            self.assertIn(text, self.protocol)

    def test_post_study_decisions_preserve_release_and_study_boundaries(self):
        for text in ("Nie wydano 0.3.1 ani 0.4", "Co Probiernik już potrafi",
                     "Gdzie nadal są problemy", "Co przygotowano po badaniu",
                     "zmiany nie zostały jeszcze wdrożone",
                     "Nie podmieniono planu B2", "nie uruchamia"):
            self.assertIn(text, self.readme)
        for text in ("20 października 2026", "nie zmiana jego warunków",
                     "72 testy", "42 kontrole", "Nie rozpoczęto nowego badania"):
            self.assertIn(text, self.protocol)

    def test_public_documents_contain_no_corpus_urls(self):
        for path in (U1 / "README.md", U1 / "protokol.md"):
            content = path.read_text(encoding="utf-8")
            self.assertNotRegex(content, r"https?://")
            self.assertNotRegex(content, r"\bP0[1-5]\s*\|")

    def test_relative_links_and_heading_hierarchy(self):
        for path in (U1 / "README.md", U1 / "protokol.md"):
            content = path.read_text(encoding="utf-8")
            headings = re.findall(r"^(#+) ", content, re.M)
            self.assertEqual(1, len(headings[0]))
            self.assertEqual(1, headings.count("#"))
            self.assertTrue(all(len(h) <= 2 for h in headings))
            for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
                if "://" not in link:
                    self.assertTrue((path.parent / link.split("#")[0]).exists(), link)


if __name__ == "__main__":
    unittest.main()

