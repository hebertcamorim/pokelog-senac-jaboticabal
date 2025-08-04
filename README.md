# 🐾 PokeLog

Projeto desenvolvido para aula demonstrativa como **Docente de Informática no SENAC Jaboticabal**.  
O **PokeLog** utiliza **Flask (Python)** para consumir e exibir dados da [PokeAPI](https://pokeapi.co/), uma API pública com informações sobre o universo Pokémon.

---

## 🎯 Objetivo Educacional

Este projeto foi criado com fins didáticos para demonstrar:

- Consumo de APIs REST em Python.
- Estrutura básica de um backend com Flask.
- Manipulação de dados JSON.
- Aplicação prática e envolvente com temática de interesse dos alunos.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask**
- **Módulo Requests (embutido na instalação do projeto)**

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:

git clone [https://github.com/seu-usuario/pokelog.git](https://github.com/hebertcamorim/pokelog-senac-jaboticabal)

2. Execute o arquivo principal diretamente com o Python:

python app.py

## 🔗 Endpoints Disponíveis

| Método | Rota              | Descrição                            |
|--------|-------------------|----------------------------------------|
| GET    | `/`               | Mensagem de boas-vindas                |
| GET    | `/pokemon/<nome>` | Retorna dados do Pokémon informado     |
| GET    | `/types`          | Lista os tipos existentes              |
| GET    | `/abilities`      | Lista habilidades comuns dos Pokémons  |

---

## 📸 Exemplo de Resposta

**Requisição:**  
`GET /pokemon/charmander`

**Resposta:**

```json
{
  "name": "charmander",
  "id": 4,
  "types": ["fire"],
  "abilities": ["blaze", "solar-power"],
  "sprite": "https://raw.githubusercontent.com/PokeAPI/..."
}

git clone https://github.com/seu-usuario/pokelog.gitithub.com/seu-usuario/pokelog.git
cd pokelog
