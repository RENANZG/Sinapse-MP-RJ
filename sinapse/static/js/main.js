const init = () => {
    initNeo4JD3()
    getLabels()
    initSearch()
}

let neo4jd3

const initNeo4JD3 = () => {
    neo4jd3 = new Neo4jd3('#neo4jd3', {
        highlight: [
            {
                class: 'Project',
                property: 'name',
                value: 'neo4jd3'
            }, {
                class: 'User',
                property: 'userId',
                value: 'eisman'
            }
        ],
        icons: {
            'Api': 'gear',
            'Cookie': 'paw',
            'Email': 'at',
            'Git': 'git',
            'Github': 'github',
            'Google': 'google',
            'Ip': 'map-marker',
            'Issues': 'exclamation-circle',
            'Language': 'language',
            'Options': 'sliders',
            'Password': 'lock',
            'Phone': 'phone',
            'Project': 'folder-open',
            'SecurityChallengeAnswer': 'commenting',
            'pessoa': 'user',
            'personagem':'users',
            'veiculo': 'car',
            'empresa': 'building',
            'mgp':'balance-scale',
            'zoomFit': 'arrows-alt',
            'zoomIn': 'search-plus',
            'zoomOut': 'search-minus'
        }, 
        images: {
            'Address': 'img/twemoji/1f3e0.svg',
            'BirthDate': 'img/twemoji/1f382.svg',
            'Cookie': 'img/twemoji/1f36a.svg',
            'CreditCard': 'img/twemoji/1f4b3.svg',
            'Device': 'img/twemoji/1f4bb.svg',
            'Email': 'img/twemoji/2709.svg',
            'Git': 'img/twemoji/1f5c3.svg',
            'Github': 'img/twemoji/1f5c4.svg',
            'icons': 'img/twemoji/1f38f.svg',
            'Ip': 'img/twemoji/1f4cd.svg',
            'Issues': 'img/twemoji/1f4a9.svg',
            'Language': 'img/twemoji/1f1f1-1f1f7.svg',
            'Options': 'img/twemoji/2699.svg',
            'Password': 'img/twemoji/1f511.svg',
            'Project': 'img/twemoji/2198.svg',
            'Project|name|neo4jd3': 'img/twemoji/2196.svg',
            'User': 'img/twemoji/1f600.svg'
        },
        minCollision: 60,
        neo4jDataUrl: '/static/json/neo4jData_vazio.json',
        nodeRadius: 25,
        onNodeDoubleClick: function(node) {
            get('api/nextNodes?node_id=' + node.id, (data) => {
                neo4jd3.updateWithNeo4jData(data)
            });                        
        },
        onRelationshipDoubleClick: function(relationship) {
            console.log('double click on relationship: ' + JSON.stringify(relationship))
        },
    })
}

const getLabels = () => {
    get('/api/labels', setLabels)
}

const setLabels = labels => {
    document.getElementById('loading').className = 'hidden'
    document.getElementById('step1').className = ''
    let labelsMenu = document.getElementById('opcoes')
    labels.sort().map(label => {
        if (label !== 'teste') {
            // <span>
            let labelTooltipEl = document.createElement('span')
            let labelTooltipStr = document.createTextNode(formatPropString(label))
            labelTooltipEl.appendChild(labelTooltipStr)
            labelTooltipEl.className = 'tooltip'
            // <img>
            let labelImg = document.createElement('img')
            labelImg.setAttribute('src', `/static/img/icon/${label}.svg`)
            labelImg.dataset.label = label
            // <div>
            //   <img>
            //   <span/>
            // </div>
            let labelEl = document.createElement('div')
            labelEl.appendChild(labelImg)
            labelEl.appendChild(labelTooltipEl)
            labelEl.className = label
            labelEl.onclick = getNodeProperties
            // append to DOM
            labelsMenu.appendChild(labelEl)
        }
    })
    // init comece-aqui button
    let comeceAquiEl = document.getElementById('comece-aqui')
    let opcoesEl = document.getElementById('opcoes')
    comeceAquiEl.onclick = () => {
        if (opcoesEl.className === 'opcoes') {
            opcoesEl.className = 'opcoes hidden'
        } else {
            opcoesEl.className = 'opcoes'
        }
    }
    // step2 back button
    document.getElementById('step2img').onclick = e => {
        document.getElementById('step1').className = ''
        document.getElementById('step2').className = 'hidden'
    }
}

const getNodeProperties = e => {
    let label = e.target.dataset.label
    document.getElementById('step2img').setAttribute('src', `/static/img/icon/${label}.svg`)
    document.getElementById('selectLabel').value = label
    document.getElementById('form-step2').className = label
    get(`api/nodeProperties?label=${label}`, setProps)
}

const appendOption = (select, optionValue) => {
    var option = document.createElement('option')
    option.value = optionValue
    option.innerHTML = formatPropString(optionValue)
    select.appendChild(option)
}

const setProps = nodeProperties => {
    // hide step1, show step2
    document.getElementById('step1').className = 'hidden'
    document.getElementById('step2').className = ''

    let props = nodeProperties.data[0][0]
    
    let selectProp = document.getElementById('selectProp')
    
    // remove children option
    while (selectProp.firstChild) {
        selectProp.removeChild(selectProp.firstChild);
    }

    // add empty option
    let emptyOption = document.createElement('option')
    emptyOption.value = ''
    emptyOption.innerHTML = 'Refinar a busca'
    selectProp.appendChild(emptyOption)
    
    // add options
    props.sort().map(prop => appendOption(selectProp, prop))
}

const initSearch = () => {
    document.getElementById('buttonBusca').onclick = findNodes
}

const findNodes = () => {
    let label = document.getElementById('selectLabel').value
    let prop = document.getElementById('selectProp').value
    let val = document.getElementById('textVal').value
    if (!label || !prop || !val) {
        return alert('ERRO: É preciso escolher o tipo, a propriedade e preencher um valor para realizar uma busca.')
    }
    get(`/api/findNodes?label=${label}&prop=${prop}&val=${val}`, updateNodes)
    // hide form
    document.getElementById('step1').className = 'hidden'
    document.getElementById('step2').className = 'hidden'
}

const updateNodes = data => {
    neo4jd3.updateWithNeo4jData(data)
}

/**
 * Adds diacritics (a => á) and formats props case.
 * 
 * @param {string} text The prop string to be formatted
 */
const formatPropString = text => {
    switch (text) {
        // 1st Level
        case 'veiculo':
            return 'Veículo'
        case 'orgao':
            return 'Órgão'
        case 'mgp':
            return 'MGP'
        // Empresa
        case 'cnae':
            return 'CNAE'
        case 'cnpj':
            return 'CNPJ'
        case 'cpf_responsavel':
            return 'CPF do Responsável'
        case 'data_inicio':
            return 'Data de Início'
        case 'municipio':
            return 'Município'
        case 'nome_responsavel':
            return 'Nome do Responsável'
        case 'razao_social':
            return 'Razão Social'
        case 'uf':
            return 'UF'
        // MGP
        case 'cdorgao':
            return 'Código do Órgão'
        case 'docu_dk':
            return 'ID do Documento'
        case 'dt_cadastro':
            return 'Data do Cadastro'
        case 'nr_ext':
            return 'Número Externo'
        case 'nr_mprj':
            return 'Número MPRJ'
        // Multa
        case 'desc':
            return 'Descrição'
        // Órgão
        case 'craai':
            return 'CRAAI'
        case 'dt_criacao':
            return 'Data de Criação'
        case 'dt_extincao':
            return 'Data de Extinção'
        case 'sensivel':
            return 'Sensível'
        case 'situacao':
            return 'Situação'
        // Pessoa
        case 'cpf':
            return 'CPF'
        case 'dt_nasc':
            return 'Data de Nascimento'
        case 'nome_mae':
            return 'Nome da Mãe'
        // Telefone
        case 'numero':
            return 'Número'
        // Veículo
        case 'cpfcnpj':
            return 'CPF/CNPJ'
        default:
            return text.split('_').map(word => word.substr(0, 1).toUpperCase() + word.substr(1)).join(' ')
    }
}

/**
 * Make a HTTP GET call and returns the data.
 * 
 * @param {String} url - The URL to GET
 * @param {Function} callback - A function to be executed with the returned data.
 */
const get = (url, callback) => {
    var xmlhttp = new XMLHttpRequest()
    xmlhttp.open('GET', url, true)
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4) {
            if(xmlhttp.status == 200) {
                var obj = JSON.parse(xmlhttp.responseText)
                console.log(obj)
                if (callback) {
                    callback(obj)
                }
            }
        }
    }
    xmlhttp.send(null)
}

window.onload = init
