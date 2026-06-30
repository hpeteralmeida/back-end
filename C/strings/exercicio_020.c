/* Exercício 20

Leia uma palavra e informe quantas vezes a letra 'a' aparece. */

#include <stdio.h>

int main() {
    char palavra[50];
    int contadorA = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    for (int i = 0; palavra[i] != '\0'; i++) {
        if (palavra[i] == 'a' || palavra[i] == 'A') {
            contadorA++;
        }
    }

    printf("A letra 'a' aparece %d vezes na palavra.\n", contadorA);

    return 0;
}