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
import psycopg2
import os

# Remember - storing secrets in plaintext is potentially unsafe. Consider using
# something like https://cloud.google.com/secret-manager/docs/overview to help keep
# secrets secret.
db_user = os.environ["postgres"]
db_pass = os.environ["jeff"]
db_name = os.environ["dimension"]
db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
cloud_sql_connection_name = os.environ["smootthenorth:us-east1:dimension"]

pool = sqlalchemy.create_engine(

    # Equivalent URL:
    # postgres+pg8000://<db_user>:<db_pass>@/<db_name>
    #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
    sqlalchemy.engine.url.URL(
        drivername="postgresql+pg8000",
        username=db_user,  # e.g. "my-database-user"
        password=db_pass,  # e.g. "my-database-password"
        database=db_name,  # e.g. "my-database-name"
        query={
            "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                db_socket_dir,  # e.g. "/cloudsql"
                cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
        }
    ),
    **db_config
)

#os.system('./cloud_sql_proxy -instances=smootthenorth:us-east1:dimension=tcp:5432 &')
conn = psycopg2.connect(user="postgres",password="jeff",host='34.73.215.171',port='5432',database="dimension")
cur = conn.cursor()

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app, resources={"r/*": {"origins": "*"}})

@app.route('/query')
def query():
    value = request.args.get('value')
    
    # Insert SQL code here
    conn = psycopg2.connect(user="postgres",password="jeff",host='34.73.215.171',port='5432',database="dimension")
    cur = conn.cursor()
    cur.execute("SELECT * FROM lengthAgain ORDER BY ABS(converted - (%s))",(value,))
    out = cur.fetchmany(2)
    i=0
    j=1
    
    if out[0][3]<float(value):
        i=1
        j=0
        while out[i][3]<float(value):
            i=i+1
            cur.execute("SELECT * FROM lengthAgain ORDER BY ABS(converted - (%s))",(value,))
            out = cur.fetchmany(i+1)
    
    #Placeholder code for testing

    tname = out[i][4]
    tvalue = out[i][3]
    bname = out[j][4]
    bvalue = out[j][3]
    
    return {
            "tname" : tname,
            "tvalue" : tvalue,
            "bname" : bname,
            "bvalue" : bvalue
            }

cur.close()
conn.close()

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
