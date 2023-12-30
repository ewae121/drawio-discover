# drawio-discover

Project that analyse Python sources to generate Drawio schema.

As plantUML and mermaid can not be updatable so easily, this project generate Drawio schema
that can be updatable by hand.

## Poetry usage

- Init poetry session:

```bash
poetry shell
```

- format the code:

```bash
black drawio_discover/
```

- lint the code

```bash
pylint drawio_discover/
pylint tests/
```

- run tests

```bash
pytests tests/
```