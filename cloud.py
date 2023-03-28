import scratchconnect

user = scratchconnect.ScratchConnect("Username", "Password")
project = user.connect_project(project_id=1)
variables = project.connect_cloud_variables()
variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
variables.get_cloud_variable_value(variable_name="Name", limit=100)  # Returns the cloud variable value
# Program to set cloud variables:
set = variables.set_cloud_variable(variable_name="Name", value=123)  # Set a Cloud Variable
if set:
    print("Cloud Variable Updated!")
