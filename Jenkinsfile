#!groovy

node {
  stage 'Checkout'
    checkout scm

  stage 'Create virtualenv'
    sh 'virtualenv -p python3 talkmeup-env'
    sh 'source talkmeup-env/bin/activate'

  stage 'Intall requirements'
    sh 'cd talkmeup'
    sh 'pip install -r requirements.txt'

  stage 'Run test'
    sh 'python manage.py test'

  stage 'Cleanup'
    sh 'deactivate'
    sh 'cd ..'
    sh 'rm talkmeup-env -rf'
}
