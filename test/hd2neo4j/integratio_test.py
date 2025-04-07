import pytest
from hd2neo4j.services import MapperService, RepositoryService
from test.hd2neo4j.mocks.config import config_mock
from test.hd2neo4j.mocks.data_mock import mocked_data

class TestIntegration:
    repository = RepositoryService("neo4j://localhost:7687", "neo4j", "Anime404*01", "neo4j")
    mapper = MapperService(data_to_map=mocked_data, mapping_config=config_mock, repository_service=repository)
        
    @pytest.mark.asyncio
    async def test_integration(self):
        self.mapper.start_mapping()
        result = await self.repository.get_graph()
        
        print(result)
        assert True