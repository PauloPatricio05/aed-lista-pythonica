def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
   # Encontrarei a posição de quem não pode vir
    indice = guests.index(unavailable)
    
    # Colocando o novo convidado exatamente na mesma posição
    guests[indice] = new_guest
    
    return guests
