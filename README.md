# Controle-remoto
Pratica de POO curso CURSO EM VÍDEO

# 📺 Controle Remoto Virtual

Projeto desenvolvido em **Python** para simular o funcionamento básico de um controle remoto de televisão diretamente pelo terminal.

O projeto permite **ligar e desligar a TV**, alterar os **canais**, controlar o **volume** e visualizar todas as informações através de uma interface estilizada utilizando a biblioteca **Rich**.

---

## 🚀 Funcionalidades

O sistema possui as seguintes funcionalidades:

- 🔴 Ligar e desligar a TV;
- 📺 Aumentar o canal;
- 📺 Diminuir o canal;
- 🔊 Aumentar o volume;
- 🔉 Diminuir o volume;
- 🔄 Retorno automático do canal máximo para o canal mínimo;
- 🔄 Retorno automático do canal mínimo para o canal máximo;
- 🎚️ Controle de volume com limite mínimo e máximo;
- 🎨 Interface visual no terminal utilizando a biblioteca **Rich**.

---

## 🖥️ Como funciona

Ao iniciar o programa, um objeto da classe `Contole_remoto` é criado:

```python
c = Contole_remoto()
```

Esse objeto representa o controle remoto e é responsável por armazenar e controlar informações como:

- Canal atual;
- Volume atual;
- Estado da televisão (ligada ou desligada).

O programa permanece funcionando através de um loop:

```python
while True:
```

Dentro desse loop, a TV é atualizada constantemente e o usuário pode inserir comandos para controlar suas funções.

---

## 🎮 Comandos disponíveis

| Comando | Função |
|--------|--------|
| `@` | Liga ou desliga a TV |
| `>` | Aumenta o canal |
| `<` | Diminui o canal |
| `+` | Aumenta o volume |
| `-` | Diminui o volume |

Exemplo de interação:

```text
<CAL1> | -VOL1+
```

O usuário digita um dos comandos disponíveis e o programa executa a ação correspondente.

---

## 🧠 Conceitos utilizados

Este projeto foi desenvolvido para praticar conceitos fundamentais e intermediários de Python.

### 🐍 Python

- Classes e objetos;
- Programação Orientada a Objetos (POO);
- Construtor `__init__`;
- Atributos de classe;
- Atributos de instância;
- Métodos;
- Condicionais (`if` e `else`);
- Laços de repetição (`while` e `for`);
- Estrutura `match/case`;
- Operadores lógicos;
- Operador `not`;
- F-strings.

---

## 📦 Biblioteca utilizada

O projeto utiliza a biblioteca **Rich** para melhorar a aparência da interface no terminal.

Bibliotecas utilizadas:

```python
from rich import print
from rich.panel import Panel
```

A biblioteca permite criar uma interface mais visual, utilizando:

- Painéis;
- Cores;
- Formatação de texto.

---

## 📺 Funcionamento dos canais

A televisão possui canais entre:

```text
Canal mínimo: 1
Canal máximo: 6
```

Quando o usuário está no canal máximo e aumenta novamente, o sistema retorna para o canal mínimo.

Exemplo:

```text
1 → 2 → 3 → 4 → 5 → 6 → 1
```

Ao diminuir o canal estando no canal mínimo:

```text
1 → 6
```

---

## 🔊 Funcionamento do volume

O volume possui níveis entre:

```text
Volume mínimo: 1
Volume máximo: 6
```

A interface utiliza cores para representar visualmente os níveis de volume:

🟩 Volume selecionado  
🟦 Volume não selecionado

---

## 🗂️ Estrutura principal do projeto

```text
controle-remoto/
│
├── controle_remoto.py
└── README.md
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd controle-remoto
```

### 3. Instale a biblioteca Rich

```bash
pip install rich
```

### 4. Execute o programa

```bash
python controle_remoto.py
```


## 👨‍💻 Autor

Projeto desenvolvido por **Adriel** como parte dos estudos de **Python e Programação Orientada a Objetos**, com foco na evolução para o desenvolvimento **Back-End**.

---

⭐ Este projeto faz parte do meu processo de aprendizado e evolução como desenvolvedor.
