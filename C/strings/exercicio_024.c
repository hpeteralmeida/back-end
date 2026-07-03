/* Exercício 24

Leia uma frase e informe quantas letras 'a' ou 'A' existem. */

#include <stdio.h>
#include <string.h>

int main() {
    char frase[50];
    int contador = 0;

    printf("Digite uma frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        if (frase[i] == 'a' || frase[i] == 'A') {
            contador++;
        }
    }

    printf("A quantidade de letras A foi: %d\n", contador);

    return 0;
}