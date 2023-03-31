from controle_parcelamento.models import Parcelas


def check_parcelas_status(parcela: Parcelas) -> bool:

    '''
    Recebe uma instancia de Parcelas e verifica se todas as parcelas da mesma 
    venda ja foram pagas(status='Pago'), se sim, atualiza o status da venda para
    Concluido.
    '''

    venda = parcela.venda
    parcelas_venda = Parcelas.objects.filter(
        num_pedido=parcela.num_pedido,
        nome_cliente=parcela.nome_cliente,
        venda=venda
    )
    parcelas_pagas = parcelas_venda.filter(status='Pago')
    if parcelas_pagas.count() == venda.qnt_parcelas:
        venda.status_venda = 'Concluido'
        venda.save()
        return True
    else:
        return False