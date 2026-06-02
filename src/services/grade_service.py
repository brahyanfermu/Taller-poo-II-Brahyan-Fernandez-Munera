from ..models.grade import Grade
from ..storage.json_storage import JSONStorage


class GradeService:

    def __init__(self):

        self.storage = JSONStorage(
            "data/grades.json"
        )

        try:
            self.grades = self.storage.load_grades()
        except:
            self.grades = []

    # =====================
    # MÉTODOS INTERNOS
    # =====================

    def _save_changes(self):

        return self.storage.save_grades(
            self.grades
        )

    def get_next_id(self):

        if not self.grades:
            return 1

        return max(
            grade.id
            for grade in self.grades
        ) + 1

    # =====================
    # CREATE
    # =====================

    def add_grade(
            self,
            student_id,
            subject_id,
            grade,
            exam_type,
            date
    ):

        if grade < 0 or grade > 5:
            print("❌ La nota debe estar entre 0 y 5")
            return False

        new_grade = Grade(
            self.get_next_id(),
            student_id,
            subject_id,
            grade,
            exam_type,
            date
        )

        self.grades.append(
            new_grade
        )

        return self._save_changes()

    # =====================
    # READ
    # =====================

    def get_all_grades(self):

        return self.grades.copy()

    def get_grade_by_id(
            self,
            grade_id
    ):

        for grade in self.grades:

            if grade.id == grade_id:
                return grade

        return None

    # =====================
    # DELETE
    # =====================

    def delete_grade(
            self,
            grade_id
    ):

        grade = self.get_grade_by_id(
            grade_id
        )

        if not grade:
            return False

        self.grades.remove(grade)

        return self._save_changes()

    # =====================
    # SEARCH
    # =====================

    def get_student_grades(
            self,
            student_id
    ):

        return [

            grade

            for grade in self.grades

            if grade.student_id == student_id

        ]

    def get_subject_grades(
            self,
            subject_id
    ):

        return [

            grade

            for grade in self.grades

            if grade.subject_id == subject_id

        ]

    # =====================
    # ESTADÍSTICAS
    # =====================

    def get_statistics(self):

        total = len(
            self.grades
        )

        approved = len(
            [
                grade
                for grade in self.grades
                if grade.is_passing()
            ]
        )

        failed = total - approved

        return {

            "total": total,

            "approved": approved,

            "failed": failed

        }