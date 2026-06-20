/* Exercício 11

Leia uma palavra e imprima cada caractere em uma linha diferente. */

#include <stdio.h>

int main() {
    char palavra[50];
    int i = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    while(palavra[i] != '\0') {
        printf("%c\n", palavra[i]);
        i++;
    }

    return 0;
}