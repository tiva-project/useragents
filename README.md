<div align="center">
<img src="README_DOT_MD_RESOURCES/HEADER.png" width="100%" style="text-align-all:center; ">
</div>

# User Agent Device

By using this service, we can store all the information about users who connect to us on a specific device.

## Installation

We assume that you have created a Django project.

In the first step, you need to install the "useragents" and "django_user_agents" libraries.
You can do this by using your desired package managers.
Allow me not to say more about the installation of a package.

After installing the package, you should add this library to your project.

 ```python

INSTALLED_APPS = [
  ...,
  'useragents',
  'django_user_agents',
]

```

Then add the desired tables to the database by executing the "python manage.py migrate" command.

Finally, make the final settings.

```python
MIDDLEWARE = [
  ...,
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  ...,
  'useragents.services.UserAgentDeviceMiddleware',
]
```

Now you can easily see the activities of your users for using your software on a specific device in the Django admin
panel.

## Licence

Copyright (c) 2024 Horin Software Group

<div align="center">
<img src="README_DOT_MD_RESOURCES/HORIN2024.png" width="12%" style="text-align-all:center; ">
</div>

