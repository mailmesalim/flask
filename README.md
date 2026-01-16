DOCKER COMMANDS REFERENCE
=========================

1. docker -v
   → Check Docker version

2. docker pull <image_name>
   → Download an image from Docker Hub
   Example: docker pull docker/getting-started

3. docker images
   → List all local images

4. docker run -d -p <host_port>:<container_port> <image_name>
   → Run container in detached mode with port mapping
   Example: docker run -d -p 80:80 docker/getting-started

5. docker run -p <host_port>:<container_port> <image_name>
   → Run container in foreground with port mapping
   Example: docker run -p 5000:5000 welcome-app

6. docker ps
   → List running containers

7. docker stop <container_id>
   → Stop a running container
   Example: docker stop d92b1af6f095

8. docker image rm -f <image_id>
   → Force remove an image
   Example: docker image rm -f d79336f4812b

9. docker login
   → Authenticate with Docker Hub

10. docker build -t <image_name> .
    → Build image from Dockerfile with a tag
    Example: docker build -t welcome-app .

11. docker tag <source_image> <target_image>
    → Create a new tag for an image (for pushing to registry)
    Example: docker tag welcome-app mailmesalim/welcome-app

12. docker push <image_name>:<tag>
    → Push image to Docker Hub
    Example: docker push mailmesalim/welcome-app:latest

docker compose up
docker compose down
docker compose stop    

Install git cli
check 
  git version

  git config --global user.name "xxx"

  git config --global user.email "xxx@gmail.com"  