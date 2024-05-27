import json

# on the CLI, enter the line below to get a list of all projects in json
# gcloud projects list --format="json" > projects.json

# read the file generated from above
with open("projects.json", "r") as f:
 projects = json.load(f)

# update with new billing account ID
new_billing_account_id = "YOUR_NEW_BILLING_ACCOUNT_ID"


for project in projects:
    project_name = project["projectId"]
    ptype = project["parent"]["type"]

    if ptype == 'organization':
        # gcloud billing projects link PROJECT_ID --billing-account=ACCOUNT_ID 
        command = f"gcloud billing projects link {project_name} --billing-account={new_billing_account_id}"
        # print(f"Updating billing for project: {project_name} type: {ptype}")
        # print out the command lines to review the command line generated
        print(command)
        # when ready enable the command below and comment out the line above
        # os.system(command)
    else:
        print(f"Skipping resource: {project_name} type: {ptype}")