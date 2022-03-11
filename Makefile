
docker-build-local:
	docker image build --build-arg SETTINGS=mytestsite.settings.docker-local -t mirror-admin-local .

docker-run-local:
	docker container run -p 8000:8000 mirror-admin-local

docker-build-staging:
	docker image build --build-arg SETTINGS=mytestsite.settings.docker-staging -t mirror-admin-staging .

docker-build-gunicorn-staging:
	docker image build --build-arg ADMIN_ENV=DOCKER-STAGING -f Dockerfile2 -t mirror-admin-gunicorn-staging .

docker-run-staging:
	docker container run -e ADMIN_ENV=STAGING -p 8000:8000 mirror-admin-staging

docker-run-gunicorn-staging:
	docker container run -p 8000:8000 mirror-admin-gunicorn-staging

staging-tunnel:
	ssh -i ~/.ssh/mirror-staging-bastion.pem -fN -l ec2-user -L 54321:mirror-staging-mirror.cuw7frnyz7b7.eu-west-2.rds.amazonaws.com:5432 ec2-18-130-158-254.eu-west-2.compute.amazonaws.com -v

stop-tunnels:
	killall ssh

run-local:
	ADMIN_ENV=LOCAL python3 manage.py runserver 0.0.0.0:8000 --settings mytestsite.settings.local

run-staging:
	ADMIN_ENV=STAGING python3 mytestsite/manage.py runserver 0.0.0.0:8000 --settings mytestsite.settings.staging

run-gunicorn-staging:
	cd mytestsite; ADMIN_ENV=STAGING gunicorn --bind 0.0.0.0:8000 mytestsite.wsgi 
