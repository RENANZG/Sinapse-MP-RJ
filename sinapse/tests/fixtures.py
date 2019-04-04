import responses


request_node_ok = {
    'statements': [
        {
            'statement': 'MATCH  (n) where id(n) = 395989945 return n',
            'resultDataContents': [
                'row',
                'graph'
            ]
        }
    ]
}

resposta_node_ok = {
    'nodes': [
        {
            'id': '395989945',
            'type': ['personagem'],
            'label': 'Label de Teste',
            'properties': {
                'cpf': '11452244740',
                'nome': 'DANIEL CARVALHO BELCHIOR',
                'pess_dk': 15535503
            }
        }],
    'edges': []
}

resposta_node_sensivel_ok = {
    'nodes': [
        {
            'id': '395989945',
            'type': ['personagem'],
            'label': 'Label de Teste',
            'properties': {
                'cpf': '11452244740',
                'nome': 'DANIEL CARVALHO BELCHIOR',
                'pess_dk': 15535503,
                'sensivel': True
            }
        }],
    'edges': []
}

nos_sensiveis_esp = [
        {
            'id': '395989945',
            'labels': ['sigiloso'],
            'properties': {
            }
        }
]


relacoes_sensiveis = [{
    'id': '282346165',
    'type': 'filho',
    'startNode': '12075099',
    'endNode': '10844320',
    'properties': {'sensivel': True},
    }]

relacoes_sensiveis_esp = [{
    'id': '282346165',
    'type': 'sigiloso',
    'startNode': '12075099',
    'endNode': '10844320',
    'properties': {},
    }]

resposta_node_sensivel_esp = {
    'nodes': [
        {
            'id': '395989945',
            'type': ['sigiloso'],
            'label': 'Label de Teste',
            'properties': {}
        }],
    'edges': []
}


request_filterNodes_ok = {
    'statements': [
        {'statement': "MATCH (n: pessoa { "
         "nome:toUpper('DANIEL CARVALHO BELCHIOR')}) return n limit 100",
         'resultDataContents': [
             'row',
             'graph'
         ]
         }
    ]
}


resposta_filterNodes_ok = {
    'nodes': [{
        'id': '140885160',
        'type': ['pessoa'],
        'label': 'Label de Teste',
        'properties': {
            'cpf': '11452244740',
            'dt_nasc': '19850522',
            'filho_rel_status': 1,
            'filho_rel_status_pai': 1,
            'nome': 'DANIEL CARVALHO BELCHIOR',
            'nome_mae': 'MARTA CARVALHO BELCHIOR',
            'nome_pai': 'FRANCISCO IVAN FONTELE BELCHIOR',
            'nome_rg': 'DANIEL CARVALHO BELCHIOR',
            'rg': '131242950',
            'sexo': '1',
            'uf': 'RJ',
            'visitado': False,
        }
    }],
    'edges': []
}

request_nextNodes_ok = {
    'statements': [
        {
            'statement': 'MATCH r = (n)-[*..1]-(x) '
            'where id(n) = 395989945 return r,n,x limit 100',
            'resultDataContents': ['row', 'graph']}
    ]
}

resposta_nextNodes_ok = {
    'nodes': [
        {
            'id': '395989945',
            'type': ['personagem'],
            'label': 'Label de Teste',
            'properties': {
                'cpf': '11452244740',
                'nome': 'DANIEL CARVALHO BELCHIOR',
                'pess_dk': 15535503
            }
        },
        {
            'id': '359754850',
            'type': ['mgp'],
            'label': 'Label de Teste',
            'properties': {
                'cdorgao': 400749,
                'classe': 'Notícia de Fato',
                'docu_dk': 17430731,
                'dt_cadastro': '12/01/2018 15:46:42',
                'nr_mprj': 201800032105
            }
        },
        {
            'id': '140885160',
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'cpf': '11452244740',
                'dt_nasc': '19850522',
                'filho_rel_status': 1,
                'filho_rel_status_pai': 1,
                'nome': 'DANIEL CARVALHO BELCHIOR',
                'nome_mae': 'MARTA CARVALHO BELCHIOR',
                'nome_pai': 'FRANCISCO IVAN FONTELE BELCHIOR',
                'nome_rg': 'DANIEL CARVALHO BELCHIOR',
                'rg': '131242950',
                'sexo': '1',
                'uf': 'RJ',
                'visitado': False
            }
        }
    ],
    'edges': [
        {
            'to': '359754850',
            'id': '256806410',
            'properties': {
                'papel': 'NOTICIANTE'
            },
            'from': '395989945',
            'arrows': 'to',
            'dashes': False,
            'label': 'personagem'
        },
        {
            'to': '395989945',
            'id': '277481565',
            'properties': {
                'papel': 'NOTICIANTE'
            },
            'from': '140885160',
            'arrows': 'to',
            'dashes': False,
            'label': 'personagem'
        }
    ]
}


resposta_sensivel_mista = {
    'nodes': [
        {
            'id': '85604696', 
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '0004',
                'cpf': '0004',
                'filho_rel_status': 1,
                'filho_rel_status_pai': 8,
                'nome_mae': 'M H P R',
                'nome': 'N R P',
                'sexo': '2',
                'nome_rg': 'N R P',
                'dt_nasc': '20180709',
            }
        }, 
        {
            'id': '10844320', 
            'type': ['pessoa'],
            'label': 'Label de Teste', 
            'properties': {
                'uf': 'RJ',
                'cpf': '005',
                'nome_mae': 'H M P',
                'nome': 'M H P R',
                'sensivel': True,
                'sexo': '2',
                'dt_nasc': '20180709'
            }
        },
        {
            'id': '12075099', 
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '008',
                'cpf': '008',
                'filho_rel_status': 1,
                'filho_rel_status_pai': 8,
                'nome_mae': 'M H P R',
                'nome': 'A P R',
                'sensivel': True,
                'sexo': '1',
                'nome_rg': 'A P R',
                'dt_nasc': '20180709',
            }
        },
        {
            'id': '57161336', 
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '011',
                'cpf': '011',
                'filho_rel_status': 1,
                'filho_rel_status_pai': 8,
                'nome_mae': 'M H P R',
                'nome': 'S P R',
                'sexo': '1',
                'nome_rg': 'S P R',
                'dt_nasc': '20180709',
            }
        },
        {
            'id': '116929750', 
            'type': ['pessoa'],
            'label': 'Label de Teste', 
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '016',
                'cpf': '016',
                'filho_rel_status_pai': 8,
                'filho_rel_status': 1,
                'nome_mae': 'M H P R',
                'nome': 'M T R DE A',
                'sexo': '2',
                'nome_rg': 'M T R DE A',
                'dt_nasc': '20180709',
            }
        }
    ], 
    'edges': [
        {
            'id': '282236618',
            'label': 'filho',
            'from': '85604696',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {}
        },
        {
            'id': '282346165',
            'label': 'filho',
            'from': '12075099',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {'sensivel': True},
        },
        {
            'id': '286160836',
            'label': 'filho',
            'from': '57161336',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {},
        },
        {
            'id': '288798795',
            'label': 'filho',
            'from': '116929750',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {},
        }
    ]
}

resposta_sensivel_mista_esp = {
    'nodes': [
        {
            'id': '85604696', 
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '0004',
                'cpf': '0004',
                'filho_rel_status': 1,
                'filho_rel_status_pai': 8,
                'nome_mae': 'M H P R',
                'nome': 'N R P',
                'sexo': '2',
                'nome_rg': 'N R P',
                'dt_nasc': '20180709',
            }
        }, 
        {
            'id': '10844320', 
            'type': ['sigiloso'],
            'label': 'Label de Teste', 
            'properties': {}
        },
        {
            'id': '12075099', 
            'type': ['sigiloso'],
            'label': 'Label de Teste',
            'properties': {}
        },
        {
            'id': '57161336', 
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '011',
                'cpf': '011',
                'filho_rel_status': 1,
                'filho_rel_status_pai': 8,
                'nome_mae': 'M H P R',
                'nome': 'S P R',
                'sexo': '1',
                'nome_rg': 'S P R',
                'dt_nasc': '20180709'
            }
        },
        {
            'id': '116929750', 
            'type': ['pessoa'],
            'label': 'Label de Teste',
            'properties': {
                'uf': 'RJ',
                'nome_pai': 'E P R',
                'rg': '016',
                'cpf': '016',
                'filho_rel_status_pai': 8,
                'filho_rel_status': 1,
                'nome_mae': 'M H P R',
                'nome': 'M T R DE A',
                'sexo': '2',
                'nome_rg': 'M T R DE A',
                'dt_nasc': '20180709'
            }
        }
    ], 
    'edges': [
        {
            'id': '282236618',
            'label': 'filho',
            'from': '85604696',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {}
        },
        {
            'id': '282346165',
            'label': 'sigiloso',
            'from': '12075099',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {}
        },
        {
            'id': '286160836',
            'label': 'filho',
            'from': '57161336',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {}
        },
        {
            'id': '288798795',
            'label': 'filho',
            'from': '116929750',
            'to': '10844320',
            'arrows': 'to',
            'dashes': False,
            'properties': {}
        }
    ]
}


request_nodeproperties_ok = {
    'query': 'MATCH (n:pessoa)  RETURN  keys(n) limit 1'
}

resposta_nodeproperties_ok = {
    'columns': ['keys(n)'],
    'data': [
        [['nome_mae', 'cpf', 'dt_nasc', 'sexo', 'uf', 'nome']]
    ]
}

resposta_label_ok = [
    'multa',
    'veiculo',
    'personagem',
    'telefone',
    'mgp',
    'empresa',
    'orgao',
    'pessoa'
]

resposta_relationships_ok = [
    'filho',
    'proprietario',
    'autuado',
    'socio',
    'membro',
    'membro_inativo',
    'servidor_mprj',
    'responsavel',
    'personagem',
    'orgao_responsavel',
    'telefonema'
]

request_findShortestPath_ok = {
    "statements": [
        {
        "statement": "MATCH p = shortestPath((a)-[*]-(b)) "
            "WHERE id(a) = 140885160 AND id(b) = 328898991 RETURN p",
        "resultDataContents": ["row", "graph"]
        }
    ]
}

resposta_findShortestPath_ok = {
    "edges": [
        {
            "arrows":"to",
            "dashes":False,
            "from":"81208568",
            "id":"384945543",
            "label":"trabalha",
            "properties":{
                "dt_admissao":"20180601"
                },
            "to":"328898991"
        },
        {
            "arrows":"to",
            "dashes":False,
            "from":"205537878",
            "id":"304651477",
            "label":"filho",
            "properties":{},
            "to":"81208568"
        },
        {
            "arrows":"to",
            "dashes":False,
            "from":"205537878",
            "id":"288234032",
            "label":"filho",
            "properties":{},
            "to":"140885160"
        }
    ],
    "nodes":[
        {
            "id":"328898991",
            "label":"Label de Teste",
            "properties":{},
            "type":["sigiloso"]
        },
        {
            "id":"205537878",
            "label":"Label de Teste",
            "properties":{
                "cpf":"17937488700",
                "dt_nasc":"20120924",
                "filho_rel_status":7,
                "filho_rel_status_pai":1,
                "nome":"LUIZA LIMA DE ALMEIDA BELCHIOR",
                "nome_mae":"SILVIA LIMA DE ALMEIDA",
                "nome_pai":"DANIEL CARVALHO BELCHIOR",
                "nome_rg":"LUIZA LIMA DE ALMEIDA BELCHIOR",
                "rg":"298572447",
                "sexo":"2",
                "uf":"RJ"},
            "type":["pessoa"]
        },
        {
            "id":"140885160",
            "label":"Label de Teste",
            "properties":{
                "cpf":"11452244740",
                "dt_nasc":"19850522",
                "filho_rel_status":1,
                "filho_rel_status_pai":1,
                "nome":"DANIEL CARVALHO BELCHIOR",
                "nome_mae":"MARTA CARVALHO BELCHIOR",
                "nome_pai":"FRANCISCO IVAN FONTELE BELCHIOR",
                "nome_rg":"DANIEL CARVALHO BELCHIOR",
                "rg":"131242950",
                "sexo":"1",
                "uf":"RJ",
                "visitado":False},
            "type":["pessoa"]
        },
        {
            "id":"81208568",
            "label":"Label de Teste",
            "properties":{
                "cpf":"10069222703",
                "dt_nasc":"19820723",
                "filho_rel_status":3,
                "filho_rel_status_pai":1,
                "nome":"SILVIA LIMA DE ALMEIDA",
                "nome_mae":"MARIA FREITAS DE LIMA",
                "nome_pai":"AMARO JOSE DE ALMEIDA PINHEIRO",
                "nome_rg":"SILVIA LIMA DE ALMEIDA",
                "rg":"203556378",
                "sexo":"2",
                "uf":"RJ"},
            "type":["pessoa"]
        }
    ]
}

casos_servicos = [
    {
        'nome': 'api_node',
        'endereco': '/db/data/transaction/commit',
        'servico': '/api/node',
        'resposta': resposta_node_ok,
        'requisicao': request_node_ok,
        'query_string': {
            "node_id": 395989945
        },
        'metodo': responses.POST
    },
    {
        'nome': 'api_findShortestPath',
        'endereco': '/db/data/transaction/commit',
        'servico': '/api/findShortestPath',
        'resposta': resposta_findShortestPath_ok,
        'requisicao': request_findShortestPath_ok,
        'query_string': {
            "node_id1": 140885160,
            "node_id2": 328898991
        },
        'metodo': responses.POST
    },
    {
        'nome': 'api_nodeProperties',
        'endereco': '/db/data/cypher',
        'servico': '/api/nodeProperties',
        'resposta': resposta_nodeproperties_ok,
        'requisicao': request_nodeproperties_ok,
        'query_string': {
            "label": "pessoa"
        },
        'metodo': responses.POST
    },
    {
        'nome': 'api_labels',
        'endereco': '/db/data/labels',
        'servico': '/api/labels',
        'resposta': resposta_label_ok,
        'requisicao': None,
        'query_string': {},
        'metodo': responses.GET
    },
    {
        'nome': 'api_relationships',
        'endereco': '/db/data/relationship/types',
        'servico': '/api/relationships',
        'resposta': resposta_relationships_ok,
        'requisicao': None,
        'query_string': {},
        'metodo': responses.GET
    },
]

query_dinamica = [
    {'statement': "optional match (a:pessoa {nome:toUpper('DANIEL CARVALHO BELCHIOR')}) "
                  "optional match (b:personagem {pess_dk:24728287}) return a,b limit 100",
                  'resultDataContents': ['row', 'graph']}]


# Detran
response_rg = b'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><consultarRGResponse xmlns="http://www.detran.rj.gov.br"><consultarRGResult>0000 - Inclus\xc3\xa3o realizada com sucesso. Aguardar processamento</consultarRGResult></consultarRGResponse></soap:Body></soap:Envelope>'

response_processado_rg=b'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><BuscarProcessadosResponse xmlns="http://www.detran.rj.gov.br"><BuscarProcessadosResult><dadosCivil><Base>1</Base><IdCidadao>131242950</IdCidadao><RG>131242950</RG><DtExpedicao>22/01/2003 00:00:00</DtExpedicao><NoCidadao>Daniel Carvalho Belchior</NoCidadao><NoPaiCidadao>Francisco Ivan Fontele Belchior</NoPaiCidadao><NoMaeCidadao>Marta Carvalho Belchior</NoMaeCidadao><DtNascimento>22/05/1985 00:00:00</DtNascimento><EstadoCivil>1</EstadoCivil><EdLogradouro>Est do Rio Grande</EdLogradouro><EdComplemento>303</EdComplemento><EdNumero>3600</EdNumero><EdBairro>Jacarepagua</EdBairro><UFLogradouro>RJ</UFLogradouro><TpCertidao>1</TpCertidao><NuCertidaoLivro>863</NuCertidaoLivro><NuCertidaoFolha>98</NuCertidaoFolha><NuCertidaoTermo>87294</NuCertidaoTermo><NuCertidaoCircunscricao>8</NuCertidaoCircunscricao><PossuiObito>N</PossuiObito><DtObito /><CoRetorno>1</CoRetorno><MsgRetorno>Cidad\xc3\xa3o encontrado, atrav\xc3\xa9s do RG</MsgRetorno><fotoCivil><string>abcd</string></fotoCivil></dadosCivil></BuscarProcessadosResult></BuscarProcessadosResponse></soap:Body></soap:Envelope>'
