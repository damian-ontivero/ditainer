# Dependency Inection Container for Python

This is a basic Dependency Inection Container for Python.

## How to use it
At the moment, `ditainer` can only load dependencies from yaml files.

Dependencies are treated as services.
These services are classes that can receive arguments to be initialized or not.
It is also possible to initialize these services through their factory methods, which can also accept arguments.
Additionally, these services can be tagged with a tag.

Arguments can be simple, a reference to another service, or a list of all services with a specific tag.

An example of yaml file could be:

```yaml
services:
  - id: DBSession
    module: my_module.db
    class: DBSession
    factory: create_session

  - id: UserRepository
    module: my_module.user.repository
    class: MySqlUserRepository
    arguments:
      - !ref DBSession

  - id: QueryBus
    module: my_module.query_bus
    class: InMemoryQueryBus
    arguments:
      - !tagged query_handler

  - id: UserFindByIDQueryHandler
    module: my_module.user.find_by_id_query_handler
    class: UserFindByIDQueryHandler
    arguments:
      - !ref UserRepository
    tags:
      - query_handler

  - id: UserFindByCodeQueryHandler
    module: my_module.user.find_by_code_query_handler
    class: UserFindByCodeQueryHandler
    arguments:
      - !ref UserRepository
    tags:
      - query_handler

```

Each service must have id, module and class.
If the service has no id, module or class, there will be an error.

`ditainer` can also understand an import file with different files to load:

```yaml
imports:
  - { resource: "./services_1.yaml" }
  - { resource: "./services_2.yaml" }
  - { resource: "./services_3.yaml" }

```

### Start using ditainer
Once the yaml files are ready:

```python
import os

from ditainer.container import Container
from ditainer.loader import YAMLLoader


container = Container()
loader = YAMLLoader(container)
loader.load(os.path.join(os.path.dirname(__file__), "imports.yaml"))

```


```python
from my_module import container
from my_module.user import User
from my_module.user.find_by_id_query import UserFindByIdQuery

def get_user() -> User:
  query_bus = container.get("QueryBus")
  query = UserFindByIdQuery(123)
  
  user = query_bus.ask(query)
  return user
```

You can find more examples in the tests folder.

Based on: https://www.npmjs.com/package/node-dependency-injection
