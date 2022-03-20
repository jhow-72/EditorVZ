from FilaVZ import FilaVZ

############# TESTES #############
# fila = 'Nam quis nulla. Integer malesuada. In in enim a arcu imperdiet malesuada. Sed vel lectus. Donec odio urna, tempus molest01798orttitor u123456789012345, sem. Phasellus rhoncus. Aenean id metus id velit ullamcorper pulvinar. Vestibulum fermentum tortor id mi. Pellentesque ipsum. Nulla non arcu lacinia neque faucibus fringilla. Nulla non lectus sed nisl molestie malesuada. Proin in tellus sit amet nibh dignissim sagittis. Vivamus luctus egestas leo. Maecenas sollicitudin. Nullam rhoncus aliquam metus. Etiam egestas wiDFD3DC1640F63B6D369um dolor sit amet, consectetuer adipiscing elit. Nullam feugiat, turpis atxas'

fila = '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# print(fila)

filaVZ = FilaVZ(fila)
print(f'fila inicial:\t\t{filaVZ._fila}')

# # # Teste do chpras
# # print(f'CHPRAS:\t{filaVZ.chpras}')
# # filaVZ.chpras_replace('73815')
# # print(f'CHPRAS:\t{filaVZ.chpras}')
# #
# # print(f'Fila atualizada:\t{filaVZ._fila}')
# #
# # # Teste da data
# # print(f'data:\t{filaVZ.data_transacao}')
# # filaVZ.data_transacao_replace('2019-08-27')
# # print(f'data:\t{filaVZ.data_transacao}')
# #
# # print(f'Fila atualizada:\t{filaVZ._fila}')
# #
# # # Teste da hora
# # print(f'hora:\t{filaVZ.hora_transacao}')
# # filaVZ.hora_transacao_replace('12:32:41')
# # print(f'hora:\t{filaVZ.hora_transacao}')
# #
# # # Teste do CPF
# # print(f'Numero Documento original:\t\t{filaVZ.numero_documento}')
# # filaVZ.numero_documento_replace('000044024873822')
# # print(f'Numero Documento atualizado:\t{filaVZ.numero_documento}')
# #
# # print(f'Fila atualizada:\t{filaVZ._fila}')
# #
# # # Teste da HASH do cartão
# # # DFD3DC1640F63B6D369
# # # F28BE31DBAE83DB283B
# # print(f'hash cartão original:\t{filaVZ.hash_cartao}')
# # filaVZ.hash_cartao_replace('F28BE31DBAE83DB283B')
# # print(f'hash cartão atualizada:\t{filaVZ.hash_cartao}')
# #
# # print(f'Fila atualizada:\t{filaVZ._fila}')
# #
# # # Teste da DN
# # print(f'DN original:\t{filaVZ.dn}')
# # filaVZ.dn_replace('72')
# # print(f'DN atualizada:\t{filaVZ.dn}')
# #
# # print(f'Fila atualizada:\t{filaVZ._fila}')
# #
# # # Teste do valor transacao
# # print(f'valor transacao:\t{filaVZ.valor_transacao}')
# # filaVZ.valor_transacao_replace('2032')
# # print(f'valor transacao:\t{filaVZ.valor_transacao}')
# #
# # print(f'Fila atualizada:\t{filaVZ._fila}')
# #
# # # Teste nome estab
# # print(f'Nome Estabelecimento:\t{filaVZ.nome_estabelecimento}')
# # filaVZ.nome_estabelecimento_replace('POSTO SAO SEBASTIAO')
# print(f'Nome Estabelecimento:\t{filaVZ.nome_estabelecimento}')


filaVZ.chpras_replace('73815489')
filaVZ.data_transacao_replace('2019-08-27')
filaVZ.hora_transacao_replace('12:32:41')
filaVZ.dn_replace('1872')
filaVZ.indicador_cartao_virtual_replace('N')
filaVZ.CF_replace('51')
filaVZ.numero_documento_replace('000044024873822')
filaVZ.indic_titularidade_replace('0')
filaVZ.nome_estabelecimento_replace('POSTO SAO SEBASTIAO')
filaVZ.tipo_pessoa_replace('F')
filaVZ.valor_transacao_replace('000000000727272')
filaVZ.hash_cartao_replace('F28BE31DBAE83DB283B')


# print(f'fila original:\t\t{fila}')
print(f'Fila atualizada:\t{filaVZ._fila}')



