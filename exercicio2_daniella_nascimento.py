from plyer import notification

def alerta (nivel, base, etapa):
    message = f"Falha no carregamento da base {base} na etapa {etapa}"
    if nivel == 1:
        title = "Alerta Baixo"
    elif nivel == 2:
        tite = "Alerta Médio"
    else:
        title = "Alerta Alto"
    notification.notify(
       title = title,
       message = message 
    )

# Testando se funcionou:
# alerta (3,"Censo", "Extração")