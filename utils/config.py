import os


def load_config():
    from app import app
    from dotenv import load_dotenv
    load_dotenv()
    app.config['MODEL_PATH'] = os.environ.get('MODEL_PATH')
    app.config['S3_BUCKET_NAME'] = os.environ.get('S3_BUCKET_NAME')
    app.config['PORT'] = os.environ.get('PORT', 8080)
    app.config['DEBUG'] = True

    return app
