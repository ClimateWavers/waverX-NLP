#!/bin/bash

# oc and kubectl must be installed to deploy with this script
#Get ENV variable
source .env
token=$TOKEN

echo "Login to openshift"
oc login --token=$token --server=https://api.sandbox-m4.g2pi.p1.openshiftapps.com:6443

echo "Deploying deployment"
kubectl apply -f k8s/deployment.yaml
echo "Deploying service"
kubectl apply -f k8s/service.yaml
echo "Deploy route"
kubectl apply -f k8s/route.yaml