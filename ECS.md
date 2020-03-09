##ECS
git clone https://github.com/linuxacademy/cda-2018-flask-app.git

to start docker:
`sudo service docker start`

to add current user to docker group:
`sudo usermod -a -G docker $USER`

then quit from ssh session with Ctrl-d and login again
to check docker status:
`docket info`

other usefull commands:
`docker build -t cda-flask-app .`
`docker imgae ls`

create ecr repo
`aws ecr create-repository --repository-name name-your-ecr` this step has to supply you a json with url - write it down

get login to ecr repo
`aws ecr get-login --region us-east-1 --no-include-email` will give the command to login

once logged in add a tag to your image - use url from create repo step
`docker tag cda-flask-app:latest url-from-step-ecr-create-repo`
push tagged image to ecr
`docker push url-from-step-ecr-create-repo`
in AWS console ECR/Clusters "Get Started" btn (with FARGATE)
-configure container with name and url (saved from before)
-edit definition task (task execution role select none and then ecsTaskExecutionRole again - otherwise error)
- service
- cluster
Create, wait until it finished creation, Go to service, task tab
click on the task, click on ENI (it opens EC2)
copy it's IPV public IP, paste to the browser
