## Chat Application
This project is a chat application based on the following tech stack<sup>[1](#footnote1)</sup>:
- Docker
- Django 3
    - asgi<sup>[2](#footnote2)</sup>
    - python-socketio
    - djoser
- React
- Socket.IO

### Start the project
- Install Docker
- Clone the repo
- Add `.env` in `./django` with content
    ```
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_SSL_MODE=off
    SECRET_KEY=q$w!oi*7)x$=c#s(9+h@2prnbas$rsy-eh(#xm5fkd(vq3%^7o

    EMAIL_HOST={your-email-host}
    EMAIL_HOST_USER={your-email-host-user}
    EMAIL_HOST_PASSWORD={your-email-host-password}

    DOMAIN=localhost:3000
    SITE_NAME=socketio
    ```
- Add `.env` in `./postgres` with content
    ```
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_SSL_MODE=off
    ```
- Add folders `./django/storage/static` and `./django/storage/media` that will contain Django's static & media files
- Open terminal at root level of the repo, and run
    ```
    (root) ➜ docker-compose up
    ```
- Open the browser at http://localhost:8000/

### Fabric3
An additional `fabfile.py` module has been added to allow certain operations with Docker containers (e.g., ssh inside a container). To use it, you need to: 
- Install Fabric3
- Open terminal at root level of the repo, and run one of the commands defined in the fabfile.py module, e.g., you can ssh inside the django container by simply running:
    ```
    (root) ➜ fab ssh:django
    ```

### Windows Issues
When running on Windows, be sure to setup Docker to run in Linux mode. Moreover, it can happens that `git` automatically restyled the EOL (End Of Line) of bash files. To avoid this problem, run this global command
```
git config --global core.autocrlf input
```
This command avoids the EOL (End Of Line) replacement. The latter is due to git which automatically reformat the file based on the current OS. As a conseguence, Linux-style EOL are replaced with Windows-style EOL.

### TODO
Serve the client from a React application

<a name="footnote1">1</a>: The example is inspired by [this](https://github.com/miguelgrinberg/python-socketio/tree/master/examples/server/asgi) repo.

<a name="footnote2">2</a>: An analogous example in which wsgi is used instead of asgi is given [here](https://github.com/miguelgrinberg/python-socketio/tree/master/examples/server/wsgi/django_example).