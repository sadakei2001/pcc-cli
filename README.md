# pcc-cli

Command line interface for PrimeCloud Controller.


## Usage

```
$ pcc [command] [options] --url https://hostname/auto-web/ --access-id XXXXXXXXXX --access-key YYYYYYYYYY
```

or

```
$ export PCC_URL=https://hostname/auto-web/
$ export PCC_ACCESS_ID=XXXXXXXXXX
$ export PCC_ACCESS_KEY=YYYYYYYYYY

$ pcc [command] [options]
```

## Example

### ListFarm API

Command

```
$ pcc list-farm
```

Output

```
{
    "Farms": {
        "Farm": {
            "Comment": "Example farm",
            "DomainName": "example.dev.primecloud-controller.org",
            "FarmName": "example",
            "FarmNo": "1"
        }
    },
    "SUCCESS": "true"
}
```

### ListInstance API

Command

```
$ pcc list-instance --farm-no 1
```

Output

```
{
    "Instances": {
        "Instance": {
            "Status": "STOPPED",
            "InstanceNo": "1",
            "Fqdn": "server1.example.dev.primecloud-controller.org",
            "PrivateIp": "",
            "PublicIp": "",
            "InstanceName": "server1"
        }
    },
    "SUCCESS": "true"
}
```


## Requirement

**pcc-cli** works on Python 2.6 or 2.7.
