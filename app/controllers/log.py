from flask_restful import Resource
from app.models.user import User
from app.models.project import Project
from app.models.app import App
from app.models.log import AppLog
from app.models.log import UserLog
from app.models.log import ProjectLog

class LogsView(Resource):
    
    #Saving user logs
    def saveUserLog(id, user_id, action):
        # check for existing user based on user_id
        existing_user = User.find_first(
            id=user_id)

        if existing_user:

            if (action == 1):
                action = "Activated project."
            
            elif (action == 0):
                action = "Disabled project."
            
            elif (action == 5):
                action = "Deleted project."

            new_log = UserLog(
               user_id = id,
               action = action,
               performed_by = user_id
            )

            saved = new_log.save()

            if not saved:
                return dict(status='fail', message='Internal Server Error'), 500

            return dict(status='success', message='Log saved'), 201


        return dict(
            status='fail',
            message="User does not exist."
        ), 500
       


    #Saving project logs
    def saveProjectLog(project_id, user_id, action):

        # check for existing project based on project_id
        existing_project = Project.find_first(
            id=project_id)

        if existing_project:

            if (action == 1):
                action = "Activated project."
            
            elif (action == 0):
                action = "Disabled project."
            
            elif (action == 5):
                action = "Deleted project."


            new_log = ProjectLog(
               project_id = project_id,
               action = action,
               performed_by = user_id
            )

            saved = new_log.save()

            if not saved:
               return dict(status='fail', message='Internal Server Error'), 500

        else:
            return dict(
                status='fail',
                message="Project does not exist."
            ), 500



    #Saving app logs
    def saveAppLog(app_id, user_id, action):

        # check for existing app based on app_id
        existing_app = App.find_first(
            id=app_id)

        if existing_app:

            if (action == 1):
                action = "Activated application."
            
            elif (action == 0):
                action = "Disabled application."
            
            elif (action == 5):
                action = "Deleted application."


            new_log = AppLog(
               app_id = app_id,
               action = action,
               performed_by = user_id
            )

            saved = new_log.save()

            if not saved:
                return dict(status='fail', message='Internal Server Error'), 500

            return dict(status='success', message='Log saved'), 201


        return dict(
            status='fail',
            message="Project does not exist."
        ), 500