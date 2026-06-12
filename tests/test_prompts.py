"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"
PROMPT_KEY = "bug_to_user_story_v2"


def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def prompt_data():
    """Carrega e retorna os dados do prompt v2."""
    data = load_prompts(str(PROMPT_FILE))
    assert PROMPT_KEY in data, f"Chave '{PROMPT_KEY}' não encontrada no YAML"
    return data[PROMPT_KEY]


class TestPrompts:
    def test_prompt_has_system_prompt(self, prompt_data):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert "system_prompt" in prompt_data, "Campo 'system_prompt' ausente no prompt"
        system_prompt = prompt_data["system_prompt"]
        assert system_prompt is not None, "system_prompt é None"
        assert system_prompt.strip() != "", "system_prompt está vazio"

    def test_prompt_has_role_definition(self, prompt_data):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        system_prompt = prompt_data.get("system_prompt", "")
        role_keywords = ["você é", "you are", "sua função", "seu papel", "como especialista"]
        found = any(kw in system_prompt.lower() for kw in role_keywords)
        assert found, (
            "system_prompt não define uma persona/role. "
            "Inclua uma frase como 'Você é um Product Manager...' no início."
        )

    def test_prompt_mentions_format(self, prompt_data):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        system_prompt = prompt_data.get("system_prompt", "")
        format_keywords = ["markdown", "user story", "como um", "critérios de aceitação", "dado que"]
        found = any(kw in system_prompt.lower() for kw in format_keywords)
        assert found, (
            "system_prompt não menciona o formato esperado (Markdown, User Story, Gherkin). "
            "Inclua instruções explícitas de formato."
        )

    def test_prompt_has_few_shot_examples(self, prompt_data):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        system_prompt = prompt_data.get("system_prompt", "")
        # Verifica presença de pelo menos um bloco de exemplo com Input e Output
        has_input = "input:" in system_prompt.lower()
        has_output = "output:" in system_prompt.lower()
        assert has_input and has_output, (
            "system_prompt não contém exemplos de Few-shot Learning. "
            "Adicione pelo menos um par Input/Output de exemplo."
        )

    def test_prompt_no_todos(self, prompt_data):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        all_text = " ".join(str(v) for v in prompt_data.values() if v is not None)
        assert "[TODO]" not in all_text, (
            "O prompt ainda contém marcadores '[TODO]'. Remova-os antes de publicar."
        )

    def test_minimum_techniques(self, prompt_data):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        # Suporta tanto o campo 'techniques' quanto 'techniques_applied'
        techniques = prompt_data.get("techniques") or prompt_data.get("techniques_applied") or []
        assert isinstance(techniques, list), (
            "O campo 'techniques' deve ser uma lista no YAML."
        )
        assert len(techniques) >= 2, (
            f"Mínimo de 2 técnicas requeridas, encontradas: {len(techniques)}. "
            "Adicione o campo 'techniques' nos metadados do YAML."
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])