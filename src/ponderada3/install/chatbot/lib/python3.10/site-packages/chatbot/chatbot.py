import re
from . import actions

intent_dict = {
    r"\b([Vv][áãaàâ](?:\sao)?(?:\spara)\ (?:\ o)?[oa]|[Ll]ocomova-se\ at[ée]\ o|[Ss]e\ mova\ at[ée]\ o|[Aa]nde\ at[eé]\ o|[Vv][aá]\ ao)?\s(.+)": actions.go_to,
    r"[Vv]á\ para\ a\ secretaria": actions.go_to_secretaria,
    r"[Dd]irija-se\ ao\ laboratório": actions.go_to_laboratorio,
    r"[Mm]e\ leve\ para\ a\ biblioteca": actions.go_to_biblioteca
}

def process_command(command):
    for key, function in intent_dict.items():
        pattern = re.compile(key, re.IGNORECASE)
        point = pattern.findall(command)
        if point:
            print("Ação detectada")
            print(f"{point[0][0]} {point[0][1]}")
            function(point[0][1])
            return

if __name__ == "__main__":
    command = input("Digite seu pedido: ")
    process_command(command)
