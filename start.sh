# start.sh
export FLASK_APP=app
# export FLASK_ENV=development
export ES_HOST_URL=http://lad-elasticsearch-service-aiops-prod-prometheus-scrape.cloud.paas.psi.redhat.com
flask run
