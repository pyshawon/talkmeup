#!groovy

node {
  stage 'Checkout'
    checkout scm

  stage 'Create virtualenv'
    sh 'virtualenv -p python3 talkmeup-env'

  stage 'Upgrade pip'
    sh 'talkmeup-env/bin/pip install --upgrade pip'

  stage 'Intall requirements'
    sh 'talkmeup-env/bin/pip install -r requirements.txt'

  stage 'Run test'
    sh 'talkmeup-env/bin/python manage.py test'

  stage 'Cleanup'
    sh 'rm talkmeup-env -rf'
}
