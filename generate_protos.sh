#!/bin/bash

python3 -m grpc_tools.protoc -I./proto --python_out=hs-plugins --grpc_python_out=hs-plugins ./proto/*.proto