# Py-SSH-SCP Client
A pyton implementation of ssh and scp client. 

The native scp and ssh clients dont work on kube as the container might have been started with a pseudo user. Running the scp and ssh commands results to 

```bash
User xxxx not found
```

## Installing Yum dependencies from cache
```
$ yum install -y package -C
```

## Building Wheel Packages for Offline Installation
```
$ pip wheel --wheel-dir=/tmp/SomePackage SomePackage
```

## Installating Wheel Packages from Cache
```
$ pip install --no-index --find-links=/tmp/SomePackage SomePackage
```