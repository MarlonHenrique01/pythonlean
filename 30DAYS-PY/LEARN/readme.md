on this file, i will post my codes that i made, feel free to help.

Reverse Game é um pequeno jogo feito em Python que verifica se uma palavra é um palíndromo — ou seja, uma palavra que continua igual quando lida de trás para frente.

O programa funciona da seguinte forma:

Exibe o título do jogo no terminal.
Pede para o usuário digitar uma palavra.
Inverte a palavra usando string slicing ([::-1]).
Compara a palavra original com a palavra invertida.
Se forem iguais → mostra uma mensagem de parabéns.
Se forem diferentes → informa que a palavra não é um palíndromo.
Exemplos de palavras válidas (palíndromos)

✅ ana → ana
✅ ovo → ovo
✅ osso → osso
✅ arara → arara
✅ reviver → reviver
✅ radar → radar
✅ salas → salas
✅ mirim → mirim
✅ natan → natan
✅ subinusibus → subinusibus

Exemplos de palavras que NÃO funcionam

❌ casa → asac
❌ python → nohtyp
❌ github → buhtig
❌ computador → rodatupmoc
