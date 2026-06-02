from ..models.subject import Subject
from ..storage.json_storage import JSONStorage


class SubjectService:

    def __init__(self, storage=None):

        self.storage = storage or JSONStorage("data/subjects.json")

        try:
            self.subjects = self.storage.load_subjects()
        except:
            self.subjects = []

    # ======================
    # MÉTODOS PRIVADOS
    # ======================

    def _save_changes(self):

        return self.storage.save_subjects(self.subjects)

    def get_next_id(self):

        if not self.subjects:
            return 1

        return max(subject.id for subject in self.subjects) + 1

    # ======================
    # CREATE
    # ======================

    def add_subject(
            self,
            name,
            teacher_id,
            credits,
            description=""
    ):

        if not name.strip():
            print("❌ Nombre inválido")
            return False

        if credits <= 0:
            print("❌ Créditos inválidos")
            return False

        new_subject = Subject(
            self.get_next_id(),
            name,
            teacher_id,
            credits,
            description
        )

        self.subjects.append(new_subject)

        if self._save_changes():
            return True

        self.subjects.remove(new_subject)

        return False

    # ======================
    # READ
    # ======================

    def get_all_subjects(self):

        return self.subjects.copy()

    def get_subject_by_id(self, subject_id):

        for subject in self.subjects:

            if subject.id == subject_id:
                return subject

        return None

    # ======================
    # UPDATE
    # ======================

    def update_subject(
            self,
            subject_id,
            name=None,
            teacher_id=None,
            credits=None,
            description=None
    ):

        subject = self.get_subject_by_id(subject_id)

        if not subject:
            return False

        if name:
            subject.name = name

        if teacher_id:
            subject.teacher_id = teacher_id

        if credits:
            subject.credits = credits

        if description:
            subject.description = description

        return self._save_changes()

    # ======================
    # DELETE
    # ======================

    def delete_subject(self, subject_id):

        subject = self.get_subject_by_id(subject_id)

        if not subject:
            return False

        self.subjects.remove(subject)

        return self._save_changes()

    # ======================
    # SEARCH
    # ======================

    def search_subjects(self, text):

        text = text.lower()

        return [

            subject

            for subject in self.subjects

            if text in subject.name.lower()

        ]

    # ======================
    # STATISTICS
    # ======================

    def get_statistics(self):

        return {

            "total": len(self.subjects)

        }