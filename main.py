import os


class DataManager:
    def __init__(self):
        self.file_name = "datos.txt"

    def guardar(self, n, e, t, p, s, r, f):
        # 1. Obsesión por primitivos & 3. Lista larga de parámetros & 4. Nombres poco descriptivos
        # 2. Anidamiento excesivo (Arrow anti-pattern)
        # 6. Acoplamiento de I/O con lógica de negocio
        if n != "":
            if e != "":
                if t != "":
                    if p != "":
                        if s != "":
                            if r != "":
                                # 5. Cadenas hardcodeadas y comparaciones redundantes
                                if (
                                    (p == "Alta") == True
                                    or (p == "Media") == True
                                    or (p == "Baja") == True
                                ):
                                    # 7. Persistencia frágil mediante cadenas planas
                                    linea = (
                                        n
                                        + ","
                                        + e
                                        + ","
                                        + t
                                        + ","
                                        + p
                                        + ","
                                        + s
                                        + ","
                                        + r
                                        + ","
                                        + f
                                        + "\n"
                                    )
                                    fl = open(self.file_name, "a")
                                    fl.write(linea)
                                    fl.close()
                                    print("Guardado correctamente")
                                else:
                                    pass  # 8. Validación silenciosa sin feedback
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

    def listar(self):
        print("--- LISTADO DE SOLICITUDES ---")
        try:
            fl = open(self.file_name, "r")
            l = fl.readlines()
            fl.close()
            for x in l:
                # 1. Obsesión por primitivos (parseo manual frágil por split)
                d = x.strip().split(",")
                if len(d) == 7:
                    # 5. Comparaciones redundantes y anidamiento excesivo en estados
                    if (d[4] == "Pendiente") == True:
                        print(
                            "Estudiante: "
                            + d[0]
                            + " | Tipo: "
                            + d[2]
                            + " | Prioridad: "
                            + d[3]
                            + " | Estado: "
                            + d[4]
                            + " | Responsable: "
                            + d[5]
                        )
                    else:
                        if (d[4] == "Proceso") == True:
                            print(
                                "Estudiante: "
                                + d[0]
                                + " | Tipo: "
                                + d[2]
                                + " | Prioridad: "
                                + d[3]
                                + " | Estado: "
                                + d[4]
                                + " | Responsable: "
                                + d[5]
                            )
                        else:
                            if (d[4] == "Cerrada") == True:
                                print(
                                    "Estudiante: "
                                    + d[0]
                                    + " | Tipo: "
                                    + d[2]
                                    + " | Prioridad: "
                                    + d[3]
                                    + " | Estado: "
                                    + d[4]
                                    + " | Responsable: "
                                    + d[5]
                                )
                            else:
                                print("Estado desconocido")
                else:
                    pass
        except:
            # 8. Ausencia de manejo real de excepciones (captura genérica y silenciosa)
            pass

    def actualizarProceso(self, n_busca):
        fl = open(self.file_name, "r")
        lines = fl.readlines()
        fl.close()
        new_lines = []
        for line in lines:
            parts = line.strip().split(",")
            # 5. Cadenas hardcodeadas y comparación redundante
            if (parts[0] == n_busca) == True:
                parts[4] = "Proceso"  # Cambio de estado hardcodeado
                new_lines.append(",".join(parts) + "\n")
            else:
                new_lines.append(line)
        fl = open(self.file_name, "w")
        for nl in new_lines:
            fl.write(nl)
        fl.close()
        
    def actualizarCerrada(self, n_busca):
        fl = open(self.file_name, "r")
        lines = fl.readlines()
        fl.close()
        new_lines = []
        for line in lines:
            parts = line.strip().split(",")
            # 5. Cadenas hardcodeadas y comparación redundante
            if (parts[0] == n_busca) == True:
                parts[4] = "Cerrada"  # Cambio de estado hardcodeado
                new_lines.append(",".join(parts) + "\n")
            else:
                new_lines.append(line)
        fl = open(self.file_name, "w")
        for nl in new_lines:
            fl.write(nl)
        fl.close()

    def actualizarPendiente(self, n_busca):
        fl = open(self.file_name, "r")
        lines = fl.readlines()
        fl.close()
        new_lines = []
        for line in lines:
            parts = line.strip().split(",")
            # 5. Cadenas hardcodeadas y comparación redundante
            if (parts[0] == n_busca) == True:
                parts[4] = "Pendiente"  # Cambio de estado hardcodeado
                new_lines.append(",".join(parts) + "\n")
            else:
                new_lines.append(line)
        fl = open(self.file_name, "w")
        for nl in new_lines:
            fl.write(nl)
        fl.close()


class ProcessHandler:
    def __init__(self):
        self.dm = DataManager()

    def run(self):
        while True:
            print("\n1. Registrar Solicitud")
            print("\n2. Listar Solicitudes")
            print("\n3. Cambiar Estado a Pendiente")
            print("\n4. Cambiar Estado a Proceso")
            print("\n5. Cambiar Estado a Cerrada")
            print("\n0. Salir")
            op = input("Elija opcion: ")

            if op == "1":
                n = input("Nombre: ")
                e = input("Email: ")
                t = input("Tipo: ")
                p = input("Prioridad (Alta/Media/Baja): ")
                s = input("Estado inicial: ")
                r = input("Responsable: ")
                f = input("Fecha: ")
                self.dm.guardar(n, e, t, p, s, r, f)
            elif op == "2":
                self.dm.listar()
            elif op == "3":
                nom = input("Nombre del estudiante a actualizar: ")
                self.dm.actualizarPendiente(nom)
            elif op == "4":
                nom = input("Nombre del estudiante a actualizar: ")
                self.dm.actualizarProceso(nom)
            elif op == "5":
                nom = input("Nombre del estudiante a actualizar: ")
                self.dm.actualizarCerrada(nom)
            elif op == "0":
                break
            else:
                print("Opcion invalida")


if __name__ == "__main__":
    ph = ProcessHandler()
    ph.run()
