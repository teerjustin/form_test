from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        # self.name = data['dojo_name']
        # self.location = data['location']
        # self.language = data['language']
        # self.comment = data['comment']
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        print(data, 'THIS IS DATA THIS IS DATA')
        query = "INSERT INTO dojos (dojo_name, location, language, comment, created_at, updated_at) " \
        "VALUES (%(dojo_name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"

        print(query, 'THIS IS QUERYYYY')
        print(data, 'this is something else')

        dojo_id = connectToMySQL("dojo_survey_schema").query_db(query, data)

        dojo_obj_copy = {
            "dojo_name": data['dojo_name'],
            "dojo_location": data['location'],
            "dojo_language": data['language'],
            "dojo_comment": data['comment'],
            "dojo_id": dojo_id
        }

        return dojo_obj_copy

    @staticmethod
    def validate_dojo(post_data):
            is_valid = True # we assume this is true
            if len(post_data['dojo_name']) < 3:
                flash("Name must be at least 3 characters.")
                is_valid = False
            return is_valid