# SOS Aluno — Projeto Web

## Componentes do Grupo

| Nome | Matrícula |
|------|------------|
| Marco Buffara | 2111337 |
| xxxxxxx | 22222222 |
| xxxxxxx | 2222222 |
| xxxxxxx | 2222222 |

---

## Descrição do Tema

O site **SOS Aluno** tem como objetivo criar uma plataforma colaborativa onde alunos podem avaliar o desempenho de seus professores de forma **anônima**, **transparente** e **construtiva**.

A aplicação permite que os estudantes:
- Atribuam notas e comentários aos professores;
- Consultem o perfil e a média de avaliação de cada docente;
- Filtram avaliações por curso, disciplina, universidade ou período;
- Contribuam para melhorar a qualidade do ensino por meio de feedbacks responsáveis.

**Tecnologias utilizadas:**
- Front-end: HTML, CSS
- Back-end: Django
- Banco de Dados: MySQL 
- Hospedagem: GitHub  

---

## Como Usar o Site

### Acesso
Abra o site no navegador pelo link:  
 -> [xxxxxxxxxxx](xxxxxxxxxxx)

---

### Página Inicial
A página inicial exibe uma barra para pesquisa de professores, curso ou faculdades no centro da página. No canto superior direito, tem dois butões para a página de Login e Cadastro. No rodapé da página, temos links para diferentes páginas do nosso site: **Início**, **Sobre**, **Contato**. Outrou links no rodapé são: **Termos de uso** e **Política de privacidade**

*Exemplo:*  
![Página inicial do site](./imagens/home.png)

---

### 3️⃣ Avaliar um Professor
Clique no botão **“Avaliar”** ao lado do nome do professor.  
Preencha o formulário com:
- Nota (de 1 a 5 estrelas ⭐)
- Comentário (opcional)
- Disciplina (opcional)

🖼️ *Exemplo:*  
![Formulário de avaliação](./imagens/avaliar.png)

---

### 4️⃣ Consultar Avaliações
Acesse o perfil do professor para ver todas as avaliações e estatísticas.

🖼️ *Exemplo:*  
![Página do professor com avaliações](./imagens/perfil-professor.png)

---

## 🧰 Como Executar Localmente (opcional)

Se quiser rodar o projeto na sua máquina:

```bash
# Clone o repositório
git clone https://github.com/seuusuario/avaliacao-professores.git

# Acesse a pasta do projeto
cd avaliacao-professores

# Instale as dependências (se houver)
npm install

# Inicie o servidor local
npm start
