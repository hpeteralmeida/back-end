/* Exercício 5

Faça um programa em C que declare uma string com seu nome e imprima:

Meu nome é _____
A primeira letra do meu nome é _ */

#include <stdio.h>

int main () {
    char nome[20];

    printf("Escreva o seu nome: ");
    scanf("%s", nome);

    printf("Seu nome é %s \n", nome);
    printf("A primeira letra do seu nome é %c \n", nome[0]);

    return 0;
}