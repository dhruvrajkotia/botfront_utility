from flask import Flask, jsonify
import os
import logging
import boto3
from botocore.exceptions import ClientError
import os
from utils.config import load_config

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        with open(file_name, "rb") as f:
            s3_client.upload_fileobj(f, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

app = Flask(__name__)

@app.route("/health-checkup")
def health_checkup():
    return jsonify({
        'ok': True
    })

@app.route("/")
def home():
    return jsonify({
        'ok': True
    })

@app.route("/sync_model")
def sync_model():
    status = upload_file(app.config.get('MODEL_FILE'),
                         app.config.get('S3_BUCKET_NAME'))
    return jsonify({'status': status})


if __name__ == "__main__":
    app = load_config()
    app.run(host='0.0.0.0', debug=app.config.get('DEBUG'), port=app.config.get('PORT'))
