docker build -t 'bus-puppet' site-api
docker run -d --name 'bus-puppet' -p 5000:5000 'bus-puppet'

