Aula 3 — Percorrendo uma string caractere por caractere

Considere:
    char nome[] = "Pedro";

Na memória:
    Índice:  0 1 2 3 4 5
    Valor :  P e d r o \0

Podemos acessar cada posição:
    printf("%c\n", nome[0]);
    printf("%c\n", nome[1]);
    printf("%c\n", nome[2]);

Saída:
    P
    e
    d

Usando um laço, em vez de escrever uma linha para cada letra:
    for(int i = 0; i < 5; i++) {
        printf("%c\n", nome[i]);
    }

Saída:
    P
    e
    d
    r
    o

Percorrendo até o final da string, o tamanho pode variar.
Então usamos o \0 como sinal de parada:
    int i = 0;

    while(nome[i] != '\0') {
        printf("%c\n", nome[i]);
        i++;
    }

Isso funciona para qualquer tamanho de string.

Exemplo importante:
Contar quantas letras existem:
    int contador = 0;

    while(nome[contador] != '\0') {
        contador++;
    }

    printf("%d", contador);

Resultado: 5

Esse é basicamente o que a função strlen() faz internamente.

exercicios 9 - 14