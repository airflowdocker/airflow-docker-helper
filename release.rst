RELEASE_TYPE: minor

* Added a :mod:`airflow_docker_helper.codec` to encode data from json serializable python primitives to ascii and back again.
* Added host and client staticmethods for encoding and decoding data.
* Added a console_script entry_point :func:`airflow_docker_helper.call.call` to enable an airflow-docker native extension for executing python functions from :class:`airflow_docker.operator.BaseDockerOperator` classes.
* Added release branch automation with releasely

Authors:

* Hunter Senft-Grupp

