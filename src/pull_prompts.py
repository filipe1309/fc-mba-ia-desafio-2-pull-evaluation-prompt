"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

PROMPTS_TO_PULL = [
    {
        "repo": "leonanluppi/bug_to_user_story_v1",
        "output_file": "prompts/bug_to_user_story_v1.yml",
        "key": "bug_to_user_story_v1",
    },
]


def pull_prompts_from_langsmith() -> int:
    """
    Faz pull dos prompts do LangSmith Hub e salva localmente em YAML.

    Returns:
        0 em sucesso, 1 em falha
    """
    print_section_header("📥 Pull de prompts do LangSmith Hub")

    required_env_vars = ["LANGSMITH_API_KEY"]
    if not check_env_vars(required_env_vars):
        return 1

    success_count = 0

    for entry in PROMPTS_TO_PULL:
        repo = entry["repo"]
        output_file = entry["output_file"]
        key = entry["key"]

        print(f"Fazendo pull de: {repo}")
        try:
            prompt = hub.pull(repo)
        except Exception as e:
            print(f"❌ Erro ao fazer pull de '{repo}': {e}")
            continue

        # Extrair system e user message dos templates
        messages = prompt.messages
        system_prompt = ""
        user_prompt = ""

        for msg in messages:
            role = msg.__class__.__name__.lower()
            # Extrair texto do template (pode ser StringPromptTemplate ou lista)
            if hasattr(msg, "prompt"):
                text = msg.prompt.template
            elif hasattr(msg, "template"):
                text = msg.template
            else:
                text = str(msg)

            if "system" in role:
                system_prompt = text
            else:
                user_prompt = text

        prompt_data = {
            key: {
                "description": f"Prompt obtido via pull de {repo}",
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "version": "v1",
                "tags": ["bug-analysis", "user-story", "product-management"],
            }
        }

        if save_yaml(prompt_data, output_file):
            print(f"✅ Prompt salvo em: {output_file}")
            success_count += 1
        else:
            print(f"❌ Falha ao salvar '{output_file}'")

    print(f"\n{success_count}/{len(PROMPTS_TO_PULL)} prompt(s) salvos com sucesso.")
    return 0 if success_count == len(PROMPTS_TO_PULL) else 1


def main() -> int:
    """Função principal"""
    return pull_prompts_from_langsmith()


if __name__ == "__main__":
    sys.exit(main())
