# sudo apt install -y protobuf-compiler
#wget https://github.com/protocolbuffers/protobuf/releases/download/v23.1/protoc-23.1-linux-aarch_64.zip
../../bin/protoc ./stats.proto --python_out=./
../../bin/protoc ./extensions.proto --python_out=./
python3 -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ ./stats.proto
python3 -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ ./extensions.proto
