import uuid
from .task import Tasks
class Projects:
    all = []
    def __init__(self,title, description, due_date, owner, id=None):
        self.id = id or str(uuid.uuid4())
        self.title=title
        self.description=description
        self.due_date=due_date
        self.owner=owner
        Projects.all.append(self)

         
    def tasks(self):
        return [t for t in Tasks.all if t.project is self]
    def completion_rate(self):
        all=self.tasks()
        if not all:
            return 0.0
        done=[t for t in all if t.status=="done"]
        return len(done)/len(all)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "owner_id": self.owner.id,
        }


    @classmethod
    def from_dict(cls, dat, own):
        return cls(
            title=dat["title"],
            description=dat["description"],
            due_date=dat["due_date"],
            owner=own,
            id=dat["id"],
        )

    @classmethod
    def find(cls, pid):
        return next((p for p in cls.all if p.id == pid), None)

    def __repr__(self):
        return f"[{self.id[:8]}] {self.title} (due: {self.due_date})"