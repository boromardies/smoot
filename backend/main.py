# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]

from flask import Flask, request, json
import pg8000

import math

conversion_dict = {
    #these are the prefix conversions
    'da': math.pow(10,1),
    'h': math.pow(10,2),
    'k': math.pow(10,3),
    'M': math.pow(10,6),
    'G': math.pow(10,9),
    'T': math.pow(10,12),
    'P': math.pow(10,15),
    'E': math.pow(10,18),
    'Z': math.pow(10,21),
    'Y': math.pow(10,24),
    'c': math.pow(10,-2),
    'm': math.pow(10,-3),
    'u': math.pow(10,-6),
    'n': math.pow(10,-9),
    'p': math.pow(10,-12),
    'f': math.pow(10,-15),
    'a': math.pow(10,-18),
    'z': math.pow(10,-21),
    'y': math.pow(10,-24),
    #these are the unit conversions
    'A': 100*math.pow(10,-12),
    'in': 25.4*math.pow(10,-3),
    'ft': .3048,
    'yd': .9144,
    'mile': 1609.344,
    'league': 4800,
    'fathom': 1.8288,
    'chain': 20.1168,
    'rod': 5.0292,
    'furlong': 201.168,
    'potrzebie': 2.2633485*math.pow(10,-3),
    'altuve': 1.65,
    'parsec': 3.086*math.pow(10,16),
    'beard-second': math.pow(10,-9),
    'smoot': 1.7018,
}



app = Flask(__name__)
#con = pg8000.connect("postgres",host="34.73.215.171",password="jeff")

@app.route('/query')
def query_api():
    value = request.args.get('value')
    unit = request.args.get('unit')
    
    # Insert SQL code here
    
    #con.run("SELECT TOP 2 * FROM [myTable] WHERE Unit = *{} ORDER BY ABS( "Converted Value" - {})".format(unit,value)) 
    
    
    #Placeholder code for testing

    tname = value
    tvalue = value
    bname = value
    bvalue = value
    
    return {
            "tname" : tname,
            "tvalue" : tvalue,
            "bname" : bname,
            "bvalue" : bvalue
            }


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
