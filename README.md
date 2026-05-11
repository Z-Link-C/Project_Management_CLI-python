# commands:
## Python main.py user [add, list, delete]
  ### Add:
    Python main.py user add --name <Name> --email <Email>
  ### Delete:
    Python main.py user delete --id <UserID> 
  ### List:
    Python main.py user list {outputs saved users from users.json}
    
## Python main.py project [add, list, delete]
  ### Add:
    Python main.py project add --title <Title> --description <Description(optional)> --due-date <Date(yyyy-mm-dd fromat)> --owner-id <UserID>
  ### Delete:
    Python main.py project delete --id <ProjectID> 
  ### List:
    Python main.py project list {outputs saved users from project.json}
## Python main.py task [add, list, update, delete]
  ### Add:
    Python main.py task add --title <Title> --status <Status (options:"todo", "in-progress", "done")> --project-id <ProjectID> --assigned-to <UserID>
  ### Delete:
    Python main.py task delete --id <TaskID> 
  ### List:
    Python main.py task list {outputs saved users from task.json}
  ### Update:
    Python main.py task update --id <TaskID> --status <newStatus (options:"todo", "in-progress", "done")>

