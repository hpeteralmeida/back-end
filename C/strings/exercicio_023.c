/* Exercício 23

Leia uma palavra e informe quantas vogais ela possui. */

#include <stdio.h>

int main() {
    char palavra[50];
    int contadorVogais = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    for (int i = 0; palavra[i] != '\0'; i++) {
        char letra = palavra[i];
        if (letra == 'a' || letra == 'A' ||
            letra == 'e' || letra == 'E' ||
            letra == 'i' || letra == 'I' ||
            letra == 'o' || letra == 'O' ||
            letra == 'u' || letra == 'U') {
            contadorVogais++;
        }
    }

    printf("A palavra tem %d vogais.\n", contadorVogais);

    return 0;
}