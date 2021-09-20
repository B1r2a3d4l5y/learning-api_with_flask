import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


items = []


class Item(Resource):
    

    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,  
    required=True,
     help="This field can not be blank!"
      )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {"message": "Item not found"},404

      


@classmethod
def find_by_name(cls, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM items WHERE name =?"
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    connection.close()

    if row:
        return {'item': row[0], 'price': row[1]}
        

    def post(self, name):
        if Item.find_by_name(name):
            return {"message": "An item with name '{}' already exits".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "IINSERT INTO items VALUES(?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item, 201

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, item), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "INSERT INTO items VALUES(?,?)"
            cursor.execute(query,(item['name']), item['price'])

            connection.commit()
            connection.close()
       
        return item, 201
        return {'item': row[0], 'price': row[1]}
        

    def post(self, name):
        if Item.find_by_name(name):
            return {"message": "An item with name '{}' already exits".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "IINSERT INTO items VALUES(?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item, 201

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, item), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "INSERT INTO items VALUES(?,?)"
            cursor.execute(query,(item['name']), item['price'])

            connection.commit()
            connection.close()
       
        return item, 201


class ItemList(Resource):
    def get(self):

        return {'items':  items}


class ItemList(Resource):
    def get(self):

        return {'items':  items}
