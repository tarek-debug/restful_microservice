from flask import Flask
from flask_restx import Api, Resource, fields, reqparse, abort
import json
import os

# Initialize Flask and Flask-RESTX
app = Flask(__name__)
api = Api(app, version='1.0', title='Diary API',
          description='A simple diary API')

# Namespace for diary operations
ns = api.namespace('diary', description='Diary operations')

# Diary model for serialization and deserialization
diary_model = api.model('Diary', {
    'title': fields.String(required=True, description='The diary entry title'),
    'content': fields.String(required=True, description='The diary entry content'),
})

# Construct the path to the diary.json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIARY_FILE = os.path.join(BASE_DIR, 'routes', 'diary.json')

def load_entries():
    """Load diary entries from the file."""
    try:
        with open(DIARY_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_entries(entries):
    """Save diary entries to the file."""
    with open(DIARY_FILE, 'w') as file:
        json.dump(entries, file, indent=4)

@ns.route('/')
class DiaryList(Resource):
    @ns.doc('list_diaries')
    @ns.marshal_list_with(diary_model)
    def get(self):
        """List all diary entries"""
        return load_entries()

    @ns.doc('create_diary')
    @ns.expect(diary_model)
    @ns.marshal_with(diary_model, code=201)
    def post(self):
        """Create a new diary entry"""
        entries = load_entries()
        new_entry = api.payload
        # Use title as the unique ID
        new_entry['id'] = new_entry['title']
        # Check for uniqueness
        if any(entry['id'] == new_entry['id'] for entry in entries):
            abort(400, "Title already exists as an ID")
        entries.append(new_entry)
        save_entries(entries)
        return new_entry, 201

@ns.route('/<string:title>')
@ns.response(404, 'Diary entry not found')
@ns.param('title', 'The diary entry title')
class Diary(Resource):
    @ns.doc('get_diary')
    @ns.marshal_with(diary_model)
    def get(self, title):
        """Fetch a diary entry given its title"""
        entries = load_entries()
        for entry in entries:
            if entry['id'] == title:  # Use title to fetch the diary
                return entry
        abort(404)

    @ns.doc('delete_diary')
    @ns.response(204, 'Diary entry deleted')
    def delete(self, title):
        """Delete a diary entry given its title"""
        entries = load_entries()
        entries = [entry for entry in entries if entry['id'] != title]
        save_entries(entries)
        return '', 204

    @ns.expect(diary_model)
    @ns.doc('update_diary')
    @ns.marshal_with(diary_model)
    def put(self, title):
        """Update a diary entry given its title"""
        updated_data = api.payload
        entries = load_entries()
        for entry in entries:
            if entry['id'] == title:
                entry.update(updated_data)  # Update the entry with new data
                save_entries(entries)
                return entry
        abort(404, "Diary entry not found")

if __name__ == '__main__':
    app.run(debug=True)
