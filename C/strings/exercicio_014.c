/* Exercício 14

Leia uma palavra e conte quantas vezes a letra 'a' aparece nela. */

#include <stdio.h>

int main() {
    char palavra[] = "Arara";
    int contadorA = 0, i = 0;

    while (palavra[i] != '\0') {
        if (palavra[i] == 'a') {
            contadorA++;
        }

        i++;
    }

    printf("A palavra tem %d letras a \n", contadorA);

    return 0;
}