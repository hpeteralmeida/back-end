/* Exercício 22

Leia uma frase e informe quantos espaços existem nela. */

#include <stdio.h>

int main() {
    char frase[100];
    int contadorEspacos = 0;

    printf("Digite uma frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        if (frase[i] == ' ') {
            contadorEspacos++;
        }
    }

    printf("A frase tem %d espaços.\n", contadorEspacos);

    return 0;
}