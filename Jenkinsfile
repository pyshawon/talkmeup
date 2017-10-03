#!groovy

node {
  stage 'Checkout'
    checkout scm

  stage 'Install python 3'
    sh 'sudo yum -y install python35'
    sh 'sudo yum -y install python35-setuptools'
    sh 'sudo easy_install-3.5 pip'

  stage 'Install virtualenv'
    sh 'sudo python3 -m pip install virtualenv'

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
