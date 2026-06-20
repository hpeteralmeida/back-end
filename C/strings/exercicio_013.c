/* Exercício 13

Leia uma palavra e imprima suas letras separadas por espaço. */

#include <stdio.h>

int main() {
    char palavra[] = "palavra";
    int i = 0;

    while (palavra[i] != '\0') {
        printf("%c ", palavra[i]);
        i++;
    }
    printf("\n");

    return 0;
}