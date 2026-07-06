/* Exercício 28

Leia uma frase e conte quantos caracteres existem sem considerar os espaços. */

#include <stdio.h>
#include <string.h>

int main() {
    char frase[200];
    int contadorCaracteres = 0;

    printf("Digite uma frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        if (frase[i] != ' ' && frase[i] != '\n') {
            contadorCaracteres++;
        }
    }

    printf("A frase tem %d caracteres (sem contar os espaços).\n", contadorCaracteres);

    return 0;
}
