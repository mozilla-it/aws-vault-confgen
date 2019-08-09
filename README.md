# aws-vault-confgen thingamabobber
Generates an aws config file for aws-vault, this is very specific to mozilla
IT-SRE group use at own risk

## Usage
```
docker pull itsre/aws-vault-confgen:latest
cd itsre-accounts
docker run --rm -it -v $(pwd):/data itsre/aws-vault-confgen -u elim -i ./accounts/mozilla-itsre/terraform.tfvars
```
