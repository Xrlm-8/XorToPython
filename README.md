# CalculoXorForPython
<h1 >Calculadora XOR em Python </h1>
<p>Vamos começar recebendo meus dados, em bytes, após transformar em hexadecimal, vamos colocar em um array</p> <br>

<code>
while index < len(str_decoded):
    percorre = slice(index,index + 2)
    res = str_decoded[percorre]
    index = index + 2
    array.append(int(res, base=16))
pegar_checksum = array.pop()
hex_chec = hex(pegar_checksum)

def calcXor(array):
    res = 0
    i = 0
    while i < len(array):
        res = res ^ array[i]
        i = i + 1
    return res
res = calcXor(array)
check = res ^ 0xff
checksum = hex(check)
var = {
    'hex_chec': hex_chec,
    'checksum': checksum
}
return var
</code>
<br>
<h2>Vamos instaciar a função me variaveis agora...</h2>

<code>
user_xor = calculo_xor(str_decoded) # Chamando Calculo XOR para o Evento Socket
hex_chec = user_xor['hex_chec'] # Retorna XOR do Byte
checksum = user_xor['checksum'] # Retorna XOR do Calculo
</code>
<br>

<p>Fazendo a verificação do Checksum</p><br>

<code>
if(hex_chec == checksum): # Confirma Checksum
    print("Checksum Correto",hex_chec," Corresponde com o calculo >",checksum,"\n")
else:
    print("checksum Incorreto",hex_chec, "Não corresponde com o calculo > ", checksum,"\n")
print ("Continua codigo\n")
</code>
