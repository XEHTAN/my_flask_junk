from application import app
from connetion import engine
from models import Role
from flask import request
from sqlalchemy.orm import Session
from flask import jsonify
from role_serializer import RoleSerializer


@app.route('/role', methods=['POST'])
def create_role():
    if request.form:
        try:
            session = Session(bind=engine)
            role = Role(
                name=request.form['name']
            )
            session.add(role)
            session.commit()
            print('success!')
            return jsonify({'status': 'success'})

        except Exception as e:
            print(e)
            return jsonify({'status': 'error'})


@app.route('/role', methods=['GET'])
def get_all_roles():
    try:
        session = Session(bind=engine)
        data_collection = session.query(Role).all()
        serialized_data = RoleSerializer.serialize_many(data_collection)
        return serialized_data

    except Exception as e:
        print(e)
        return jsonify({'status': 'error'})


@app.route('/role', methods=['POST'])
def update_role():
    if request.form:
        try:
            session = Session(bind=engine)
            data = session.query(Role)   #надо посмотреть в курсе. сделать силект по id. вроде нужно импортнуть
            updetedrole = UpdeteRole(
                name=request.form['name']
            )
            session.add(updetedrole)
            session.commit()
            print('success')
            return jsonify({'status': 'success'})

        except Exception as e:
            print(e)
            return jsonify({'status': 'error'})

@app.route('/role', methods=['POST'])
def delete_role():
    if request.form:
        try:
            session = Session(bind=engine)
            deletedrole = DelitedRole(
                name=request.form['name']
            )
            session.delete(deletedrole)
            session.commit()
            print('success')
            return jsonify({'status': 'success'})

        except Exception as e:
            print(e)
            return jsonify({'status': 'error'})
