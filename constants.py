def collect_info():
    bomb_info = {}

    bomb_info['serial_no'] = input("What's the serial number on the bomb? ")
    bomb_info['batteries'] = input("How many batteries are there on the bomb? ")
    bomb_info['indicators'] = [i.strip() for i in input("Enter a comma-seperated list of lit indicators on the bomb. ").split(',')]

    return bomb_info