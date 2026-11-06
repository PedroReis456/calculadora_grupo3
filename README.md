# UniRide

**Uma forma mais simples de compartilhar o caminho até a universidade.**

O UniRide é uma plataforma que conecta estudantes universitários interessados em compartilhar caronas. A proposta é aproximar pessoas que possuem trajetos, horários e rotinas semelhantes, facilitando a organização de deslocamentos recorrentes.

O projeto está sendo desenvolvido no âmbito da disciplina **ENG4021 — Projeto Integrado de Software**, da PUC-Rio, pelo Grupo 3.

## Sobre o projeto

Encontrar pessoas para compartilhar o trajeto até a universidade pode ser difícil. Embora existam grupos de mensagens e plataformas de carona, nem sempre é fácil encontrar alguém que tenha uma rotina compatível.

O UniRide busca solucionar esse problema por meio de uma plataforma voltada ao ambiente universitário, na qual estudantes podem cadastrar seus trajetos e encontrar pessoas com interesses e horários semelhantes.

## Objetivos

- Conectar estudantes que realizam trajetos semelhantes.
- Facilitar a organização de caronas recorrentes.
- Incentivar o compartilhamento de veículos.
- Reduzir os custos individuais de deslocamento.
- Contribuir para uma mobilidade urbana mais colaborativa e sustentável.

## Funcionalidades propostas

- Cadastro e autenticação de usuários.
- Cadastro de trajetos, horários e dias da semana.
- Busca por caronas compatíveis.
- Visualização de informações sobre motoristas e passageiros.
- Gerenciamento de caronas e solicitações.

As funcionalidades estão sujeitas à evolução do projeto e à implementação de cada etapa.

## Tecnologias

- **Python**
- **Django** — desenvolvimento do backend.
- **HTML e CSS** — estrutura e estilização das páginas.
- **Figma** — prototipação e planejamento das interfaces.
- **Git e GitHub** — versionamento e colaboração.

## Estrutura do repositório

```text
ENG4021_Grupo3_Transporte/
│
├── Calculadora/
├── Concorrencia_e_Publico/
├── Entrevista/
├── Estudo de risco/
├── Ideias/
├── Marca_e_Identidade/
├── Monetização/
├── Planejamento/
├── Prototipo_Telas/
├── Termos de uso e privacidade/
│
├── UniRide/
├── assets/
├── css/
├── html/
│
├── impactos_sociais/
├── requirements.txt
└── README.md
```

As pastas organizam os materiais de pesquisa, planejamento, prototipação e desenvolvimento do UniRide.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/bernardoc3po/ENG4021_Grupo3_Transporte.git
```

### 2. Entrar na pasta

```bash
cd ENG4021_Grupo3_Transporte
```

### 3. Criar e ativar um ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o servidor

Acesse a pasta que contém o arquivo `manage.py` e execute:

```bash
python manage.py migrate
python manage.py runserver
```

Depois, acesse:

```text
http://127.0.0.1:8000/
```

## Desenvolvimento

O UniRide é desenvolvido de forma colaborativa, com organização das tarefas, documentação das decisões e versionamento do código pelo GitHub.

O repositório reúne tanto os materiais de concepção do produto quanto os arquivos relacionados à sua implementação.

## Projeto acadêmico

**Disciplina:** ENG4021 — Projeto Integrado de Software  
**Instituição:** Pontifícia Universidade Católica do Rio de Janeiro (PUC-Rio)  
**Grupo:** 3  
**Projeto:** UniRide
