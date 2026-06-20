/* Exercício 6

Leia o nome do usuário usando scanf e imprima:
Ola, nome! */

#include <stdio.h>

int main() {
    char nome[10];

    printf("Escreva o seu nome");
    scanf("%s", nome);

    printf("Olá, %s", nome);
    
    return 0;
}