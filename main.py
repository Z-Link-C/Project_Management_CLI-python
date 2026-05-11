import argparse
import sys
from models import Users, Projects,Tasks
from utils import load, save, print_table

#---Users
def add_user(args):
    load()
    user = Users(name=args.name, email=args.email)
    save()
    print(f"Created {user}.")


def list_users(args):
    load()
    print_table([repr(u) for u in Users.all], header=f"Users ({len(Users.all)})")


def delete_user(args):
    load()
    user = Users.find(args.user_id)
    if not user:
        raise KeyError(f"No user with ID '{args.user_id}'")

    for project in user.projects():
        for task in project.tasks():
            Tasks.all.remove(task)
        Projects.all.remove(project)

    for task in user.tasks():
        if task in Tasks.all:
            Tasks.all.remove(task)

    Users.all.remove(user)
    save()
    print(f"User '{user.name}' deleted (cascade: projects + tasks removed).")

#---projects
def add_project(args):
    load()
    owner = Users.find(args.owner_id)
    if not owner:
        raise KeyError(f"No user with ID '{args.owner_id}'")

    project = Projects(
        title=args.title,
        description=args.description,
        due_date=args.due_date,
        owner=owner,
    )
    save()
    print(f"Created {project}")


def list_projects(args):
    load()
    if args.owner_id:
        owner = Users.find(args.owner_id)
        if not owner:
            raise KeyError(f"No user with ID '{args.owner_id}'")
        projects = owner.projects()
    else:
        projects = Projects.all
    print_table([repr(p) for p in projects], header=f"Projects ({len(projects)})")


def delete_project(args):
    load()
    project = Projects.find(args.project_id)
    if not project:
        raise KeyError(f"No project with ID '{args.project_id}'")

    for task in project.tasks():
        Tasks.all.remove(task)

    Projects.all.remove(project)
    save()
    print(f"Projects '{project.title}' deleted (cascade: tasks removed).")
#---tasks
 
def add_task(args):
    load()
    project = Projects.find(args.project_id)
    if not project:
        raise KeyError(f"No project with ID '{args.project_id}'")

    assigned_to = None
    if args.assigned_to:
        assigned_to = Users.find(args.assigned_to)
        if not assigned_to:
            raise KeyError(f"No user with ID '{args.assigned_to}'")

    task = Tasks(
        title=args.title,
        status=args.status,
        project=project,
        assigned_to=assigned_to,
    )
    save()
    print(f"Created {task} task")


def list_tasks(args):
    load()
    if args.project_id:
        project = Projects.find(args.project_id)
        if not project:
            raise KeyError(f"No project with ID '{args.project_id}'")
        tasks = project.tasks()
    else:
        tasks = Tasks.all
    print_table([repr(t) for t in tasks], header=f"Tasks ({len(tasks)})")


def update_task(args):
    load()
    task = Tasks.find(args.task_id)
    if not task:
        raise KeyError(f"No task with ID '{args.task_id}'")
    task.status = args.status
    save()
    print(f"Status updated to {args.status} for '{task.title}' task.")


def delete_task(args):
    load()
    task = Tasks.find(args.task_id)
    if not task:
        raise KeyError(f"No task with ID '{args.task_id}'")
    Tasks.all.remove(task)
    save()
    print(f"Deleted '{task.title}'.")   

#---entry
def build_parser():
    parser = argparse.ArgumentParser(prog="pm", description="project-management CLI")
    sub = parser.add_subparsers(dest="entity", metavar="entity", required=True)

    # -- Users
    user_parser = sub.add_parser("user", help="Manage users")
    user_sub = user_parser.add_subparsers(dest="action", metavar="action", required=True)
    ua = user_sub.add_parser("add")
    ua.add_argument("--name", required=True)
    ua.add_argument("--email", required=True)
    user_sub.add_parser("list")
    ud = user_sub.add_parser("delete")
    ud.add_argument("--id", required=True, dest="user_id")

    # -- Projects
    proj_parser = sub.add_parser("project", help="Manage projects")
    proj_sub = proj_parser.add_subparsers(dest="action", metavar="action", required=True)
    pa = proj_sub.add_parser("add")
    pa.add_argument("--title", required=True)
    pa.add_argument("--description", required=False)
    pa.add_argument("--due-date", required=True, metavar="YYYY-MM-DD")
    pa.add_argument("--owner-id", required=True)
    pl = proj_sub.add_parser("list")
    pl.add_argument("--owner-id")
    pdel = proj_sub.add_parser("delete")
    pdel.add_argument("--id", required=True, dest="project_id")

    # -- Tasks
    task_parser = sub.add_parser("task", help="Manage tasks")
    task_sub = task_parser.add_subparsers(dest="action", metavar="action", required=True)
    ta = task_sub.add_parser("add")
    ta.add_argument("--title", required=True)
    ta.add_argument("--status", required=True, choices=["todo", "in-progress", "done"])
    ta.add_argument("--project-id", required=True)
    ta.add_argument("--assigned-to")
    tl = task_sub.add_parser("list")
    tl.add_argument("--project-id")
    tu = task_sub.add_parser("update")
    tu.add_argument("--id", required=True, dest="task_id")
    tu.add_argument("--status", required=True, choices=["todo", "in-progress", "done"])
    tdel = task_sub.add_parser("delete")
    tdel.add_argument("--id", required=False, dest="task_id")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.entity == "user":
            if args.action == "add": add_user(args)
            elif args.action == "list": list_users(args)
            elif args.action == "delete": delete_user(args)
        elif args.entity == "project":
            if args.action == "add": add_project(args)
            elif args.action == "list": list_projects(args)
            elif args.action == "delete": delete_project(args)
        elif args.entity == "task":
            if args.action == "add": add_task(args)
            elif args.action == "list": list_tasks(args)
            elif args.action == "update": update_task(args)
            elif args.action == "delete": delete_task(args)
    except (KeyError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()