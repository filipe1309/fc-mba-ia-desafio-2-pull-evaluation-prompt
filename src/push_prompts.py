"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        # Criar o template do prompt
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", prompt_data["system_prompt"]), ("user", prompt_data["user_prompt"])]
        )

        # Publicar no LangSmith Hub
        username = os.environ.get("USERNAME_LANGSMITH_HUB", "")
        repo_full_name = f"{username}/{prompt_name}" if username else prompt_name
        hub.push(
            repo_full_name,
            prompt_template,
            new_repo_is_public=True,
            new_repo_description=prompt_data.get("description", ""),
            tags=prompt_data.get("tags", []),
        )
        print(f"✅ Prompt '{prompt_name}' publicado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao publicar o prompt '{prompt_name}': {e}")
        return False



def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []
    if "system_prompt" not in prompt_data:
        errors.append("Falta 'system_prompt'")
    if "user_prompt" not in prompt_data:
        errors.append("Falta 'user_prompt'")
    return (len(errors) == 0, errors)


def main():
    """Função principal"""
    print_section_header("🚀 Iniciando o push de prompts otimizados para o LangSmith Hub")

    # Verificar variáveis de ambiente
    required_env_vars = ["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]
    if not check_env_vars(required_env_vars):
        print("❌ Variáveis de ambiente necessárias não estão definidas. Abortando.")
        return 1

    # Carregar prompt otimizado
    prompt_file = "prompts/bug_to_user_story_v2.yml"
    raw_data = load_yaml(prompt_file)
    if not raw_data:
        print(f"❌ Falha ao carregar o prompt otimizado de {prompt_file}. Abortando.")
        return 1

    # O YAML tem uma chave raiz com o nome do prompt; extrair o dict interno
    prompt_name_key = next(iter(raw_data))
    prompt_data = raw_data[prompt_name_key]

    # Validar prompt
    is_valid, validation_errors = validate_prompt(prompt_data)
    if not is_valid:
        print(f"❌ Prompt '{prompt_file}' falhou na validação:")
        for error in validation_errors:
            print(f"   - {error}")
        return 1

    # Fazer push do prompt para o LangSmith Hub
    prompt_name = prompt_name_key
    if not push_prompt_to_langsmith(prompt_name, prompt_data):
        print("❌ Falha ao publicar o prompt. Abortando.")
        return 1

    print("✅ Push de prompts concluído com sucesso!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
