
docker-build-local:
	docker image build --build-arg SETTINGS=mytestsite.settings.docker-local -t mirror-admin-local .

docker-run-local:
	docker container run -p 8000:8000 mirror-admin-local

docker-build-staging:
	docker image build --build-arg SETTINGS=mytestsite.settings.docker-staging -t mirror-admin-staging .

docker-run-staging:
	docker container run -p 8000:8000 mirror-admin-staging

staging-tunnel:
	ssh -i ~/.ssh/mirror-staging-bastion.pem -fN -l ec2-user -L 54321:mirror-staging-mirror.cuw7frnyz7b7.eu-west-2.rds.amazonaws.com:5432 ec2-18-130-158-254.eu-west-2.compute.amazonaws.com -v

stop-tunnels:
	killall ssh
