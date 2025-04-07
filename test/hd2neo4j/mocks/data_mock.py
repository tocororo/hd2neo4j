mocked_data = [
    {
            "id": "PER-001",
            "name": "Carlos",
            "last_name": "Pérez",
            "gender": "M",
            "country": {
              "code": "CU",
              "name": "Cuba"
            },
            "email_addresses": ["carlos.perez@uniejemplo.edu"],
            "institutional_email": "carlos.perez@uniejemplo.edu",
            "aliases": ["C. Pérez"],
            "research_interests": ["Inteligencia Artificial"],
            "key_words": ["Machine Learning", "Data Science"],
            "academic_titles": ["PhD en Computación"],
            "roles_sceiba": ["Investigador"],
            "identifiers": [
            {
              "idtype": "grid",
              "value": "grid.1310.3"
            },
            {
              "idtype": "orgref",
              "value": "9477251"
            },
            {
              "idtype": "wkdata",
              "value": "Q5260531"
            },
            {
              "idtype": "ror",
              "value": "https://ror.org/017wrhq72"
            }
          ],
            "affiliations": {
              "name":"Universidad de Habana",
              "id": "ORG-001",
              "start_date": "2015-09-01",
              "support_address": "contacto@uniejemplo.edu",
              "label": "Profesor Titular",
              "roles": ["Investigador Principal"]
            }
          },
          {
            "id": "PER-002",
            "name": "Ana",
            "last_name": "García",
            "gender": "F",
            "country": {
              "__id":"code",
              "code": "CU",
              "name": "Cuba"
            },
            "email_addresses": ["ana.garcia@uniejemplo.edu"],
            "institutional_email": "ana.garcia@uniejemplo.edu",
            "aliases": ["A. García"],
            "research_interests": ["Robótica"],
            "key_words": ["Automatización", "Control"],
            "academic_titles": ["MSc en Robótica"],
            "roles_sceiba": ["Docente"],
            "affiliations": [{
              "id": "ORG-001",
              "start_date": "2018-02-15",
              "name": "Profesora Asistente",
              "roles": ["Docente"]
            },
            {
              "id": "ORG-002",
              "start_date": "2018-02-15",
              "name": "Contrata",
              "roles": ["Docente"]
            }
          ]
          },
          {
            "id": "PER-003",
            "name": "Luis",
            "last_name": "Martínez",
            "gender": "M",
            "country": {
                "code": "MX",
                "name": "México"
            },
            "email_addresses": ["luis.martinez@universidad.mx"],
            "institutional_email": "luis.martinez@universidad.mx",
            "aliases": ["L. Martínez"],
            "research_interests": ["Ciberseguridad"],
            "key_words": ["Hacking Ético", "Seguridad de Redes"],
            "academic_titles": ["PhD en Seguridad Informática"],
            "roles_sceiba": ["Investigador"],
            "affiliations": {
                "id": "ORG-001",
                "start_date": "2016-10-01",
                "label": "Profesor Titular",
                "roles": ["Investigador Principal"]
            }
        },
        {
            "id": "PER-004",
            "name": "María",
            "last_name": "López",
            "gender": "F",
            "country": {
                "code": "ES",
                "name": "España"
            },
            "email_addresses": ["maria.lopez@universidad.es"],
            "institutional_email": "maria.lopez@universidad.es",
            "aliases": ["M. López"],
            "research_interests": ["Bioinformática"],
            "key_words": ["Genómica", "Análisis de Datos Biomédicos"],
            "academic_titles": ["MSc en Biología Computacional"],
            "roles_sceiba": ["Investigador", "Docente"],
            "affiliations": {
                "id": "ORG-001",
                "start_date": "2017-05-20",
                "label": "Investigadora Asociada",
                "roles": ["Docente", "Coordinadora de Proyecto"]
            }
        },
        {
            "id": "PER-005",
            "name": "Pedro",
            "last_name": "Gómez",
            "gender": "M",
            "country": {
                "code": "AR",
                "name": "Argentina"
            },
            "email_addresses": ["pedro.gomez@investigacion.ar"],
            "institutional_email": "pedro.gomez@investigacion.ar",
            "aliases": ["P. Gómez"],
            "research_interests": ["Energías Renovables"],
            "key_words": ["Energía Solar", "Eficiencia Energética"],
            "academic_titles": ["PhD en Ingeniería Energética"],
            "roles_sceiba": ["Investigador"],
            "affiliations": {
                "id": "ORG-001",
                "start_date": "2014-09-15",
                "label": "Profesor Titular",
                "roles": ["Director de Departamento"]
            }
        }
    ]

error_mocked_data=[
    {
            "id": "PER-006",
            "last_name": "Ramírez",
            "gender": "F",
            "country": {
                "code": "CO",
                "name": "Colombia"
            },
            "email_addresses": ["sofia.ramirez@academia.co"],
            "institutional_email": "sofia.ramirez@academia.co",
            "aliases": ["S. Ramírez"],
            "research_interests": ["Neurociencia Computacional"],
            "key_words": ["Simulación Cerebral", "Inteligencia Artificial"],
            "academic_titles": ["MSc en Neurociencia"],
            "roles_sceiba": ["Investigador", "Docente"],
            "affiliations": {
                "name":"Universidad de Colombia",
                "id": "ORG-005",
                "start_date": "2019-03-01",
                "label": "Profesora Asociada",
                "roles": ["Investigadora"]
            }
        }
]