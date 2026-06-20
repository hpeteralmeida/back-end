/* Exercício 3

Faça um programa em C que declare uma string com uma palavra 
qualquer e imprima apenas a primeira letra dessa palavra. */

#include <stdio.h>

int main() {
    char palavra[50];

    printf("Digite uma palavra: ");
    scanf("%s", &palavra);

    printf("A primeira letra da palavra é: %c\n", palavra[0]);

    return 0;
}