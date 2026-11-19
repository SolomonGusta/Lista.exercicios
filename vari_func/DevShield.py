projeto = "LearnHub EdTech"
modulo = "Emissão de Certificado e Validação de Notas"
responsavel = "Gabriel Souza"
data_execucao = "10/11/2026"
testes_aprovados = 28
testes_reprovados = 14
testes_nao_executados = 8

print("======================================== RELATÓRIO DE EXECUÇÃO DE TESTES ======================================== ")
print("Projeto: " + projeto)
print("Módulo:" + modulo)
print("Responsável: " + responsavel)
print("Data: " + data_execucao)

print("---------------------------------------- RESULTADOS REGISTRADOS ------------------------------------------------ ")
print("Aprovados: " + str(testes_aprovados))
print("Reprovados: " + str(testes_reprovados))
print("Não Executados: " + str(testes_nao_executados))

print("---------------------------------------- MÉTRICAS DA EXECUÇÃO ---------------------------------------- ")
total_testes = testes_aprovados + testes_reprovados + testes_nao_executados
print("Total de Testes: " + str(total_testes))
testes_executados = testes_aprovados + testes_reprovados
print("Testes Executados: " + str(testes_executados))

taxa_aprovacao = (testes_aprovados / total_testes)*100
print("Taxa de Aprovação: " + str(taxa_aprovacao)+ "%")
taxa_reprovacao = (testes_reprovados / total_testes)*100
print("Taxa de Reprovados: " + str(taxa_reprovacao)+ "%")
taxa_nao_executados = (testes_nao_executados / total_testes)*100
print("Taxa de Reprovados: " + str(taxa_nao_executados)+ "%") 
print("---------------------------------------- CÁLCULOS CONCLUÍDOS ---------------------------------------- ")