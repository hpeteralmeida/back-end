Aula 1 — O que é uma string em C 

Em C, uma string é um vetor de caracteres.

Exemplo:
char nome[20] = "Pedro";

Por dentro, o C guarda assim:
P e d r o \0
O \0 indica o fim da string.

Ou seja, a string "Pedro" tem 5 letras, mas ocupa 6 posições no vetor:
nome[0] = 'P'
nome[1] = 'e'
nome[2] = 'd'
nome[3] = 'r'
nome[4] = 'o'
nome[5] = '\0'

Por isso, sempre que criar uma string, precisa deixar espaço para o \0.

Exemplo correto:
char palavra[6] = "Pedro";

Exemplo perigoso:
char palavra[5] = "Pedro";
Porque não sobra espaço para o \0.

Exemplo básico
#include <stdio.h>

int main() {
    char nome[20] = "Pedro";

    printf("%s\n", nome);

    return 0;
}

Para imprimir uma string, usamos:
%s

Para imprimir um único caractere, usamos:
%c

Exemplo:
printf("%c", nome[0]);
Isso imprime:
P

Exercicios 1 - 5