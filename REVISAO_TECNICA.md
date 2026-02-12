# Revisão técnica do repositório

## Visão geral

O repositório contém **dois projetos Django distintos**:

- `DJANGO-ACADAS/evolucao_academia`: app de acompanhamento de treinos e medidas.
- `farmacia/farmacia`: app de controle de compras em farmácia.

Além do código fonte, o repositório versiona arquivos gerados em runtime, como `db.sqlite3` e `__pycache__`.

## O que fazer agora (prioridade)

1. **Definir o foco do repositório**
   - Separar os dois sistemas em repositórios diferentes, ou
   - manter monorepo com documentação clara de cada projeto.

2. **Higiene de versionamento**
   - Adicionar `.gitignore` para remover de versionamento:
     - `__pycache__/`
     - `*.pyc`
     - `db.sqlite3`
     - `.venv/`

3. **Corrigir bugs funcionais críticos no projeto de academia**
   - Em `costas_delete`, está sendo buscado objeto de `Pernas` ao invés de `Costas`.
   - Em `pernas_update`, o template de retorno em erro de validação aponta para `treinos_form.html`, mas o template usado no restante do fluxo é `pernas_form.html`.
   - Campo `agachamneto` no model `Pernas` aparenta typo de nomenclatura.

4. **Criar base mínima de qualidade**
   - `requirements.txt` (ou `pyproject.toml`) com versões.
   - Testes unitários para CRUD básico das views.
   - Pipeline simples de CI (`python -m pip install -r requirements.txt`, `manage.py test`, lint).

## Pontos de melhoria por área

### 1) Arquitetura e organização

- Evitar múltiplos projetos sem fronteira clara no mesmo repositório.
- Estruturar diretórios de templates estáticos conforme convenção Django (`static/` e `templates/` por app).

### 2) Qualidade de código

- Remover imports duplicados (`from django.shortcuts import render` aparece duas vezes em algumas views).
- Padronizar nomes em português/inglês e corrigir typos para evitar dívida técnica e migrações futuras mais custosas.

### 3) Configuração Django

- Evitar `SECRET_KEY` fixa no código; mover para variável de ambiente.
- Evitar `DEBUG=True` fora de ambiente local.
- `STATICFILES_DIRS` usa barra invertida no caminho; preferir `Path`/`os.path.join` multiplataforma sem path hardcoded com `\\`.

### 4) Dados e persistência

- Não versionar banco SQLite local.
- Definir estratégia de migrações e seed de dados para facilitar onboarding.

### 5) UX e produto

- Incluir screenshots reais no README.
- Documentar “como rodar localmente” (setup de ambiente, migrações, usuário admin).
- Definir backlog: autenticação, filtros por data/aluno, exportação de histórico.

## Roadmap sugerido (2 semanas)

### Semana 1 (base técnica)

- [ ] Separar escopo do repositório.
- [ ] Criar `.gitignore` e limpar artefatos versionados.
- [ ] Corrigir bugs de `costas_delete` e `pernas_update`.
- [ ] Adicionar `requirements.txt` e instruções de setup.

### Semana 2 (qualidade + entrega)

- [ ] Criar testes básicos das operações CRUD.
- [ ] Ajustar segurança de settings via variáveis de ambiente.
- [ ] Melhorar README com execução local e screenshots.
- [ ] Configurar CI simples no GitHub Actions.

## Resultado esperado após essas melhorias

- Repositório mais claro e com propósito definido.
- Menor risco de erros em produção.
- Onboarding mais rápido para novos colaboradores.
- Evolução de funcionalidades com mais segurança.
