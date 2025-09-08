# Atividade de CI com GitHub Actions

Este repositório contém uma aplicação de calculadora simples com testes e um workflow de Integração Contínua (CI) configurado com GitHub Actions.

## Funcionamento do CI

O workflow de CI está definido no arquivo `.github/workflows/ci.yml`. Ele é acionado a cada `push` para o repositório. As etapas do workflow são:

1.  **Checkout:** O código do repositório é baixado para o ambiente de execução.
2.  **Setup Python:** O ambiente Python na versão 3.9 é configurado.
3.  **Install Dependencies:** As dependências do projeto, listadas no arquivo `requirements.txt`, são instaladas.
4.  **Run Tests:** Os testes definidos na pasta `tests/` são executados com o `pytest`.

Se qualquer uma dessas etapas falhar, o workflow indicará um erro, notificando que as alterações recentes podem ter quebrado o projeto.

## Erro Proposital para Demonstração

Este repositório contém um erro proposital para demonstrar como o pipeline de CI detecta problemas.

**O Erro:**

No arquivo `app/calc.py`, a função `soma` está implementada para subtrair os números em vez de somá-los:

```python
def soma(a, b):
    return a - b  # ERRO proposital
```

**O Teste que Falha:**

O teste em `tests/test_calc.py` para esta função espera o resultado correto da soma:

```python
def test_soma():
    assert soma(2, 3) == 5
```

Quando o teste for executado no pipeline de CI, ele vai calcular `soma(2, 3)`, que a função com erro retornará como `-1` (`2 - 3`). O teste então vai verificar se `-1 == 5`, o que é falso, causando a falha do teste e, consequentemente, do workflow de CI.

**Como Corrigir em Aula:**

Para fazer o pipeline de CI passar (ficar "verde"), a correção é simples:

1.  Abra o arquivo `app/calc.py`.
2.  Altere a função `soma` para que ela retorne a soma real dos dois números.

A função corrigida ficará assim:

```python
def soma(a, b):
    return a + b
```

Após a correção e o envio (commit/push) do código, o pipeline de CI será executado novamente. Desta vez, o `test_soma` passará, demonstrando um ciclo de CI/CD bem-sucedido.


## Exercício

**Objetivo:** Adicionar uma nova funcionalidade à calculadora, com seu respectivo teste, e demonstrar o funcionamento do pipeline de CI.

**Passos:**

1.  **Crie uma nova feature:**
    *   Abra o arquivo `app/calc.py`.
    *   Adicione uma nova função à calculadora. Sugestão: uma função de potenciação (`potencia(base, expoente)`).

2.  **Adicione um novo teste:**
    *   Abra o arquivo `tests/test_calc.py`.
    *   Adicione um novo teste para a função que você criou. O teste deve verificar se a função retorna o resultado esperado para diferentes entradas.

3.  **Demonstre seu conhecimento em CI:**
    *   Faça o `commit` e o `push` das suas alterações para o seu repositório no GitHub.
    *   Acesse a aba "Actions" do seu repositório.
    *   Tire um print da tela mostrando o workflow de CI sendo executado com sucesso (com um ícone de "check" verde).
    *   Adicione este print ao seu relatório/entrega para comprovar que você completou o exercício e que suas alterações passaram nos testes automatizados.

## Como Entregar o Exercício

A entrega e a comprovação da atividade serão feitas exclusivamente através de um **Pull Request (PR)** a partir de um `fork` deste repositório.

**Passo a Passo:**

1.  **Faça um Fork:**
    *   No canto superior direito da página deste repositório no GitHub, clique no botão **Fork**.
    *   Isso criará uma cópia completa do repositório na sua própria conta do GitHub.

2.  **Clone o Seu Fork:**
    *   Na página do **seu fork**, clique no botão verde **Code** e copie a URL (HTTPS ou SSH).
    *   No seu terminal, execute o comando:
        ```bash
        git clone <URL_DO_SEU_FORK>
        ```

3.  **Crie uma Nova Branch:**
    *   Navegue para o diretório do projeto clonado e crie uma branch para suas alterações:
        ```bash
        cd <NOME_DO_REPOSITORIO>
        git checkout -b minha-nova-feature
        ```

4.  **Realize as Alterações:**
    *   Implemente a nova função na calculadora e adicione o teste, conforme descrito na seção "Exercício".

5.  **Faça o Commit e o Push:**
    *   Adicione e confirme suas alterações:
        ```bash
        git add .
        git commit -m "feat: Adiciona função de potenciação e teste"
        ```
    *   Envie a sua branch para o **seu fork** no GitHub:
        ```bash
        git push origin minha-nova-feature
        ```

6.  **Crie o Pull Request (PR) para Entrega:**
    *   Abra a página do **seu fork** no GitHub.
    *   O GitHub geralmente mostrará um aviso para criar um Pull Request a partir da sua branch recém-enviada. Clique em **Compare & pull request**.
    *   Se o aviso não aparecer, vá para a aba **Pull Requests** e clique em **New pull request**.
    *   Certifique-se de que o `base repository` seja o repositório **original** e o `head repository` seja o **seu fork**.
    *   O `compare` deve ser a sua branch (`minha-nova-feature`) e o `base` deve ser a branch `main` do repositório original.
    *   **No título do Pull Request, coloque seu RA e Nome Completo.** Exemplo: `[123456] Nome Completo do Aluno - Atividade de CI`.
    *   Adicione uma breve descrição para o seu PR, se desejar.
    *   Clique em **Create pull request**.

7.  **Comprovação:**
    *   O próprio Pull Request criado será a sua entrega. Ele conterá o link para o seu código, o histórico de alterações e, o mais importante, o status do workflow de CI (que deverá estar passando com sucesso), comprovando que sua alteração foi testada e integrada corretamente.