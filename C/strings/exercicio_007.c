/* Exercício 7

Leia uma cidade usando scanf e imprima:
Você mora em Goiânia */

#include <stdio.h>

int main() {
    char cidade[40];

    printf("Escreva o nome da sua cidade: ");
    scanf("%s", cidade);

    printf("Você mora em %s", cidade);

    return 0;
}