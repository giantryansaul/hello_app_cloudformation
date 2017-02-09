#!/bin/bash

# Chef deployment
mkdir /etc/chef

cat > /etc/chef/client.rb << EOF
log_level        :info
log_location     STDOUT
chef_server_url  '{{chef_url}}'
EOF

curl -L https://www.getchef.com/chef/install.sh | bash

chef-client

# Hello app deployment
#yum install python-pip -y
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip install flask

cat > /var/local/hello_app.py << EOF
{{hello_app}}
EOF

python /var/local/hello_app.py