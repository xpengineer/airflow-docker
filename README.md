# Airflow Docker <!-- omit in toc -->

- [Runbook](#runbook)
- [DAG_ingestion_pipeline](#dag_ingestion_pipeline)
- [Chapter2](#chapter2)
  - [Section21](#section21)
  - [Section22](#section22)
    - [Subsection](#subsection)

# Runbook

```
# git push origin main

# pipenv
pipenv install
pipenv install setuptools

# airflow
cd DAG_ingestion_pipeline/
docker-compose up airflow-init
# follow DAG_ingestion_pipeline/README.md
```

# DAG_ingestion_pipeline

1. [DAG_ingestion_pipeline/README.md](/DAG_ingestion_pipeline) - DAG_ingestion_pipeline Readme
2. [terraform/\<env-name\>.tfvars](/terraform) - Infrastructure configuration (ALBs, IAM, SG, Lambda, etc)

# Chapter2

my list

* [item1](#item1) (My Item 1)
* [item2](#item2) (My Item 2)

## Section21

a brown fox

## Section22

a brown fox

```
./run.sh param1 param2
./run2.sh param1 param2
```

### Subsection

a brown fox

```
./run.sh param1 param2
./run2.sh param1 param2
```