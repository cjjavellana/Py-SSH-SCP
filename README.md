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

## Miscellaneous
If you have faced the error on MacOS X, here's the quick fix - add these lines to your ~/.bash_profile:
```bash  
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```
Credit goes to: https://coderwall.com/p/-k_93g/mac-os-x-valueerror-unknown-locale-utf-8-in-python