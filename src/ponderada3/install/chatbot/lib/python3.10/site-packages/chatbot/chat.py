import re
from . import actions

intent_dict = {
    r"\b([Vv][áãaàâ](?:\sao)?(?:\spara)\ (?:\ o)?[oa]|[Ll]ocomova-se\ at[ée]\ o|[Ss]e\ mova\ at[ée]\ o|[Aa]nde\ at[eé]\ o|[Vv][aá]\ ao)?\s(.+)": actions.go_to,
    r"[Vv]á\ para\ a\ secretaria": actions.go_to_secretaria,
    r"[Dd]irija-se\ ao\ laboratório": actions.go_to_laboratorio,
    r"[Mm]e\ leve\ para\ a\ biblioteca": actions.go_to_biblioteca
}

def main():
    command = input("Digite seu pedido: ")
    for key, function in intent_dict.items():
        pattern = re.compile(key, re.IGNORECASE)
        matches = pattern.search(command)
        if matches:
            print("Ação detectada")
            print(f"{matches.group(1)} {matches.group(2)}")
            function(matches.group(2))
            return

if __name__ == "__main__":
    main()
