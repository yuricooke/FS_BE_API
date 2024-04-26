.PHONY: build run images remove-image list-containers stop-container remove-container

build:
	docker build -t rest-api . && docker run -p 5000:5000 rest-api

run: build
	docker run -p 5000:5000 rest-api

images:
	docker images

remove-image:
	@echo "Use: make remove-image IMAGE_ID=<IMAGE ID>"

list-containers:
	docker container ls --all

stop-container:
	@echo "Use: make stop-container CONTAINER_ID=<CONTAINER ID>"

remove-container:
	@echo "Use: make remove-container CONTAINER_ID=<CONTAINER ID>"