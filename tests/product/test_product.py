from inventory_report.inventory.product import Product


def test_cria_produto():
    product1 = Product(1, 'site', 'Vjcompany', '2023-04-04', '2025-04-04',
                       '0001', 'Git Hub')
    assert product1.id == 1
    assert product1.nome_da_empresa == 'Vjcompany'
    assert product1.nome_do_produto == 'site'
    assert product1.data_de_fabricacao == '2023-04-04'
    assert product1.data_de_validade == '2025-04-04'
    assert product1.numero_de_serie == '0001'
    assert product1.instrucoes_de_armazenamento == 'Git Hub'
