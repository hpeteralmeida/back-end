/* Exercício 26

Leia uma frase e conte quantas vogais existem. */

#include <stdio.h>
#include <string.h>

int main() {
    char frase[200];
    int contadorVogais = 0;

    printf("Digite uma frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        char letra = frase[i];
        if (letra == 'a' || letra == 'A' ||
            letra == 'e' || letra == 'E' ||
            letra == 'i' || letra == 'I' ||
            letra == 'o' || letra == 'O' ||
            letra == 'u' || letra == 'U') {
            contadorVogais++;
        }
    }

    printf("A frase tem %d vogais.\n", contadorVogais);

    return 0;
}