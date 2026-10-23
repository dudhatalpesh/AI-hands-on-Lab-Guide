import unittest
from unittest.mock import patch
from src.advisor.core import (
    Model, agent, bounded_text, execute_tool, extract_request, rag, research, retrieve,
)
from scripts.run_lab import run


class CoreTests(unittest.TestCase):
    def test_all_labs_execute_offline(self):
        for lab in range(1, 12):
            with self.subTest(lab=lab):
                self.assertIsInstance(run(lab, Model(True), "MFA access"), dict)

    def test_tenant_filter_precedes_embedding(self):
        model = Model(True)
        with patch.object(model, "embed", wraps=model.embed) as embed:
            docs = retrieve("Contoso secret", "northstar", model)
            corpus = embed.call_args_list[0].args[0]
        self.assertTrue(all(d["tenant"] == "northstar" for d in docs))
        self.assertNotIn("ORCHID-TEST-ONLY", " ".join(corpus))

    def test_unknown_tenant_never_calls_model(self):
        model = Model(True)
        result = rag("MFA", "unknown", model)
        self.assertEqual(result["sources"], [])
        self.assertEqual(model.calls, 0)

    def test_tool_rejects_extra_authority_and_arguments(self):
        for proposal in [
            {"tool": "shell", "args": {}},
            {"tool": "policy_lookup", "args": {"topic": "access", "tenant": "contoso"}},
            {"tool": "policy_lookup", "args": {"topic": "../secret"}},
            {"tool": "policy_lookup", "args": {"topic": []}},
            [],
        ]:
            with self.subTest(proposal=proposal), self.assertRaises(ValueError):
                execute_tool(proposal, "northstar")

    def test_tool_does_not_cross_tenant(self):
        result = execute_tool(
            {"tool": "policy_lookup", "args": {"topic": "access"}}, "contoso"
        )
        self.assertEqual(result["documents"], [])

    def test_extraction_rejects_unsubstantiated_values(self):
        with self.assertRaises(ValueError):
            extract_request(Model(True), "No request or numeric data.")

    def test_extraction_rejects_boolean_quantity(self):
        model = Model(True)
        with patch.object(model, "generate", return_value=
                          '{"request_id":"REQ-104","quantity":true,"budget_usd":9600}'):
            with self.assertRaises(ValueError):
                extract_request(model, "REQ-104 12 9600")

    def test_agent_call_budget(self):
        model = Model(True)
        agent("MFA", model)
        self.assertEqual(model.calls, 2)

    def test_review_has_explicit_handoff(self):
        result = research("MFA", Model(True))
        self.assertIn("draft", result)
        self.assertIn("review", result)

    def test_input_boundaries(self):
        for value in ["", "x" * 6001, None]:
            with self.assertRaises(ValueError):
                bounded_text(value)


if __name__ == "__main__":
    unittest.main()
