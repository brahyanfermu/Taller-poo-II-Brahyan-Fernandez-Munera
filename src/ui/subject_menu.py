from ..services.subject_service import SubjectService


class SubjectMenu:

    def __init__(self):
        self.service = SubjectService()

    def show_menu(self):

        print("\n" + "=" * 50)
        print("📚 GESTIÓN DE MATERIAS")
        print("=" * 50)

        print("1. Ver materias")
        print("2. Buscar materia")
        print("3. Agregar materia")
        print("4. Actualizar materia")
        print("5. Eliminar materia")
        print("6. Estadísticas")
        print("0. Volver")

        print("-" * 50)

    def list_subjects(self):

        subjects = self.service.get_all_subjects()

        if not subjects:
            print("\n❌ No hay materias registradas")
            return

        print("\n📚 LISTA DE MATERIAS")
        print("-" * 50)

        for subject in subjects:
            print(subject)

    def add_subject(self):

        print("\n➕ NUEVA MATERIA")

        name = input("Nombre: ")

        teacher_id = int(
            input("ID Profesor: ")
        )

        credits = int(
            input("Créditos: ")
        )

        description = input(
            "Descripción: "
        )

        success = self.service.add_subject(
            name,
            teacher_id,
            credits,
            description
        )

        if success:
            print("✅ Materia creada")
        else:
            print("❌ Error al crear materia")

    def search_subject(self):

        text = input(
            "\n🔍 Buscar materia: "
        )

        results = self.service.search_subjects(
            text
        )

        if not results:
            print("❌ No encontrada")
            return

        for subject in results:
            print(subject)

    def delete_subject(self):

        subject_id = int(
            input("ID materia a eliminar: ")
        )

        if self.service.delete_subject(
                subject_id
        ):
            print("✅ Materia eliminada")
        else:
            print("❌ No encontrada")

    def statistics(self):

        stats = self.service.get_statistics()

        print("\n📊 ESTADÍSTICAS")
        print("-" * 30)
        print(
            f"Total materias: {stats['total']}"
        )

    def run(self):

        while True:

            self.show_menu()

            option = input(
                "Seleccione opción: "
            )

            if option == "1":
                self.list_subjects()

            elif option == "2":
                self.search_subject()

            elif option == "3":
                self.add_subject()

            elif option == "5":
                self.delete_subject()

            elif option == "6":
                self.statistics()

            elif option == "0":
                break

            else:
                print("❌ Opción inválida")

            input(
                "\nPresione ENTER para continuar..."
            )