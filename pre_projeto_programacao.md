# PRÉ-PROJETO: SISTEMA DE ORIENTAÇÃO VOCACIONAL EM PYTHON

**Instituição:** SATC - Educação e Tecnologia  
**Curso:** Inteligência Artificial (Noturno - 2ª Fase)  
**Componente Curricular:** Programação I  
**Professor(a):** Evandro Luiz Martignago  
**Data de Entrega:** 13/11/2026 (Até 22:00) | **Peso:** 2.0  

---

## 1. Integrantes da Equipe
* **Ana Carolina**
* **Daniela**

---

## 2. Descrição / Apresentação do Sistema

O sistema consiste em uma ferramenta de Teste Vocacional Interativo desenvolvida em Python. Seu objetivo é auxiliar estudantes e profissionais na descoberta de áreas de atuação que se alinham ao seu perfil pessoal e preferências.

O programa interage com o usuário por meio de perguntas direcionadas a quatro grandes áreas do conhecimento: Tecnologia, Saúde, Humanas e Negócios. Ao final do questionário, o sistema contabiliza os pontos de forma dinâmica, identifica a área com maior afinidade e exibe uma lista personalizada de profissões sugeridas para aquela carreira. O sistema foi projetado para rodar continuamente em um terminal, permitindo que múltiplos testes sejam realizados na mesma sessão sem perder o estado atual da execução.

---

## 3. Principais Funções do Projeto a Ser Implementado

Para cumprir as regras e os controles de fluxo exigidos, o código-fonte foi estruturado nas seguintes funções principais:

* **`menu()`**: Gerencia a interface interativa principal utilizando um laço de repetição `while`. Apresenta as opções de realizar o teste ou encerrar o programa usando estruturas condicionais de escolha (`match/case`).
* **`questionario()`**: Limpa as pontuações anteriores e executa a sequência de perguntas dinâmicas para o usuário, mapeando as respostas para suas respectivas áreas.
* **`fazer_pergunta(pergunta, area, pontos)`**: Automatiza a captura de respostas em formato Sim/Não (S/N). Possui um mecanismo de validação com `while` e `if/elif` que impede entradas inválidas e soma os pontos diretamente no dicionário global de áreas.
* **`mostrar_resultado()`**: Processa os dados armazenados temporariamente, calcula o valor máximo de pontuação para determinar a área recomendada e percorre as listas de carreiras utilizando o laço `for` para exibir os resultados na tela.
