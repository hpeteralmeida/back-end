/* Exercício 29

Leia uma frase e informe:
    quantidade de vogais
    quantidade de espaços */

#include <stdio.h>
#include <string.h>

int main() {
    char frase[200];
    int contVogais = 0, contEspaco = 0;

    printf("Digite uma frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        if (frase[i] == 'A' || frase[i] == 'a' ||
            frase[i] == 'E' || frase[i] == 'e' ||
            frase[i] == 'I' || frase[i] == 'i' ||
            frase[i] == 'O' || frase[i] == 'o' ||
            frase[i] == 'U' || frase[i] == 'u') {
                contVogais++;
            } else {
                if (frase[i] == ' ') {
                    contEspaco++;
                }
            }
    }

    printf("Vogais: %d\n", contVogais);
    printf("Espaços: %d\n", contEspaco);

    return 0;
}