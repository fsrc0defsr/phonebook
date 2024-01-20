On DjangoREST Implementation of uploading a table of employee contacts from a database for downloading in xml format

# user info 
login: user
password: Q123w456

### run prod:

docker compose -f docker-compose.prod.yml up

docker compose -f docker-compose.prod.yml down

### self-signed certificate:

openssl genrsa -out rootCA.key 2048

openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.pem
    #Common Name (e.g. server FQDN or YOUR name) []:localhost

touch create_certificate_for_domain.sh

touch v3.ext

chmod +x ./create_certificate_for_domain.sh

./create_certificate_for_domain.sh localhost

