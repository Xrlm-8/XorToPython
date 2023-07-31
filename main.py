# Recebe o arquivo em Byte
byte = b'\x07\x94E\t\x00\xdf\xc4\xd4\xef'
str_decoded = hex(byte) # Transformar em Hexadecimal


# Esse script precisa de manutenção
def calculo_xor(str_decoded):
    index = 0
    array = []
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
user_xor = calculo_xor(str_decoded) # Chamando Calculo XOR para o Evento Socket
hex_chec = user_xor['hex_chec'] # Retorna XOR do Byte
checksum = user_xor['checksum'] # Retorna XOR do Calculo

if(hex_chec == checksum): # Confirma Checksum
    print("Checksum Correto",hex_chec," Corresponde com o calculo >",checksum,"\n")
else:
    print("checksum Incorreto",hex_chec, "Não corresponde com o calculo > ", checksum,"\n")
print ("Continua codigo\n")