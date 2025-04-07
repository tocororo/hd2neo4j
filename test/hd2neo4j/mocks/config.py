config_mock:dict  = {
  "name": "person_config",
  "description": "Configuration for mapping persons to a knowledge graph.",
  "entities": [
      {
          "name": "Person",
          "mapping": {
              "required": ["id", "name", "identifiers"],
              "_class": "http://iroko.org/ontology#Person",
              "properties": {
                  "id": "http://iroko.org/ontology#id",
                  "name": "http://iroko.org/ontology#name",
                  "last_name": "http://iroko.org/ontology#lastName",
                  "public": "http://iroko.org/ontology#publicProfile",
                  "active": "http://iroko.org/ontology#activeStatus",
                  "gender": "http://iroko.org/ontology#gender",
                  "email_addresses": "http://iroko.org/ontology#emailAddresses",
                  "aliases": "http://iroko.org/ontology#aliases",
                  "research_interests": "http://iroko.org/ontology#researchInterests",
                  "key_words": "http://iroko.org/ontology#keyWords",
                  "academic_titles": "http://iroko.org/ontology#academicTitles",
                  "roles_sceiba": "http://iroko.org/ontology#rolesSceiba",
                  "country": {
                      "__relation": "code",
                      "__predicate": "LIVES_IN",
                      "__target": "Country",
                      "code": "http://iroko.org/ontology#countryCode",
                      "name": "http://iroko.org/ontology#countryName"
                  },
                  "identifiers": {
                      "__predicate": "idtype",
                      "__object": "value",
                      "idtype": "valuesOf:identifiers.idtype"
                  },
                  "affiliations": {
                      "__relation": "id",
                      "__predicate": "AFFILIATED_TO",
                      "__target": "Organization",
                      "relation_properties":{
                        "start_date": "http://iroko.org/ontology#affiliationStartDate",
                        "end_date": "http://iroko.org/ontology#affiliationEndDate",
                        "roles": "http://iroko.org/ontology#affiliationRoles"
                      },
                      "id": "http://iroko.org/ontology#affiliationId",
                      "label": "http://iroko.org/ontology#affiliationLabel"
                      
                  },
                  "publications": {
                      "__relation": "id",
                      "__predicate": "AUTHORED",
                      "__target": "Publication",
                      "id": "http://iroko.org/ontology#publicationId",
                      "title": "http://iroko.org/ontology#publicationTitle",
                      "roles": "http://iroko.org/ontology#publicationRoles",
                      "status": "http://iroko.org/ontology#publicationStatus"
                  },
                  "sources": {
                      "__relation": "id",
                      "__predicate": "ASSOCIATED_WITH",
                      "__target": "Source",
                      "id": "http://iroko.org/ontology#sourceId",
                      "name": "http://iroko.org/ontology#sourceName",
                      "roles": "http://iroko.org/ontology#sourceRoles"
                  }
              },
              "valuesOf": {
          "identifiers.idtype": {
            "ark": "http://sceiba.cu/identifier#ark",
            "arxiv": "http://sceiba.cu/identifier#arxiv",
            "doi": "http://sceiba.cu/identifier#doi",
            "bibcode": "http://sceiba.cu/identifier#bibcode",
            "ean8": "http://sceiba.cu/identifier#ean8",
            "ean13": "http://sceiba.cu/identifier#ean13",
            "handle": "http://sceiba.cu/identifier#handle",
            "isbn": "http://sceiba.cu/identifier#isbn",
            "issn_l": "http://sceiba.cu/identifier#issn_l",
            "issn_p": "http://sceiba.cu/identifier#issn_p",
            "issn_e": "http://sceiba.cu/identifier#issn_e",
            "issn_c": "http://sceiba.cu/identifier#issn_c",
            "issn_o": "http://sceiba.cu/identifier#issn_o",
            "istc": "http://sceiba.cu/identifier#istc",
            "lsid": "http://sceiba.cu/identifier#lsid",
            "pmid": "http://sceiba.cu/identifier#pmid",
            "pmcid": "http://sceiba.cu/identifier#pmcid",
            "purl": "http://sceiba.cu/identifier#purl",
            "upc": "http://sceiba.cu/identifier#upc",
            "url": "http://sceiba.cu/identifier#url",
            "urn": "http://sceiba.cu/identifier#urn",
            "orcid": "http://sceiba.cu/identifier#orcid",
            "dni": "http://sceiba.cu/identifier#dni",
            "scopid": "http://sceiba.cu/identifier#scopid",
            "hrid": "http://sceiba.cu/identifier#hrid",
            "passp": "http://sceiba.cu/identifier#passp",
            "gnd": "http://sceiba.cu/identifier#gnd",
            "ads": "http://sceiba.cu/identifier#ads",
            "oai": "http://sceiba.cu/identifier#oai",
            "prnps": "http://sceiba.cu/identifier#prnps",
            "ernps": "http://sceiba.cu/identifier#ernps",
            "oaiurl": "http://sceiba.cu/identifier#oaiurl",
            "grid": "http://sceiba.cu/identifier#grid",
            "wkdata": "http://sceiba.cu/identifier#wkdata",
            "ror": "http://sceiba.cu/identifier#ror",
            "isni": "http://sceiba.cu/identifier#isni",
            "fudref": "http://sceiba.cu/identifier#fudref",
            "orgref": "http://sceiba.cu/identifier#orgref",
            "reup": "http://sceiba.cu/identifier#reup",
            "orgaid": "http://sceiba.cu/identifier#orgaid",
            "uniid": "http://sceiba.cu/identifier#uniid",
            "sceibaid": "http://sceiba.cu/identifier#sceibaid",
            "irouid": "http://sceiba.cu/identifier#irouid",
            "srcid": "http://sceiba.cu/identifier#srcid",
            "orgid": "http://sceiba.cu/identifier#orgid",
            "perid": "http://sceiba.cu/identifier#perid"
          }
        }
          }
      }
  ]
}
