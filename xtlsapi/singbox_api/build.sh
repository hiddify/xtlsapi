sudo apt install -y protobuf-compiler
protoc ./stats.proto --python_out=./
python3 -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ ./stats.proto
