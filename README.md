# Dependency Inection Container for Python

This is a basic Dependency Inection Container for Python.

## How to use it

At the moment, `ditainer` can only load dependencies from yaml files.

A dependency is treated as a service.
A service is a class and could receive arguments to be initialized.
It is also possible to initialize a class through its factory, which may also require arguments.
Additionally, a service can be tagged.

Types of arguments:

- Simple. Just the literal argument.
- A reference to another service. The prefix `!ref` followed by the id of the other service.
- All services tagged with a specific tag. The prefix `!tagged` followed by the tag.

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
  query_bus = container.find("QueryBus")
  query = UserFindByIdQuery(123)

  user = query_bus.ask(query)
  return user
```

It is also possible to find services by tags:

```python
from my_module import container
from my_module.user import User
from my_module.user.find_by_id_query import UserFindByIdQuery


query_handlers = container.find_tagged("query_handler")
```


You can find more examples in the tests folder.

Based on: https://www.npmjs.com/package/node-dependency-injection
