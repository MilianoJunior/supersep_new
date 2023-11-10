
conexoes = {
    'local': {
        'host': 'localhost',
        'user': 'root',
        'password': 'jr88869892',
        'database': 'engesepdb',
        'port': 3306
    },
    'railway': {
        'host': 'containers-us-west-66.railway.app',
        'user': 'root',
        'password': 'AIgi26lIFr70Rz6uGUbQ',
        'database': 'railway',
        'port': 7438
    },
    'local_2': {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'engesep_db',
        'port': 3307
    },
    'local_utils': {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'utils',
        'port': 3306
    },
}

supervisorio = {
    'maria_da_luz railway': {
        'status': {
            'address': 'LW-100',
            '0': 'parado',
            '1': 'desconectado',
            '2': 'conectado',
        },
        'Error': {
            'address': 'LW-101',
            '0': 'sem erro',
            '1': 'erro'
        },
        'Control': {
            'address': 'LW-110',
            '0': 'None',
            '1': 'Start',
            '2': 'Stop',
            '3': 'update',
        },
        'Reserved': {
            'address': 'LW-111',
        },
        'Port': {
            'address': 'LW-115',
        },
        'Username': {
            'address': 'LW-116',
        },
        'Password': {
            'address': 'LW-132',
        },
        'Database Name': {
            'address': 'LW-148',
        },
        'Domain name': {
            'address': 'LW-164',
        },
        'Consulta sql railway': {
            'Command ID': 'LW-200',
            'Row select': 'LW-201',
            'Row status': 'LW-202',
            'Error code': 'LW-203',
            'Error message': 'LW-204',
        },
    },
    'maria_da_luz local': {
        'status': {
            'address': 'LW-400',
            '0': 'parado',
            '1': 'desconectado',
            '2': 'conectado',
        },
        'Error': {
            'address': 'LW-401',
            '0': 'sem erro',
            '1': 'erro'
        },
        'Control': {
            'address': 'LW-410',
            '0': 'None',
            '1': 'Start',
            '2': 'Stop',
            '3': 'update',
        },
        'Reserved': {
            'address': 'LW-411',
        },
        'Port': {
            'address': 'LW-415',
        },
        'Username': {
            'address': 'LW-416',
        },
        'Password': {
            'address': 'LW-432',
        },
        'Database Name': {
            'address': 'LW-448',
        },
        'Domain name': {
            'address': 'LW-464',
        },
        'Consulta sql local': {
            'Command ID': 'LW-300',
            'Row select': 'LW-301',
            'Row status': 'LW-302',
            'Error code': 'LW-303',
            'Error message': 'LW-304',
        },
    },
    'parisoto local': {
        'status': {
            'address': 'LW-400',
            '0': 'parado',
            '1': 'desconectado',
            '2': 'conectado',
        },
        'Error': {
            'address': 'LW-401',
            '0': 'sem erro',
            '1': 'erro'
        },
        'Control': {
            'address': 'LW-410',
            '0': 'None',
            '1': 'Start',
            '2': 'Stop',
            '3': 'update',
        },
        'Reserved': {
            'address': 'LW-411',
        },
        'Port': {
            'address': 'LW-415',
        },
        'Username': {
            'address': 'LW-416',
        },
        'Password': {
            'address': 'LW-432',
        },
        'Database Name': {
            'address': 'LW-448',
        },
        'Domain name': {
            'address': 'LW-464',
        },
        'Consulta sql local': {
            'Command ID': 'LW-300',
            'Row select': 'LW-301',
            'Row status': 'LW-302',
            'Error code': 'LW-303',
            'Error message': 'LW-304',
        },
    },
}
# INSERT INTO usina(valor) VALUES ('${1}');