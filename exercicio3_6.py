materia1 = float(input("Informe a Media da Primeira materia: "))
materia2 = float(input("Informe a Madia da Segunda materia: "))
materia3 = float(input("Informe a Media da Terceira materia: "))

if materia1 < 7 or materia2 < 7 or materia3 < 7:
	print("Aluno Nao Aprovado")
else:
	print("Aluno Aprovado")