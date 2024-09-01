import json

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


try:
    ### Load JSON
    with open('commands.json') as json_file:
        commands = json.load(json_file)
    print('loaded')
except:
    ### Initialize commands.json
    commands = {
        'temp_automatizacion': [],
        'temp_impresoras': [],
        'temp_taller': [],
        'temp_oficinas': [],
        'temp_host': [],
        'puerta': [],
        'cortinas_oficinas': [],
        'cortinas_automatizacion': [],
    }
    print('initialize')

while True:
    print('-'*30)
    print('>>> Servicios disponibles:\n')
    i = 0
    command_keys = []
    for command_i in commands.keys():
        command_keys.append(command_i)
        i += 1
        print('> [{}]: {}'.format(i,command_i))

    print('\n')
    service_i = int(input('Seleccione el número de servicio al cual desea añadir una petición especifica: '))
    command_i = input('Su petición: ')
    commands[command_keys[service_i-1]].append(normalize(command_i.lower()))
    again = input('Gracias, su petición fue guardada, ¿Desea registrar otra? [ Y / N ]').lower()

    if again == 'n':
        break
    

### Write JSON
with open('commands.json', 'w') as fp:
    json.dump(commands, fp, indent = 4)