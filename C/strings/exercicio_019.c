/* Exercício 19

Leia uma palavra e crie outra string contendo uma cópia dela.
Depois mostre:
    Original: banana
    Copia: banana

Use strcpy(). */

#include <stdio.h>
#include <string.h>

int main() {
    char palavra[50], copia[50];

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    strcpy(copia, palavra);

    printf("Original: %s\n", palavra);
    printf("Copia: %s\n", copia);

    return 0;
}