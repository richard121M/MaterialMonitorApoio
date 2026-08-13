#mostrar um texto na tela:
print("Ola mundo")

idade = 12

#mostra um texto junto com um valor na tela:
print("idade e igual a",idade,"anos")
#com fstring
print(f'idade e igual a {idade} anos')

#OBS: ao se utilizar as virgulas nao e necessario colocar
#o espacamento

#tag sep
    #mostra um texto junto com um valor na tela sem espacamento:
print("idade e igual a",idade,"anos",sep="")

#tag end
#a tag end serve para a acao que o print ira fazer apois 
#mostra o texto, no padrao ele faz a quebra de linha
print("print SEM a tag end:")
print("abc")
print("def")

print("print COM a tag end:")
print("abc",end="")
print("def")

