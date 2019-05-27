# Start project with this core file

### Django 2.2.1

## Installation

Install requirements ...
```
pip install -r requirements\local.txt
```

Create a file `env.ini`.

Copy the code inside `env.template.ini` to `env.ini`.

```
[PRODUCTION]
DATABASE_ENGINE =
DATABASE_NAME =
DATABASE_USER =
DATABASE_PASSWORD =
DATABASE_HOST =
DATABASE_PORT =

[STAGING]
DATABASE_ENGINE =
DATABASE_NAME =
DATABASE_USER =
DATABASE_PASSWORD =
DATABASE_HOST =
DATABASE_PORT =

[LOCAL]
DATABASE_ENGINE =
DATABASE_NAME =
DATABASE_USER =
DATABASE_PASSWORD =
DATABASE_HOST =
DATABASE_PORT =

```

**Note:** Configure your database settings here.


#### Working With Multiple Settings Modules

You have to configure which `settings` module you want to use:
```
[SETTINGS]
CONFIG = config.settings.local
```

