import uuid
from .project import Projects
from .task import Tasks
class Users:
    all=[]
    def __init__(self, name, email, id=None):
        self.id=id or str(uuid.uuid4())
        self.name= name
        self.email= email
        Users.all.append(self)

    def projects(self):
        return[p for p in Projects.all if p.owner is self]
    def tasks(self):
        return[t for t in Tasks.all if t.assigned_to is self]
    
    def to_dict(self):
        return{"id":self.id, "name":self.name,"email":self.email}
    @classmethod
    def from_dict(cls,data):
        return cls(name=data["name"],email=data["email"],id=data["id"])
    @classmethod
    def find(cls,uID):
        return next((u for u in cls.all if u.id ==uID),None)
    def __repr__(self):
        return f"[{self.id[:8]}] {self.name} <{self.email}>"
    