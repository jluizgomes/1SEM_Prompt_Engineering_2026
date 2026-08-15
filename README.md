# 1SEM — Prompt Engineering and Artificial Intelligence (2026)

Repositório referente ao **1º Semestre 2026** da disciplina **Prompt Engineering and Artificial Intelligence**
do curso de **Ciência da Computação** da **FIAP**.

O repositório possui a seguinte estrutura organizada sob a pasta `aulas/`, contendo:
- Notebooks das 14 aulas (Demo e Aluno)
- Projetos de referência do professor (com código completo)
- Esqueletos para alunos (com `# TODO`)
- Checkpoints de avaliação
- Infraestrutura Docker para laboratório local
- Fichas de exercícios para o professor
- Modelos proibidos e stack tecnológica aprovada

---

## Índice

1. [Visão geral do repositório](#1-visão-geral-do-repositório)
2. [Estrutura de pastas](#2-estrutura-de-pastas)
3. [Plano do semestre](#3-plano-do-semestre)
4. [Notebooks das aulas](#4-notebooks-das-aulas)
5. [Projetos — Referência vs Aluno](#5-projetos--referência-vs-aluno)
6. [Infraestrutura Docker](#6-infraestrutura-docker)
7. [Fichas de exercícios — Professor](#7-fichas-de-exercícios--professor)
8. [Arquivos ignorados](#8-arquivos-ignorados-mantidos-apenas-localmente)
9. [Ebooks e Referências Acadêmicas](#9-ebooks-e-referências-acadêmicas)
10. [Stack tecnológica aprovada](#10-stack-tecnológico-aprovado)
11. [Modelos proibidos](#11-modelos-proibidos)
12. [Referências acadêmicas](#12-referências-acadêmicas)
13. [Troubleshooting](#13-troubleshooting)

---

## 1. Visão geral do repositório

| Componente | Descrição | Público |
|---|---|---|
| `aulas/Checkpoints/` | 3 arquivos HTML de checkpoint (CKP01, CKP02, CKP03) | Professor e aluno |
| `aulas/fiap-ai-lab-complete/` | Stack Docker completa (12+ containers) | Professor e aluno |
| `aulas/fiap-openwebui-ollama-setup/` | Setup Docker leve (Ollama + Open WebUI) | Aluno |
| `aulas/fichas_professor_1SEM/` | 14 fichas de exercícios em HTML | Professor |
| `aulas/projetos/` | 12 pastas de referência do professor (Aula_01 a Aula_12) | Professor |
| `aulas/projetos_aluno/` | 12 pastas de esqueletos para alunos (com `# TODO`) | Alunos |
| `aulas/Modulo_1_Fundamentos_de_IA/` | Conteúdo do Módulo 1 (Aulas 01–04) | Professor e aluno |
| `aulas/Modulo_2_Tecnicas_de_Prompt/` | Conteúdo do Módulo 2 (Aulas 05–08) | Professor e aluno |
| `aulas/Modulo_3_Python_para_IA/` | Conteúdo do Módulo 3 (Aulas 09–11) | Professor e aluno |
| `aulas/Modulo_4_Seguranca_Carreiras_Encerramento/` | Conteúdo do Módulo 4 (Aulas 12–14) | Professor e aluno |
| `Plano_Aulas_1Sem_2026.pdf` | Plano detalhado do 1º semestre 2026 | Professor e aluno |

---

## 2. Estrutura de pastas

```
1SEM_Prompt_Engineering_2026/
├── .gitignore
├── Plano_Aulas_1Sem_2026.pdf
├── README.md
└── aulas/
    ├── .DS_Store
    ├── Checkpoints/
    │   ├── CKP01_1Semestre_Mapa_IA.html
    │   ├── CKP02_1Semestre_Biblioteca_Prompts.html
    │   └── CKP03_1Semestre_Chatbot_Especializado.html
    ├── fiap-ai-lab-complete/
    │   ├── docker-compose.yml
    │   ├── Makefile
    │   ├── .env / .env.example
    │   ├── ollama/
    │   ├── postgres/
    │   ├── chromadb/
    │   ├── pipelines/
    │   ├── searxng/
    │   └── mem0/
    ├── fiap-openwebui-ollama-setup/
    │   ├── docker-compose.yml
    │   ├── Dockerfile
    │   ├── entrypoint.sh
    │   └── .env.example
    ├── fichas_professor_1SEM/
    │   ├── 1Sem_Aula_01_Ficha_Professor_Exercicios.html
    │   ├── 1Sem_Aula_02_Ficha_Professor_Exercicios.html
    │   ├── ... (14 fichas no total)
    │   └── 1Sem_Aula_14_Ficha_Professor_Exercicios.html
    ├── projetos/
    │   ├── Aula_01_O_que_e_IA_Da_ficcao_a_realidade/
    │   │   ├── main.py              # Código completo e funcional
    │   │   ├── requirements.txt     # Dependências Python
    │   │   ├── .env                 # Variáveis de ambiente (chave já preenchida)
    │   │   ├── .env.example         # Template das variáveis
    │   │   ├── .gitignore
    │   │   └── README.md            # Instruções específicas da aula
    │   ├── Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_03_Etica_Vies_LGPD_antes_de_construir/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_04_Anatomia_do_prompt_primeiro_codigo_Python/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_05_Zero_shot_One_shot_Few_shot/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_06_Chain_of_Thought_pense_passo_a_passo/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_07_Role_prompting_parametros_do_modelo/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_08_Funcoes_loops_estrutura_chamada_API/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_09_Historico_de_conversa_como_chatbot_lembra/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_10_Prompts_templates_variaveis/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   ├── Aula_11_Mini_chatbot_integrador/
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   ├── .env
    │   │   ├── .env.example
    │   │   ├── .gitignore
    │   │   └── README.md
    │   └── Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails/
    │       ├── main.py
    │       ├── requirements.txt
    │       ├── .env
    │       ├── .env.example
    │       ├── .gitignore
    │       └── README.md
    ├── projetos_aluno/
    │   ├── Aula_01_O_que_e_IA_Da_ficcao_a_realidade/       # Pasta vazia (setup.sh/.gitignore pendentes)
    │   ├── Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura/
    │   ├── Aula_03_Etica_Vies_LGPD_antes_de_construir/
    │   ├── Aula_04_Anatomia_do_prompt_primeiro_codigo_Python/
    │   ├── Aula_05_Zero_shot_One_shot_Few_shot/
    │   ├── Aula_06_Chain_of_Thought_pense_passo_a_passo/
    │   ├── Aula_07_Role_prompting_parametros_do_modelo/
    │   ├── Aula_08_Funcoes_loops_estrutura_chamada_API/
    │   ├── Aula_09_Historico_de_conversa_como_chatbot_lembra/
    │   ├── Aula_10_Prompts_templates_variaveis/
    │   ├── Aula_11_Mini_chatbot_integrador/
    │   └── Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails/
    ├── Modulo_1_Fundamentos_de_IA/
    │   ├── Aula_01_O_que_e_IA_Da_ficcao_a_realidade_aluno.ipynb
    │   ├── Aula_01_O_que_e_IA_Da_ficcao_a_realidade_demo.ipynb
    │   ├── Aula_01_O_que_e_IA_Da_ficcao_a_realidade.html
│   │   ├── Aula_01_O_que_e_IA_Da_ficcao_a_realidade.pdf
│   │   ├── Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura_aluno.ipynb
│   │   ├── Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura_demo.ipynb
│   │   ├── Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura.html
│   │   ├── Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura.pdf
│   │   ├── Aula_03_Etica_Vies_LGPD_antes_de_construir_aluno.ipynb
│   │   ├── Aula_03_Etica_Vies_LGPD_antes_de_construir_demo.ipynb
│   │   ├── Aula_03_Etica_Vies_LGPD_antes_de_construir.html
│   │   └── Aula_03_Etica_Vies_LGPD_antes_de_construir.pdf
│   ├── Modulo_2_Tecnicas_de_Prompt/
    │   ├── Aula_04_Anatomia_do_prompt_primeiro_codigo_Python_aluno.ipynb
    │   ├── Aula_04_Anatomia_do_prompt_primeiro_codigo_Python_demo.ipynb
    │   ├── Aula_04_Anatomia_do_prompt_primeiro_codigo_Python.html
    │   ├── Aula_04_Anatomia_do_prompt_primeiro_codigo_Python.pdf
    │   ├── Aula_05_Zero_shot_One_shot_Few_shot_aluno.ipynb
    │   ├── Aula_05_Zero_shot_One_shot_Few_shot_demo.ipynb
    │   ├── Aula_05_Zero_shot_One_shot_Few_shot.html
    │   ├── Aula_05_Zero_shot_One_shot_Few_shot.pdf
    │   ├── Aula_06_Chain_of_Thought_pense_passo_a_passo_aluno.ipynb
    │   ├── Aula_06_Chain_of_Thought_pense_passo_a_passo_demo.ipynb
    │   ├── Aula_06_Chain_of_Thought_pense_passo_a_passo.html
    │   ├── Aula_06_Chain_of_Thought_pense_passo_a_passo.pdf
│   │   ├── Aula_07_Role_prompting_parametros_do_modelo_aluno.ipynb
│   │   ├── Aula_07_Role_prompting_parametros_do_modelo_demo.ipynb
│   │   ├── Aula_07_Role_prompting_parametros_do_modelo.html
│   │   └── Aula_07_Role_prompting_parametros_do_modelo.pdf
│   ├── Modulo_3_Python_para_IA/
│   │   ├── Aula_08_Funcoes_loops_estrutura_chamada_API_aluno.ipynb
│   │   ├── Aula_08_Funcoes_loops_estrutura_chamada_API_demo.ipynb
│   │   ├── Aula_08_Funcoes_loops_estrutura_chamada_API.html
│   │   ├── Aula_08_Funcoes_loops_estrutura_chamada_API.pdf
│   │   ├── Aula_09_Historico_de_conversa_como_chatbot_lembra_aluno.ipynb
│   │   ├── Aula_09_Historico_de_conversa_como_chatbot_lembra_demo.ipynb
│   │   ├── Aula_09_Historico_de_conversa_como_chatbot_lembra.html
│   │   └── Aula_09_Historico_de_conversa_como_chatbot_lembra.pdf
│   ├── Modulo_4_Seguranca_Carreiras_Encerramento/
│   │   ├── Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails_aluno.ipynb
│   │   ├── Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails_demo.ipynb
│   │   ├── Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails.html
│   │   ├── Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails.pdf
│   │   ├── Aula_13_IA_mercado_trabalho_carreiras_portfolio_aluno.ipynb
│   │   ├── Aula_13_IA_mercado_trabalho_carreiras_portfolio_demo.ipynb
│   │   ├── Aula_13_IA_mercado_trabalho_carreiras_portfolio.html
│   │   └── Aula_13_IA_mercado_trabalho_carreiras_portfolio.pdf
│   └── Aula_14_O_que_vem_a_seguir_aluno.ipynb
│   └── Aula_14_O_que_vem_a_seguir_demo.ipynb
│
```

**Observação:** Cada pasta `aulas/projetos/Aula_XX/` contém `main.py` completo (professor) ou com `# TODO` (aluno), mais `requirements.txt`, `.env`, `.env.example`, `.gitignore` e `README.md` específicos.

---

## 3. Plano do semestre

| # | Título | Data | Módulo | CKP |
|---|---|---|---|---|
| 01 | Role prompting, system prompts, parâmetros e reasoning LLMs | 04/Ago | M1 | — |
| 02 | Segurança em LLMs: prompt injection, jailbreak e guardrails | 11/Ago | M1 | — |
| 03 | Ética, viés algorítmico, LGPD e responsabilidade no uso de IA | 18/Ago | M1 | — |
| 04 | Context Engineering, frameworks reutilizáveis e structured output | 25/Ago | M1 | CKP01 |
| 05 | LangChain: LCEL, ChatOllama, chains, templates e memory | 01/Set | M2 | — |
| 06 | Chatbots e assistentes virtuais com gerenciamento de contexto | 08/Set | M2 | — |
| 07 | Embeddings + RAG com ChromaDB e nomic-embed-text via Ollama | 15/Set | M2 | — |
| 08 | RAG avançado: chunking, reranking, RAGAS e synthetic RAG | 22/Set | M2 | CKP02 |
| 09 | Interfaces com Gradio/Streamlit + deploy no Colab com URL pública | 29/Set | M3 | — |
| 10 | Agentes de IA: ReAct, tools e function calling | 06/Out | M3 | — |
| 11 | Context Engineering para agentes: curadoria em loop agêntico | 13/Out | M3 | — |
| 12 | Agente com RAG como tool + interface Gradio ao vivo | 20/Out | M3 | CKP03 |
| 13 | LangGraph, Deep Agents e multiagentes supervisor/worker | 27/Out | M4 | — |
| 14 | Tendências 2026 e o futuro de Prompt & Context Engineering | 03/Nov | M4 | — |

**Módulos:**
- **M1** (Aulas 01–04): Fundamentos de Prompt Engineering
- **M2** (Aulas 05–08): LangChain, RAG e Embeddings
- **M3** (Aulas 09–11): Interfaces, Agentes e Integração
- **M4** (Aulas 12–14): Avançado e Tendências

**Checkpoints:**
- CKP01 — Obrigatório (Aula 04, 25/Ago)
- CKP02 — Obrigatório (Aula 08, 22/Set)
- CKP03 — Opcional (Aula 12, 20/Out)

---

## 4. Notebooks das aulas

A pasta `aulas/Modulo_1_Fundamentos_de_IA/` through `aulas/Modulo_4_Seguranca_Carreiras_Encerramento/` contém **27 notebooks** Jupyter no formato:

| Tipo | Sufixo | Descrição |
|---|---|---|
| Demo | `_Demo.ipynb` | Código demonstrativo do professor durante a aula |
| Aluno | `_Aluno.ipynb` | Atividade prática para o aluno completar |

> Aula 02 possui versões adicionais `_Demo_Local.ipynb` e `_Aluno_Local.ipynb`
> para uso com Ollama local ao invés de API cloud.

Os notebooks estão organizados por módulo:
- **Módulo 1** (Aulas 01–04): Fundamentos de IA, tokens, contexto, temperatura, ética, vieses e LGPD
- **Módulo 2** (Aulas 05–08): Zero-shot/One-shot/Few-shot, Chain-of-Thought, Role prompting, funções/loops/API, templates e variáveis
- **Módulo 3** (Aulas 09–11): Histórico de conversa, chatbot integrador, prompts templates
- **Módulo 4** (Aulas 12–14): Segurança LLMs, mercado de trabalho e IA, o que vem a seguir

### Como usar no Google Colab

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. File → Upload notebook → selecione o arquivo `.ipynb`
3. Execute as células na ordem

---

## 5. Projetos — Referência vs Aluno

### `aulas/projetos/` (Professor)

Contém **12 pastas de referência completas**, una por aula. Cada pasta tem:

```
Aula_XX_Nome/
├── main.py              # Código completo e funcional
├── requirements.txt     # Dependências Python
├── .env                 # Variáveis de ambiente (chave já preenchida)
├── .env.example         # Template das variáveis
├── .gitignore
└── README.md            # Instruções específicas da aula
```

| # | Pasta | Tema |
|---|---|---|
| 01 | `Aula_01_O_que_e_IA_Da_ficcao_a_realidade` | Revisão de IA: do fiction ao reality |
| 02 | `Aula_02_Como_um_LLM_pensa_tokens_contexto_temperatura` | Como um LLM pensa: tokens, contexto, temperatura |
| 03 | `Aula_03_Etica_Vies_LGPD_antes_de_construir` | Ética, viés e LGPD antes de construir |
| 04 | `Aula_04_Anatomia_do_prompt_primeiro_codigo_Python` | Anatomia do prompt: primeiro código Python |
| 05 | `Aula_05_Zero_shot_One_shot_Few_shot` | Zero-shot, One-shot e Few-shot |
| 06 | `Aula_06_Chain_of_Thought_pense_passo_a_passo` | Chain-of-Thought: pense passo a passo |
| 07 | `Aula_07_Role_prompting_parametros_do_modelo` | Role prompting e parâmetros do modelo |
| 08 | `Aula_08_Funcoes_loops_estrutura_chamada_API` | Funções, loops e estrutura de chamada de API |
| 09 | `Aula_09_Historico_de_conversa_como_chatbot_lembra` | Histórico de conversa como chatbot lembra |
| 10 | `Aula_10_Prompts_templates_variaveis` | Prompts templates e variáveis |
| 11 | `Aula_11_Mini_chatbot_integrador` | Mini chatbot integrador |
| 12 | `Aula_12_Seguranca_LLMs_injection_alucinacao_guardrails` | Segurança LLMs: injection, alucinação, guardrails |

### `aulas/projetos_aluno/` (Aluno)

Contém **12 pastas de esqueletos** com `# TODO` para os alunos completarem:

```python
# TODO: Implemente a lógica principal da chain
# TODO: Adicione streaming com .stream()
# TODO: Configure o modelo Ollama
```

Cada arquivo `main.py` mantém toda a infraestrutura (imports, config, LLM setup)
e pede ao aluno para implementar apenas a lógica principal.

> As pastas `projetos_aluno/Aula_XX/` têm estrutura básica porém alguns têm arquivos pendentes de setup (`.env.example`, `.gitignore`, `setup.sh`).

---

## 6. Infraestrutura Docker

### 6.1 Setup leve — `aulas/fiap-openwebui-ollama-setup/`

Recomendado para máquinas com pouca memória ou para uso rápido.

| Serviço | Container | Porta | Descrição |
|---|---|---|---|
| Ollama | `fiap-ollama` | `11434` | Servidor de modelos (CPU) |
| Open WebUI | `fiap-open-webui` | `3000` | Interface de chat |

**Modelos padrão:** `qwen3.5:0.8b` (chat) + `qwen3-embedding:0.6b` (embeddings)

```bash
cd aulas/fiap-openwebui-ollama-setup
cp .env.example .env
docker compose up -d --build
# Acesse http://localhost:3000
```

### 6.2 Stack completa — `aulas/fiap-ai-lab-complete/`

Laboratório completo com 12+ containers para todas as aulas.

| Serviço | Container | Porta | Uso nas aulas |
|---|---|---|---|
| Postgres (pgvector) | `fiap-postgres` | `5432` | Banco de dados unificado |
| Ollama | `fiap-ollama` | `11434` | LLM + embeddings |
| Open WebUI | `fiap-open-webui` | `3000` | Interface de chat |
| ChromaDB | `fiap-chromadb` | `8000` | Vector store (Aulas 05–12) |
| SearXNG | `fiap-searxng` | `8080` | Metabuscador web |
| mem0 | `fiap-mem0` | `8100` | Memória de longo prazo |
| Firecrawl | `fiap-firecrawl-api` | `3002` | Scrape/crawl web |
| Langfuse | `fiap-langfuse-web` | `3001` | Observabilidade (perfil separado) |

**Perfis disponíveis:**

| Perfil | Containers | Quando usar |
|---|---|---|
| `minimum` | postgres, ollama, open-webui | Máquina fraca, Aulas 01–04 |
| `complete` | todos (12 containers) | Aula normal, todas as integrações |
| `rag` | base + pipelines + chromadb | Aulas de RAG (07, 08) |
| `search` | base + searxng + valkey | Aulas de busca web |
| `memory` | base + mem0 | Aula de memória (11) |

```bash
cd aulas/fiap-ai-lab-complete
cp .env.example .env
# Para uso completo:
make up-profile-complete
# Ou apenas o básico:
make up-profile-minimum
```

---

## 7. Fichas de exercícios — Professor

A pasta `aulas/fichas_professor_1SEM/` contém **14 fichas** de exercícios em HTML, uma para cada aula:

```
1Sem_Aula_01_Ficha_Professor_Exercicios.html
1Sem_Aula_02_Ficha_Professor_Exercicios.html
...
1Sem_Aula_14_Ficha_Professor_Exercicios.html
```

Estas fichas contêm exercícios teóricos e práticos alinhados ao conteúdo de cada aula, destinados ao uso pelo professor durante as sessões.

---

## 8. Arquivos ignorados (mantidos apenas localmente)

Alguns arquivos grandes ou específicos do professor são mantidos apenas localmente
e **não são commitados** no repositório:

| Arquivo | Descrição |
|---|---|
| `Plano_Aulas_1Sem_2026.pdf` | Plano detalhado do 1º semestre 2026 |

> Este arquivo está listado no `.gitignore`. Para acessá-lo, peça ao professor.

---

## 9. Ebooks e Referências Acadêmicas

### Livros (na pasta `Ebooks/`)

A pasta `Ebooks/` (não mostrada no tree por ser grande) contém livros para consulta:
- AI Agents in Action | Micheal Lanham
- Agentic Artificial Intelligence | Pascal Bornet et al.
- Agentic Coding with Claude Code | Eden Marco
- Agentic Design Patterns | Antonio Gullí
- Architecting AI Software Systems | Richard D. Avila
- Domain-Specific Small Language Models | Guglielmo Iozzia
- Effective Conversational AI | Andrew Freed et al.
- Essential GraphRAG | Tomaž Bratanic, Oskar Hane
- Learning LangChain | Mayo Oshin, Nuno
- Prompt Engineering | (hands-on guide)
- Python Illustrated | Maaike van Putten
- RAG with Python Cookbook | Dominik Polzer
- AI-Native LLM Security | Vaibhav Malik et al.
- A Practical Guide to RLHF | Sandip Kulkarni
- ChatGPT Business Goldmines | Dr. Ope Banwo

### Referências acadêmicas

**Livros:**
- Russell, S.; Norvig, P. — *Inteligência Artificial*. 3ª ed. Pearson, 2016
- Goodfellow, I. et al. — *Deep Learning*. Pearson, 2017
- Muller, A.; Guido, S. — *Introdução ao AM com Python*. Pearson, 2016
- Alpaydin, E. — *Aprendizado de Máquina*. Pearson, 2016
- Chollet, F. — *Deep Learning com Python*. Pearson, 2018

**Papers:**
- Vaswani et al. (2017) — "Attention Is All You Need" — arxiv.org/abs/1706.03762
- Brown et al. (2020) — "Language Models are Few-Shot Learners" — arxiv.org/abs/2005.14165
- Wei et al. (2022) — "Chain-of-Thought Prompting Elicits Reasoning in LLMs"
- Yao et al. (2022) — "ReAct: Synergizing Reasoning and Acting in LLMs" — arxiv.org/abs/2210.03629

**Online:**
- [promptingguide.ai](https://promptingguide.ai) — guia principal
- [anthropic.com/engineering](https://anthropic.com/engineering) — context engineering
- [python.langchain.com](https://python.langchain.com) — docs LangChain
- [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph) — docs LangGraph
- [ragas.io](https://ragas.io) — docs RAGAS
- [ollama.com](https://ollama.com) — modelos e API

**Legislação:**
- Lei 13.709/2018 (LGPD) — planalto.gov.br
- PL 2338/2023 (Marco Legal da IA) — senado.leg.br
- EU AI Act — Regulation 2024/1689

---

## 10. Stack tecnológica aprovada

### Modelos (via Ollama Cloud API)

```
qwen3.6:27b     → principal, maioria das demos
qwen3:8b        → alternativa leve
llama4:scout    → multimodal
gemma4:9b       → alternativa Google
deepseek-r2     → reasoning mode e CoT
devstral-small  → agentes de código
mistral-small   → alternativa europeia
phi4:14b        → alternativa Microsoft
nomic-embed-text → ÚNICO modelo de embeddings aprovado
```

### Frameworks Python

```
LangChain 0.3+  → LCEL, ChatOllama, chains, memory, agents, tools
LangGraph       → StateGraph, nodes, edges, MemorySaver
ChromaDB        → vector store local
RAGAS           → avaliação de RAG
Pydantic v2     → structured output, validação
Gradio          → interfaces web
Streamlit       → apps web com estado
```

### Ambiente

- Google Colab (gratuito) para notebooks
- Docker + Ollama (gratuito) para projetos locais
- Custo zero como requisito de atividade

---

## 11. Modelos proibidos

Os seguintes modelos **não devem ser usados** em código ou exemplos:

```
GPT-3, GPT-3.5, Claude 1, Claude 2, LLaMA 1, LLaMA 2, BERT, GPT-2
```

> Aceitos apenas em citação histórica com contexto explícito.

---

## 12. Referências acadêmicas

### Livros

- Russell, S.; Norvig, P. — *Inteligência Artificial*. 3ª ed. Pearson, 2016
- Goodfellow, I. et al. — *Deep Learning*. Pearson, 2017
- Chollet, F. — *Deep Learning com Python*. Pearson, 2018

### Papers

- Vaswani et al. (2017) — "Attention Is All You Need" — arxiv.org/abs/1706.03762
- Brown et al. (2020) — "Language Models are Few-Shot Learners" — arxiv.org/abs/2005.14165
- Wei et al. (2022) — "Chain-of-Thought Prompting Elicits Reasoning in LLMs"
- Yao et al. (2022) — "ReAct: Synergizing Reasoning and Acting in LLMs" — arxiv.org/abs/2210.03629

### Online

- [promptingguide.ai](https://promptingguide.ai) — guia principal
- [anthropic.com/engineering](https://anthropic.com/engineering) — context engineering
- [python.langchain.com](https://python.langchain.com) — docs LangChain
- [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph) — docs LangGraph
- [ragas.io](https://ragas.io) — docs RAGAS
- [ollama.com](https://ollama.com) — modelos e API

### Legislação

- Lei 13.709/2018 (LGPD) — planalto.gov.br
- PL 2338/2023 (Marco Legal da IA) — senado.leg.br
- EU AI Act — Regulation 2024/1689

---

## 13. Troubleshooting

### Ollama não responde

```bash
# Verificar se o container está rodando
docker compose ps

# Verificar logs
docker compose logs -f ollama

# Reiniciar
docker compose restart ollama
```

### Erro de permissão no PowerShell

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Modelo não encontrado

O download do modelo é automático na primeira execução. Verifique o progresso:

```bash
docker compose logs -f ollama
# Ou
docker exec -it fiap-ollama ollama list
```

### Espaço insuficiente

O setup completo (`aulas/fiap-ai-lab-complete`) pode consumir ~15 GB. Use o setup leve (`aulas/fiap-openwebui-ollama-setup`) se tiver pouca espaço (~4 GB).

---

**Licença**

Conteúdo educacional — FIAP · Ciência da Computação · 2026.

*Copyright © 2026 Prof. Jorge Luiz Gomes · FIAP · Todos os direitos reservados.*