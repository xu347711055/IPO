from flask_restful import Resource, reqparse
from pmt.models.model import User
from pmt.models import db
from flask import jsonify, request, current_app

# parser = reqparse.RequestParser()
# parser.add_argument('username', 'email', 'enabled', 'admin')


class UserView(Resource):
    def get(self):
        users = User.query.all()
        current_app.logger.info(users)
        result = []
        for user in users:
            result.append({'id': user.gkey, 'username': user.name})
            current_app.logger.info(result)
        return jsonify(result)
        # return "andy"

    def post(self, **kwargs):
        # args = parser.parse_args()

        user = User(name=request.form['username'], email=request.form['email'], enabled=request.form['enabled'], admin=request.form['admin'])
        db.session.add(user)
        db.session.commit()

        return 'ok'
