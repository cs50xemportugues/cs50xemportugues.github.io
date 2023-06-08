Uso
---

Seu programa deve se comportar como nos exemplos abaixo. `INFILE.bmp` é o nome da imagem de entrada e `OUTFILE.bmp` é o nome da imagem resultante após a aplicação de um filtro.

```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
```

Dicas
---

*   Os valores dos componentes `rgbtRed`, `rgbtGreen` e `rgbtBlue` de um pixel são todos números inteiros. Certifique-se de arredondar quaisquer números de ponto flutuante para o inteiro mais próximo ao atribuí-los a um valor de pixel!

Testando
--------

Certifique-se de testar todos os seus filtros nos arquivos de bitmap de amostra fornecidos!

Execute o comando abaixo para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo também!

    check50 cs50/problems/2023/x/filter/more
    

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    style50 helpers.c
    

Como Enviar
-----------

No terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2023/x/filter/more