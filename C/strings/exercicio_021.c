/* Exercício 21

Leia uma palavra e informe quantas vezes a letra 'e' aparece. */

#include <stdio.h>

int main() {
    char palavra[50];
    int contadorE = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    for (int i = 0; palavra[i] != '\0'; i++) {
        if (palavra[i] == 'e' || palavra[i] == 'E') {
            contadorE++;
        }
    }

    printf("A letra 'e' aparece %d vezes na palavra.\n", contadorE);

    return 0;
}