from flask import Flask, jsonify, request
from CoolPropService import get_available_fluids, get_numeric_property

app = Flask(__name__)


@app.route('/fluids', methods=['GET'])
def fluids():
    if request.method == 'GET':
        data = get_available_fluids()
        return jsonify(data)


@app.route('/property', methods=['GET'])
def get_fluid_properties():
    if request.method == 'GET':
        output = request.args.get('output')
        name1 = request.args.get('name1')
        prop1_str = request.args.get('prop1')
        prop1 = float(prop1_str)
        name2 = request.args.get('name2')
        prop2_str = request.args.get('prop2')
        prop2 = float(prop2_str)
        fluid_name = request.args.get('fluid')
        data = get_numeric_property(output, name1, prop1, name2, prop2, fluid_name)
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False)
