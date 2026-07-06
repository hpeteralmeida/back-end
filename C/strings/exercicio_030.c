/* Exercício 30

Leia uma frase e informe qual vogal aparece mais vezes. */

#include <string.h>
#include <stdio.h>

int main() {
    char frase[200];
    int contA = 0, contE = 0, contI = 0, contO = 0, contU = 0;
    int maior;
    char vogal;

    printf("Digite uma frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        switch (frase[i]) {
            case 'A':
            case 'a':
                contA++;
                break;

            case 'E': 
            case 'e':
                contE++;
                break;

            case 'I': 
            case 'i':
                contI++;
                break;
            
            case 'O': 
            case 'o':
                contO++;
                break;
            
            case 'U':
            case 'u':
                contU++;
                break;
        }
    }

    maior = contA;
    vogal = 'A';

    if (contE > maior) {
        maior = contE;
        vogal = 'E';
    } else if (contI > maior) {
        maior = contI;
        vogal = 'I';
    } else if (contO > maior) {
        maior = contO;
        vogal = 'O';
    } else if (contU > maior) {
        maior = contU;
        vogal = 'U';
    }

    printf("A vogal que mais aparece é a letra '%c' com %d ocorrências\n", vogal, maior);

    return 0;
}