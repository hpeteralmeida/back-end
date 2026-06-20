/* Exercício 1

Faça um programa em C que declare uma string chamada nome, 
armazene seu primeiro nome nela e imprima o nome na tela. */

#include <stdio.h>

int main() {
    char nome[50];

    printf("Digite seu primeiro nome: ");
    scanf("%s", &nome);

    printf("Seu nome é: %s\n", nome);

    return 0;
}