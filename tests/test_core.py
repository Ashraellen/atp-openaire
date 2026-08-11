import unittest

from src.research_context import build_research_context, normalize_product, render_context_markdown


class ResearchContextTests(unittest.TestCase):
    def test_normalize_product(self):
        raw = {
            "id": "open-test-id",
            "mainTitle": "A Test Paper",
            "publicationDate": "2026-01-01",
            "type": "publication",
            "authors": [{"fullName": "Ada Example"}],
            "pids": [{"scheme": "doi", "value": "10.0000/example"}],
            "bestAccessRight": {"label": "Open Access"},
            "citationCount": 0,
        }
        out = normalize_product(raw)
        self.assertEqual(out["title"], "A Test Paper")
        self.assertEqual(out["authors"], ["Ada Example"])
        self.assertEqual(out["citation_count"], 0)
        self.assertEqual(out["openaire_id"], "open-test-id")

    def test_context_and_markdown(self):
        response = {
            "header": {"numFound": 1, "queryTime": 7, "page": 1, "pageSize": 5},
            "results": [{"id": "x", "mainTitle": "One", "type": "publication"}],
        }
        context = build_research_context("test query", response)
        self.assertEqual(context["retrieval"]["returned"], 1)
        text = render_context_markdown(context)
        self.assertIn("test query", text)
        self.assertIn("OpenAIRE Graph", text)
        self.assertIn("One", text)


if __name__ == "__main__":
    unittest.main()
