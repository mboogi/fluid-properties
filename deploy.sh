./#!/bin/sh
docker build --tag bogmilos/fluid-properties:2.0.5 .
sudo docker login
sudo docker push bogmilos/fluid-properties:2.0.5