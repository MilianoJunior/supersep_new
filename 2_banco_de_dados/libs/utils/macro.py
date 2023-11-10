'''
sub int persistir()

int status, control, status_control, error_code, erro
GetData(status,"SuperSEP",LW,6000,1)

if status == 2 then
control = 1
SetData(control,"SuperSEP",LW,6050,1)
GetData(error_code,"SuperSEP",LW,6053,1)
if error_code == 0 then
TRACE("SALVO com sucesso")
return error_code
else
TRACE("ERRO: %d", error_code)
return error_code
end if
else
erro = 2
SetData(erro, "SuperSEP",LW,6005,1)
TRACE("Erro de conexão")
return erro
end if
end sub
macro_command main()
//---------------------------------------------------
// Descrição: Executa o comando de .
// pagina: 49: _Eng_UG01_SetPoints
// Junior 06/06/2022
//--------------------------------------------------
// Declaração das variáveis
int id, a, count
// 1- Iniciar o banco de dados
count = 0
a = 1
while a > 0
    count = count + 1
    id = 1
    TRACE("1 - EXECUTANDO BANCO DE DADOS ONLINE, count %d", count)
    SetData(id,"SuperSEP",LW,6005,1)
    DELAY(3000)
    a = persistir()
    TRACE("A: %d", a)
wend
id = 2
SetData(id,"SuperSEP",LW,6005,1)
TRACE("Finalizando- PERSISTIDO DB ONLINE ")

end macro_command
'''