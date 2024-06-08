# Dependency Inection Container for Python

This is a basic Dependency Inection Container for Python.

## How to use it
At the moment `ditainer` only understands `yaml` files and a dependency is trated as `service`.

It is possible to declare a `service` as a `class`, `method` or `variable`.

There is also the possibility to add `tags` to each `service`.

A `class` or a `method` can receive a list of `arguments`.

`arguments` can be `normal`, `reference` to another `service` or a list with all the other `services` with an specific `tag`.

An example of yaml file could be:

```yaml
services:
  DBSession:
    module: my_module.db
    variable: mysql_session

  UserRepository:
    module: my_module.user.repository
    class:
      name: MySqlUserRepository
      arguments:
        - !ref DBSession

  QueryBus:
    module: my_module.query_bus
    class:
      name: InMemoryQueryBus
      arguments:
        - !tagged query_handler

  UserFindByIDQueryHandler:
    module: my_module.user.find_by_id_query_handler
    class:
      name: UserFindByIDQueryHandler
      arguments:
        - !ref UserRepository
      tags:
        - query_handler

  UserFindByCodeQueryHandler:
    module: my_module.user.find_by_code_query_handler
    class:
      name: UserFindByCodeQueryHandler
      arguments:
        - !ref UserRepository
      tags:
        - query_handler

```

Every `service` has to have a `service_id` and a `module`.
If the `service` does not have either `class`, `method` or `variable` there will be an error.

`ditainer` can also understand an *import file* with different files to load:

```yaml
imports:
  - { resource: "./services_1.yaml" }
  - { resource: "./services_2.yaml" }

```

### Start using ditainer
Once the `yaml` files are ready:

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
