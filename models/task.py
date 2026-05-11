
import uuid

VSTATS=("todo","in_progress","complete")
class Tasks:
    all=[]
    def __init__(self,title,status,project,assigned_to=None,id=None):
        if status not in VSTATS:
            raise ValueError(
                f"Invalid status {status!r}."
                f"Please Choose only from: {', '.join(VSTATS)}"
            )
        self.id or str(uuid.uuid4())
        self.title=title
        self.status=status
        self.project=project
        self.assigned_to=assigned_to
        Tasks.all.append(self)
    def to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "status":self.status,
            "project_id":self.project.id,
            "assigned_to_id":self.assigned_to.id if self.assigned_to else None
        }    
    @classmethod
    def from_dict(cls, data, project, assigned_to=None):
        return cls(
            title=data["title"],
            status=data["status"],
            project=project,
            assigned_to=assigned_to,
            id=data["id"],
        )

    @classmethod
    def find(cls, tid):
        return next((t for t in cls.all if t.id == tid), None)

    def __repr__(self):
        assigned = self.assigned_to.name if self.assigned_to else "unassigned"
        return f"[{self.id[:8]}] {self.title} [{self.status}] -> {assigned}"