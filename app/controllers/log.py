from flask_restful import Resource
from app.models.user import User
from app.models.project import Project
from app.models.app import App
import json
from app.models.log import AppLog
from app.models.log import UserLog
from app.models.log import ProjectLog
from app.schemas import UserLogsSchema, ProjectLogsSchema, AppLogsSchema

class LogsView(Resource):
    
    def get(self):
        user_logs_schema = UserLogsSchema(many=True)
        user_logs = UserLog.find_all()
        user_logs_data, errors = user_logs_schema.dumps(user_logs)

        if errors:
          return dict(status='fail', message=errors), 400

        user_logs_list = json.loads(user_logs_data)

        for log in user_logs_list:
            performed_by = User.get_by_id(log['performed_by'])

            if performed_by:
               log['user'] = performed_by.name        
            
            else:
                return dict(
                    status='fail',
                    message=f'User does not exists'
                ), 404
        

            user = User.get_by_id(log['user_id'])

            if user:
               log['entity'] = user.name        
            
            else:
                return dict(
                    status='fail',
                    message=f'User does not exists'
                ), 404
        


        project_logs_schema = ProjectLogsSchema(many=True)
        project_logs = ProjectLog.find_all()
        project_logs_data, errors = project_logs_schema.dumps(project_logs)

        if errors:
          return dict(status='fail', message=errors), 400

        project_logs_list = json.loads(project_logs_data)

        for log in project_logs_list:
            user = User.get_by_id(log['performed_by'])

            if user:
               log['user'] = user.name        
            
            else:
                return dict(
                    status='fail',
                    message=f'User does not exists'
                ), 404
        

            project = Project.get_by_id(log['project_id'])

            if project:
               log['entity'] = project.name        
            
            else:
                return dict(
                    status='fail',
                    message=f'Project does not exists'
                ), 404
                

        app_logs_schema = AppLogsSchema(many=True)
        app_logs = AppLog.find_all()
        app_logs_data, errors = app_logs_schema.dumps(app_logs)

        if errors:
          return dict(status='fail', message=errors), 400

        app_logs_list = json.loads(app_logs_data)

        for log in app_logs_list:
            user = User.get_by_id(log['performed_by'])

            if user:
               log['user'] = user.name        
            
            else:
                return dict(
                    status='fail',
                    message=f'User does not exists'
                ), 404
        

            app = App.get_by_id(log['app_id'])

            if app:
               log['entity'] = app.name        
            
            else:
                return dict(
                    status='fail',
                    message=f'App does not exists'
                ), 404

        return dict(
            status='success',
            data=dict(
                app_logs=app_logs_list, project_logs=project_logs_list, user_logs=user_logs_list)
        ), 200
                
        

                

    #Saving user logs
    def saveUserLog(id, user_id, action, comment):
        # check for existing user based on user_id
        existing_user = User.find_first(
            id=user_id)

        if existing_user:

            if (action == 1):
                action = "Activated user."
            
            elif (action == 0):
                action = "Disabled user."
            
            elif (action == 5):
                action = "Deleted user."

            new_log = UserLog(
               user_id = id,
               action = action,
               performed_by = user_id,
               comment = comment
            )

            saved = new_log.save()

            if not saved:
                return dict(status='fail', message='Internal Server Error'), 500

            return dict(status='success', message='Log saved'), 201


        return dict(
            status='fail',
            message="User does not exist."
        ), 404
       


    #Saving project logs
    def saveProjectLog(project_id, user_id, action, comment):

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
               performed_by = user_id,
               comment = comment
            )

            saved = new_log.save()

            if not saved:
               return dict(status='fail', message='Internal Server Error'), 500

            return dict(status='success', message='Log saved'), 201
        
        return dict(
            status='fail',
            message="Project does not exist."
        ), 404



    def saveProjectLogExt(project_id, action):

        # check for existing project based on project_id
        existing_project = Project.find_first(
            id=project_id)

        if existing_project:
            user = User.find_first(
            id=existing_project.owner_id)

            if user:
                new_log = ProjectLog(
                    project_id = project_id,
                    action = action,
                    performed_by = user.id
                )

                saved = new_log.save()

                if not saved:
                    return dict(status='fail', message='Internal Server Error'), 500

                return dict(status='success', message='Log saved'), 201


            return dict(
                status='fail',
                message="User does not exist."
            ), 404


        return dict(
            status='fail',
            message="Project does not exist."
        ), 404



    #Saving app logs
    def saveAppLog(app_id, user_id, action, comment):

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
               performed_by = user_id,
               comment = comment
            )

            saved = new_log.save()

            if not saved:
                return dict(status='fail', message='Internal Server Error'), 500

            return dict(status='success', message='Log saved'), 201


        return dict(
            status='fail',
            message="App does not exist."
        ), 404



    def saveAppLogExt(app_id, action):

        # check for existing app based on app_id
        existing_app = App.find_first(
            id=app_id)

        if existing_app:
            # check for existing project based on project_id
            existing_project = Project.find_first(
                id=existing_app.project_id)

            if existing_project:
                user = User.find_first(
                id=existing_project.owner_id)

                if user:
                    new_log = AppLog(
                        app_id = app_id,
                        action = action,
                        performed_by = user.id
                    )

                    saved = new_log.save()

                    if not saved:
                        return dict(status='fail', message='Internal Server Error'), 500

                    return dict(status='success', message='Log saved'), 201

                return dict(
                    status='fail',
                    message="User does not exist."
                ), 404

            return dict(
                status='fail',
                message="Project does not exist."
            ), 404

        return dict(
            status='fail',
            message="App does not exist."
        ), 404