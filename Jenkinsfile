#!groovy

node {
  stage 'Checkout'
    checkout scm

  stage 'Create virtualenv'
    sh 'virtualenv -p python3 talkmeup-env'
    sh 'source talkmeup-env/bin/activate'

  stage 'Intall requirements'
    sh 'talkmeup-env/bin/pip install -r requirements.txt'

  stage 'Run test'
    sh 'talkmeup-env/bin/python talkmeup/manage.py test'

  stage 'Cleanup'
    sh 'deactivate'
    sh 'rm talkmeup-env -rf'
}
