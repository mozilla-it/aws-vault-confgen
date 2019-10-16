# aws-vault-confgen thingamabobber
Generates an aws config file for aws-vault, this is very specific to mozilla
IT-SRE group use at own risk

## Usage
You can use docker to do this
```
docker pull itsre/aws-vault-confgen:latest
cd itsre-accounts
docker run --rm -it -v $(pwd):/data itsre/aws-vault-confgen -u elim -i ./accounts/mozilla-itsre/terraform.tfvars
```

If you don't want to use docker you can do the following
```
git clone git@github.com:mozilla-it/itsre-accounts.git
git clone git@github.com:mozilla-it/aws-vault-confgen.git
cd aws-vault-confgen
# This is a hack
pip uninstall ply; pip uninstall pyhcl; pip install ply; pip install pyhcl
pip install -r requirements.txt
./generate.py -u <your ldap username> -i <path to itsre-accounts>/accounts/mozilla-itsre/terraform.tfvars
```
