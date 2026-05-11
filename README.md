# commands:
## Python main.py user [add, list, delete]
  ### Add:
    python main.py user add --name <Name> --email <Email>
  ### Delete:
    python main.py user delete --id <UserID> 
  ### List:
    python main.py user list {outputs saved users from users.json}
    
## Python main.py project [add, list, delete]
  ### Add:
    python main.py project add --title <Title> --description <Description(optional)> --due-date <Date(yyyy-mm-dd fromat)> --owner-id <UserID>
  ### Delete:
    python main.py project delete --id <ProjectID> 
  ### List:
    python main.py project list {outputs saved users from project.json}
## Python main.py task [add, list, update, delete]
  ### Add:
    python main.py task add --title <Title> --status <Status (options:"todo", "in-progress", "done")> --project-id <ProjectID> --assigned-to <UserID>
  ### Delete:
    python main.py task delete --id <TaskID> 
  ### List:
    python main.py task list {outputs saved users from task.json}
  ### Update:
    python main.py task update --id <TaskID> --status <newStatus (options:"todo", "in-progress", "done")>

