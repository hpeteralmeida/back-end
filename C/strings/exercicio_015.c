/* Exercício 15

Leia uma palavra e mostre quantos caracteres ela possui usando strlen(). */

#include <stdio.h>
#include <string.h>

int main() {
    char palavra[] = "String";

    printf("%d", strlen(palavra));

    return 0;
}