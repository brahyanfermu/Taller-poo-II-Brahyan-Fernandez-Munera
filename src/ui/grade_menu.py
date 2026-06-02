from ..services.grade_service import GradeService


class GradeMenu:

    def __init__(self):
        self.service = GradeService()

    def show_menu(self):

        print("\n" + "=" * 50)
        print("📝 GESTIÓN DE CALIFICACIONES")
        print("=" * 50)

        print("1. Ver notas")
        print("2. Registrar nota")
        print("3. Buscar notas por estudiante")
        print("4. Buscar notas por materia")
        print("5. Eliminar nota")
        print("6. Estadísticas")
        print("0. Volver")

        print("-" * 50)

    def list_grades(self):

        grades = self.service.get_all_grades()

        if not grades:
            print("\n❌ No existen calificaciones registradas")
            return

        print("\n📋 LISTA DE CALIFICACIONES")
        print("-" * 50)

        for grade in grades:
            print(grade)

    def add_grade(self):

        print("\n➕ REGISTRAR CALIFICACIÓN")

        student_id = int(
            input("ID del estudiante: ")
        )

        subject_id = int(
            input("ID de la materia: ")
        )

        grade = float(
            input("Nota (0 - 5): ")
        )

        exam_type = input(
            "Tipo de evaluación: "
        )

        date = input(
            "Fecha (YYYY-MM-DD): "
        )

        success = self.service.add_grade(
            student_id,
            subject_id,
            grade,
            exam_type,
            date
        )

        if success:
            print("✅ Nota registrada")
        else:
            print("❌ Error al registrar")

    def search_by_student(self):

        student_id = int(
            input("ID del estudiante: ")
        )

        grades = self.service.get_student_grades(
            student_id
        )

        if not grades:
            print("❌ No hay notas")
            return

        for grade in grades:
            print(grade)

    def search_by_subject(self):

        subject_id = int(
            input("ID de la materia: ")
        )

        grades = self.service.get_subject_grades(
            subject_id
        )

        if not grades:
            print("❌ No hay notas")
            return

        for grade in grades:
            print(grade)

    def delete_grade(self):

        grade_id = int(
            input("ID de la nota a eliminar: ")
        )

        if self.service.delete_grade(
                grade_id
        ):
            print("✅ Nota eliminada")
        else:
            print("❌ No encontrada")

    def statistics(self):

        stats = self.service.get_statistics()

        print("\n📊 ESTADÍSTICAS")

        print(
            f"Total notas: {stats['total']}"
        )

        print(
            f"Aprobadas: {stats['approved']}"
        )

        print(
            f"Reprobadas: {stats['failed']}"
        )

    def run(self):

        while True:

            self.show_menu()

            option = input(
                "Seleccione opción: "
            )

            if option == "1":
                self.list_grades()

            elif option == "2":
                self.add_grade()

            elif option == "3":
                self.search_by_student()

            elif option == "4":
                self.search_by_subject()

            elif option == "5":
                self.delete_grade()

            elif option == "6":
                self.statistics()

            elif option == "0":
                break

            else:
                print("❌ Opción inválida")

            input(
                "\nPresione ENTER para continuar..."
            )