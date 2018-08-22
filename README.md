# gnucash-portfolio-cli

Gnucash Portfolio CLI

If running a web UI (server + client) is problematic, here is the CLI interface to [GnuCash Portfolio](https://github.com/MisterY/gnucash-portfolio) functions, written in Python. This can be very useful if running the code on Android devices, for example.

Initially, there are a few simple scripts for providing the basic features. That might grow into a full CLI application at a later stage.

## Tips

Set the log level using `-v` parameter.

In general, it should be possible to set the log level with `--log=DEBUG` but this does not work when using argparse.

## Distribution

Create .pypirc file in your profile directory, containing:

```ini
[distutils]
index-servers =
    pypi
    test

[pypi]
repository: https://upload.pypi.org/legacy/
username: ****
password: ****

[test]
repository: https://test.pypi.org/legacy/
username: ****
password: ****
```

### Test Site

```console
python setup.py sdist upload -r test
```

### Production Site

```console
python setup.py sdist upload -r pypi
```