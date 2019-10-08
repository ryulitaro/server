from flask import Flask, request
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app=flask_app,
          version="1.0",
          title="Member Manger",
          description="Manage various users of the application")

name_space = app.namespace('members', description='Main APIs')
model = app.model('Member Model',
                  {
                      'id': fields.String(required=True,
                                          description="ID of the member",
                                          help="ID cannot be blank."),
                      'name': fields.String(required=True,
                                            description="Name of the member",
                                            help="Name cannot be blank."),
                      'age': fields.String(required=False,
                                           description="age of the member",
                                           help="Name can be blank."),
                  })

members = dict()


@name_space.route("/")
class MemberList(Resource):
    def get(self):
        """
        returns list of members
        """
        return members

    @app.expect(model)
    def post(self):
        """
        Adds a new member to the list
        """
        body = request.json
        id = body['id']
        members[id] = body


@name_space.route("/<id>")
class Member(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'Specify the Id associated with the person'})
    def get(self, id):
        """
        get a member
        """
        return members[id]

    @app.expect(model)
    def put(self, id):
        """
        edit a member detail
        """

# import json
#
# from flask import Flask, jsonify
# from flask import request as flask_request
#
# app = Flask(__name__)
#
# members = dict()
#
#
# @app.route('/', methods=['GET'])
# def root():
#     return "This is root"
#
#
# @app.route('/members')
# def get_all_memebers():
#     return jsonify(members)
#
#
# @app.route('/members', methods=['POST'])
# def add_members():
#     body = json.loads(flask_request.data)
#     id = body['id']
#     members[id] = body
#     return "OK"
#
#
# @app.route('/members/<id>')
# def get_member(id):
#     return jsonify(members[id])
