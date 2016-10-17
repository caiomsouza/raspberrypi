echo "Send files to S3"
sudo mv /opt/file_mgmt/to_process/* /opt/file_mgmt/to_s3/
echo "Files moved"
aws s3 cp  /opt/file_mgmt/to_s3/ s3://iot-raspberrypi --recursive
echo "Files sent to S3"
sudo rm -rf /opt/file_mgmt/to_s3/*
echo "Files deleted"
echo "Files from Raspberry Sensor sent to S3 Bucket with success"
