import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

FILES = {
    "users":    os.path.join(DATA_DIR, "users.json"),
    "projects": os.path.join(DATA_DIR, "projects.json"),
    "tasks":    os.path.join(DATA_DIR, "tasks.json"),
}

def ensure_Dirs():os.makedirs(DATA_DIR,exist_ok=True)

def read(ent):
    ensure_Dirs()
    path=FILES[ent]
    if not os.path.exists(path):
        return[]
    with open(path,"r",encoding="utf-8") as f:return json.load(f)
def write(ent,rec):
    ensure_Dirs()
    with open(FILES[ent],"w",encoding="utf-8") as f:json.dump(rec,f,indent=2)
def load():
    from models.user import Users
    from models.project import Projects
    from models.task import Tasks
    Users.all.clear()
    Projects.all.clear()
    Tasks.all.clear()
    for r in read("users"):
        Users.from_dict(r)
    for r in read("projects"):
        owner=Users.find(r["owner_id"])
        if owner:
            Projects.from_dict(r,owner=owner)
    for r in read("tasks"):
        proj=Projects.find(r["owner_id"])
        assigned=(Users.find(r["assigned_to_id"]) if r.get("assigned_to_id") else None)
        if proj:
            Tasks.from_dict(r,project=proj,assigned_to=assigned)
def save():
    from models.user import Users
    from models.project import Projects
    from models.task import Tasks
    write("users",[u.to_dict()for u in Users.all])
    write("projects",[p.to_dict()for p in Projects.all])
    write("tasks",[t.to_dict()for t in Tasks.all])