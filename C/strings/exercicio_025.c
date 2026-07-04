/*Exercício 25

Leia uma palavra e conte quantas letras NÃO são 'a'. */

#include <stdio.h>
#include <string.h>

int main() {
    char palavra[100];
    int contaLetras = 0;

    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    for (int i = 0; palavra[i] != '\0'; i++) {
        if (palavra[i] != 'a' && palavra[i] != 'A') {
            contaLetras++;
        }
    }

    printf("Quantidade de letras que não são 'a': %d\n", contaLetras);
    return 0;
}