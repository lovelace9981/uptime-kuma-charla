### This repository consist in two parts

#### Ansible

To deploy a new instance of uptime kuma fully automated, you just need to put your private 
IPv4 in the ```inventory.yml```, that private IP is the server, make sure that you can use
SSH public key auth for automatic auth.

#### Json

In this respository, we have a backup JSON to be deployed in the kuma service to have an initial
list of IP to monitorize.


#### automake.py

Is a basic script that appends to your JSON backup an list of domains, this scripts is initially limited
to monitoring HTTP or HTTPs. Make sure that your JSON have that minimal list to automake the append.


```json
{
    "version": "1.23.15",
    "notificationList": [],
    "monitorList": [
        {
            "id": 1,
            "name": "Sample ",
            "description": null,
            "pathName": "Sample ",
            "parent": 22,
            "childrenIDs": [],
            "url": "https://sample.net",
            "method": "GET",
            "hostname": null,
            "port": null,
            "maxretries": 0,
            "weight": 2000,
            "active": true,
            "forceInactive": false,
            "type": "http",
            "timeout": 48,
            "interval": 60,
            "retryInterval": 120,
            "resendInterval": 0,
            "keyword": null,
            "invertKeyword": false,
            "expiryNotification": false,
            "ignoreTls": false,
            "upsideDown": false,
            "packetSize": 56,
            "maxredirects": 10,
            "accepted_statuscodes": [
                "200-299"
            ],
            "dns_resolve_type": "A",
            "dns_resolve_server": "1.1.1.1",
            "dns_last_result": null,
            "docker_container": "",
            "docker_host": null,
            "proxyId": null,
            "notificationIDList": {},
            "tags": [
                {
                    "id": 1,
                    "monitor_id": 1,
                    "tag_id": 1,
                    "value": "",
                    "name": "Sample",
                    "color": "#D97706"
                }
            ],
            "maintenance": false,
            "mqttTopic": "",
            "mqttSuccessMessage": "",
            "databaseQuery": null,
            "authMethod": null,
            "grpcUrl": null,
            "grpcProtobuf": null,
            "grpcMethod": null,
            "grpcServiceName": null,
            "grpcEnableTls": false,
            "radiusCalledStationId": null,
            "radiusCallingStationId": null,
            "game": null,
            "gamedigGivenPortOnly": true,
            "httpBodyEncoding": "json",
            "jsonPath": null,
            "expectedValue": null,
            "kafkaProducerTopic": null,
            "kafkaProducerBrokers": [],
            "kafkaProducerSsl": false,
            "kafkaProducerAllowAutoTopicCreation": false,
            "kafkaProducerMessage": null,
            "screenshot": null,
            "headers": null,
            "body": null,
            "grpcBody": null,
            "grpcMetadata": null,
            "basic_auth_user": null,
            "basic_auth_pass": null,
            "oauth_client_id": null,
            "oauth_client_secret": null,
            "oauth_token_url": null,
            "oauth_scopes": null,
            "oauth_auth_method": "client_secret_basic",
            "pushToken": null,
            "databaseConnectionString": null,
            "radiusUsername": null,
            "radiusPassword": null,
            "radiusSecret": null,
            "mqttUsername": "",
            "mqttPassword": "",
            "authWorkstation": null,
            "authDomain": null,
            "tlsCa": null,
            "tlsCert": null,
            "tlsKey": null,
            "kafkaProducerSaslOptions": {
                "mechanism": "None"
            },
            "includeSensitiveData": true
        },
    ]
}
```


##### Automake, status codes.

In the internal code you can change the accepted_statuscodes key dict, this allows to accept 
all the HTTP responses, please adjust.

```json
            "accepted_statuscodes": ["200-299", "300-399", "400-499", "500-599"],

```