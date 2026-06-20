/* Exercício 2

Faça um programa em C que declare uma string 
com o nome de uma cidade e imprima a frase:

Cidade informada: Goiânia */

#include <stdio.h>

int main() {
    char cidade[50];

    printf("Digite o nome de uma cidade: ");
    scanf("%s", &cidade);

    printf("Cidade informada: %s\n", cidade);

    return 0;
}
