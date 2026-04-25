"""
O Inspetor da Qualidade não olha apenas uma medida.
Se o diâmetro estiver bom, ele ainda precisa conferir o comprimento da peça.
Vamos criar um código que simula um robô de inspeção que faz múltiplas
checagens antes de aprovar um lote.
"""

# =======================================================================
# ROBÔ DE INSPEÇÃO DE QUALIDADE
# =======================================================================
print("=" * 50)
print("🤖 SISTEMA DE METROLOGIA AUTOMATIZADA")
print("=" * 50)

# Parâmetros ideias de projeto
diametro_ideal = 50.0  # mm
comp_ideal = 120.0  # mm
tolerancia = 0.2  # mm para mais ou para menos

# Coletando as medidas reais da peça recém-usinada
diametro_real = float(input("Leitura do Micrômetro - Diâmetro (mm):"))
comp_real = float(input("Leitura do Paquímetro - Comprimento (mm):"))

print("=" * 50)
print("Analizando tolerâncias...")

# 1ª Barreira de Verificação: 0 Diâmetro está dentro do limite?
if (diametro_real >= diametro_ideal - tolerancia) and (
    diametro_real <= diametro_ideal + tolerancia
):
    print("✔️ Diâmetro: APROVADO.")

    if (comp_real >= comp_ideal - tolerancia) and (
        comp_real <= comp_ideal + tolerancia
    ):
        print("✔️ Comprimento: APROVADO.")
        print("=" * 50)
        print("🟢 Status Final: PEÇA 100% APROVADA. ENVIAR PARA MONTAGEM.")

    elif comp_real > comp_ideal + tolerancia:
        print("❌ Comprimento: REPROVADO (Muito Longo).")
        print("=" * 50)
        print("🟡 Status Final: RETRABALHO. VOLTAR PEÇA PARA A FRESA.")
    else:
        print("❌ Comprimento: REPROVADO (Muito Curto).")
        print("=" * 50)
        print("🔴 Status Final: REFUGO. PEÇA PERDIDA.")

        # Se já reprovou logo de cara na 1a barreira (Diâmetro):
else:
    print("❌ Diâmetro: REPROVADO.")
    # Se o diâmetro já está ruim, nem perdemos tempo medindo comprimento
    if diametro_real > diametro_ideal + tolerancia:
        print(
            "🟡 Status Final: RETRABALHO. VOLTAR PARA O PASSE DE ACABAMENTO NO TORNO."
        )
    else:
        print("🔴 Status Final: REFUGO. DIÂMETRO ABAIXO DA MEDIDA, PERDA TOTAL.")
    print("=" * 50)
