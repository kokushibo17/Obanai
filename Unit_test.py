import pytest

from app import create_app, db

from app.models import User, JobApplication

@pytest.fixture

def client():

    # Set up a test Flask app with a test database

    app = create_app('test')

    app.config['TESTING'] = True

    with app.test_client() as client:

        with app.app_context():

            db.create_all()

            yield client

            db.session.remove()

            db.drop_all()

def test_create_user(client):

    # Test creating a new user

    user = User(username='testuser', email='testuser@example.com')

    user.set_password('password')

    db.session.add(user)

    db.session.commit()

    assert user in db.session

def test_create_job_application(client):

    # Test creating a new job application

    user = User(username='testuser', email='testuser@example.com')

    user.set_password('password')

    db.session.add(user)

    db.session.commit()

    application = JobApplication(title='Test Job', company='Test Company', user_id=user.id)

    db.session.add(application)

    db.session.commit()

    assert application in db.session
