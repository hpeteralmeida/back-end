/*Exercício 3

Leia o nome completo do usuário usando fgets e imprima:
Nome completo: nome sobrenome */

#include <stdio.h>

int main() {
    char nome[100];

    printf("Escreva o seu nome completo: ");
    fgets("%s", sizeof(nome), stdin);

    printf("nome completo: %s", nome);

    return 0;
}
