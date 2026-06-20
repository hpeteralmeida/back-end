Aula 2 — Lendo strings do teclado

Até agora você estava escrevendo a string diretamente no código:
char nome[50] = "Pedro";

Mas normalmente o usuário vai digitar a informação.

1. Lendo com scanf
    Exemplo:
    #include <stdio.h>

    int main() {
        char nome[50];

        printf("Digite seu nome: ");
        scanf("%s", nome);

        printf("Nome: %s\n", nome);

        return 0;
    }

    Entrada:
    Pedro

    Saída:
    Nome: Pedro

    Problema do scanf
    Se o usuário digitar "Pedro Almeida",  o programa salva apenas:

    "Pedro"

    Porque %s para quando encontra um espaço.

2. Lendo com fgets
    Para nomes completos, frases e textos usamos fgets()

    Exemplo:
    #include <stdio.h>

    int main() {
        char nome[50];

        printf("Digite seu nome: ");
        fgets(nome, 50, stdin);

        printf("%s", nome);

        return 0;
    }

    Entrada:
    Pedro Almeida

    Saída:
    Pedro Almeida

    Como funciona o fgets
    fgets(nome, 50, stdin);

    Significa:
    guardar em nome no máximo 49 caracteres lendo do teclado (stdin)

    Problema do fgets
    Quando o usuário aperta ENTER, o ENTER também é salvo.

    Exemplo:
    Entrada:
    Pedro

    Na memória fica:
    Pedro\n

    Por isso às vezes aparecem linhas extras.
    Mais pra frente aprenderemos a remover esse \n.

3. Lendo várias palavras

    Exemplo:
        char frase[100];
        fgets(frase, 100, stdin);
        printf("%s", frase);

    Entrada:
    Eu gosto de programar

    Saída:
    Eu gosto de programar

sizeof() x strlen()

- o sizeof() mostra o tamanho do vetor sendo a mesma coisa de escrever apenas o seu tamanho,
com a diferenca de que ele atualiza a mudanca de tamanho do vetor automaticamente
    fgets(frase, 100, stdin); -> precisa mudar o tamanho do vetor manualmente
    fgets(frase, sizeof(frase), stdin); -> altera o tamanho do vetor de forma automatica

- o strlen() retorna o numero de caracteres armazenados no vetor, sem contar o \0
    char nome[10] = "Joao";

    sizeof(nome): 10 -> mostra o tamanho completo do vetor com os caracteres vazios
    strlen(nome): 4 -> mostra a quantidade de caracteres salvos 

- em caso de o tamanho do vetor nao ser declarado:
    char nome[] = "Joao"

    o sizeof() automaticamente conta o numero de caracteres necessarios mais o \0. exemplo:

    sizeof(nome): 5 (J o a o \0)
    strlen(nome): 4 




exercicios 6 - 8