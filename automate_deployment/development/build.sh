#!/bin/bash

# Log in to your image repo
docker login quay.io
# Build your image
docker build -t quay.io/olagoldhackxx/climatewavers-waverX-NLP:v1 .
# Push image to repo
docker push quay.io/olagoldhackxx/climatewavers-waverX-NLP:v1
