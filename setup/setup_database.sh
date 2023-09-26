#!/bin/bash

docker pull postgres:15

docker run --name car_details -e POSTGRES_PASSWORD=secret_pass -d postgres
