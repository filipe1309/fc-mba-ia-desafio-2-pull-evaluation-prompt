Tentativa 0:
```sh
make evaluate                                                                                                                                                                               ─╯

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: openai
Modelo Principal: gpt-4o-mini
Modelo de Avaliação: gpt-4o

Criando dataset de avaliação: -eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset '-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: filipe1309/bug_to_user_story_v1
   Puxando prompt do LangSmith Hub: filipe1309/bug_to_user_story_v1
   ✓ Prompt carregado com sucesso
   Dataset: 15 exemplos
   Avaliando exemplos...
      [1/15] F1:0.75 Clarity:0.90 Precision:0.90
      [2/15] F1:0.75 Clarity:0.90 Precision:0.90
      [3/15] F1:0.75 Clarity:0.90 Precision:0.90
      [4/15] F1:0.58 Clarity:0.85 Precision:0.90
      [5/15] F1:0.69 Clarity:0.90 Precision:0.83
      [6/15] F1:0.80 Clarity:0.90 Precision:0.93
      [7/15] F1:0.85 Clarity:0.90 Precision:1.00
      [8/15] F1:0.75 Clarity:0.90 Precision:0.90
      [9/15] F1:0.80 Clarity:0.90 Precision:0.90
      [10/15] F1:0.67 Clarity:0.80 Precision:0.67
      [11/15] F1:0.80 Clarity:0.85 Precision:0.90
      [12/15] F1:0.67 Clarity:0.90 Precision:0.90
      [13/15] F1:0.69 Clarity:0.75 Precision:0.67
      [14/15] F1:0.80 Clarity:0.90 Precision:0.90
      [15/15] F1:0.69 Clarity:0.75 Precision:0.67

==================================================
Prompt: filipe1309/bug_to_user_story_v1
==================================================

Métricas Derivadas:
  - Helpfulness: 0.86 ✓
  - Correctness: 0.80 ✗

Métricas Base:
  - F1-Score: 0.73 ✗
  - Clarity: 0.87 ✓
  - Precision: 0.86 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8233
--------------------------------------------------

❌ STATUS: REPROVADO
⚠️  Métricas abaixo de 0.8: correctness, f1_score
⚠️  Média atual: 0.8233 | Necessário: 0.8000

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 0
Reprovados: 1

⚠️  Alguns prompts não atingiram todas as métricas >= 0.8
```


Tentativa 1:

```sh
==================================================
Prompt: filipe1309/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.71 ✗
  - Correctness: 0.68 ✗

Métricas Base:
  - F1-Score: 0.64 ✗
  - Clarity: 0.70 ✗
  - Precision: 0.72 ✗

--------------------------------------------------
📊 MÉDIA GERAL: 0.6904
--------------------------------------------------

❌ STATUS: REPROVADO
⚠️  Métricas abaixo de 0.8: helpfulness, correctness, f1_score, clarity, precision
⚠️  Média atual: 0.6904 | Necessário: 0.8000

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 0
Reprovados: 1

⚠️  Alguns prompts não atingiram todas as métricas >= 0.8
```

Tentativa 2:
```sh
make evaluate                                                                                                                                  ─╯

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: openai
Modelo Principal: gpt-4o-mini
Modelo de Avaliação: gpt-4o

Criando dataset de avaliação: -eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset '-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: filipe1309/bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: filipe1309/bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
   Dataset: 15 exemplos
   Avaliando exemplos...
      [1/15] F1:0.75 Clarity:0.80 Precision:0.80
      [2/15] F1:0.65 Clarity:0.70 Precision:0.70
      [3/15] F1:0.75 Clarity:0.80 Precision:0.80
      [4/15] F1:0.69 Clarity:0.85 Precision:0.90
      [5/15] F1:0.58 Clarity:0.85 Precision:0.83
      [6/15] F1:0.69 Clarity:0.85 Precision:0.83
      [7/15] F1:0.90 Clarity:0.85 Precision:1.00
      [8/15] F1:0.58 Clarity:0.85 Precision:0.80
      [9/15] F1:1.00 Clarity:1.00 Precision:1.00
      [10/15] F1:0.80 Clarity:0.80 Precision:0.83
      [11/15] F1:0.80 Clarity:0.80 Precision:0.83
      [12/15] F1:0.85 Clarity:0.80 Precision:0.90
      [13/15] F1:0.80 Clarity:0.85 Precision:0.90
      [14/15] F1:1.00 Clarity:1.00 Precision:1.00
      [15/15] F1:0.95 Clarity:0.90 Precision:0.67

==================================================
Prompt: filipe1309/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.85 ✓
  - Correctness: 0.82 ✓

Métricas Base:
  - F1-Score: 0.78 ✗
  - Clarity: 0.85 ✓
  - Precision: 0.85 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8305
--------------------------------------------------

❌ STATUS: REPROVADO
⚠️  Métricas abaixo de 0.8: f1_score
⚠️  Média atual: 0.8305 | Necessário: 0.8000

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 0
Reprovados: 1

⚠️  Alguns prompts não atingiram todas as métricas >= 0.8
```

Tentativa 3:
```sh
make evaluate                                                                                                                                  ─╯

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: openai
Modelo Principal: gpt-4o-mini
Modelo de Avaliação: gpt-4o

Criando dataset de avaliação: -eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset '-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: filipe1309/bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: filipe1309/bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
   Dataset: 15 exemplos
   Avaliando exemplos...
      [1/15] F1:0.85 Clarity:0.75 Precision:0.80
      [2/15] F1:0.75 Clarity:0.70 Precision:0.90
      [3/15] F1:0.87 Clarity:0.75 Precision:0.80
      [4/15] F1:0.69 Clarity:0.85 Precision:0.83
      [5/15] F1:0.58 Clarity:0.85 Precision:0.67
      [6/15] F1:0.75 Clarity:0.85 Precision:0.90
      [7/15] F1:0.90 Clarity:0.90 Precision:1.00
      [8/15] F1:1.00 Clarity:1.00 Precision:1.00
      [9/15] F1:1.00 Clarity:1.00 Precision:1.00
      [10/15] F1:0.75 Clarity:0.80 Precision:0.67
      [11/15] F1:0.80 Clarity:0.80 Precision:0.80
      [12/15] F1:0.89 Clarity:0.80 Precision:0.90
      [13/15] F1:0.90 Clarity:0.80 Precision:0.90
      [14/15] F1:0.95 Clarity:0.90 Precision:0.90
      [15/15] F1:0.89 Clarity:0.80 Precision:0.67

==================================================
Prompt: filipe1309/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.84 ✓
  - Correctness: 0.84 ✓

Métricas Base:
  - F1-Score: 0.84 ✓
  - Clarity: 0.84 ✓
  - Precision: 0.85 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8418
--------------------------------------------------

✅ STATUS: APROVADO - Todas as métricas >= 0.8

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

✅ Todos os prompts atingiram todas as métricas >= 0.8!

✓ Confira os resultados em:
  https://smith.langchain.com/projects/
```

Tentativa 4:
```sh
make evaluate                                                                                                                                                                               ─╯

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: openai
Modelo Principal: gpt-4o-mini
Modelo de Avaliação: gpt-4o

Criando dataset de avaliação: -eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset '-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: filipe1309/bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: filipe1309/bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
   Dataset: 15 exemplos
   Avaliando exemplos...
      [1/15] F1:0.75 Clarity:0.75 Precision:0.80
      [2/15] F1:0.75 Clarity:0.70 Precision:0.90
      [3/15] F1:0.75 Clarity:0.75 Precision:0.90
      [4/15] F1:0.69 Clarity:0.85 Precision:0.90
      [5/15] F1:0.58 Clarity:0.85 Precision:0.67
      [6/15] F1:0.69 Clarity:0.85 Precision:0.83
      [7/15] F1:0.90 Clarity:0.85 Precision:0.93
      [8/15] F1:1.00 Clarity:1.00 Precision:1.00
      [9/15] F1:0.95 Clarity:0.95 Precision:0.93
      [10/15] F1:0.69 Clarity:0.85 Precision:0.80
      [11/15] F1:0.80 Clarity:0.75 Precision:0.90
      [12/15] F1:0.85 Clarity:0.80 Precision:0.90
      [13/15] F1:0.95 Clarity:0.85 Precision:0.90
      [14/15] F1:0.95 Clarity:0.90 Precision:0.83
      [15/15] F1:0.89 Clarity:0.80 Precision:0.67

==================================================
Prompt: filipe1309/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.85 ✓
  - Correctness: 0.83 ✓

Métricas Base:
  - F1-Score: 0.81 ✓
  - Clarity: 0.83 ✓
  - Precision: 0.86 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.8361
--------------------------------------------------

✅ STATUS: APROVADO - Todas as métricas >= 0.8

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

✅ Todos os prompts atingiram todas as métricas >= 0.8!

✓ Confira os resultados em:
  https://smith.langchain.com/projects/
```