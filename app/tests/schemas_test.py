import schemas
import sqlalchemy
import unittest
from unittest.mock import patch, Mock


class TestClass(unittest.TestCase):

    @patch('sqlalchemy.create_engine')
    def testar(self, mock):
        mock_engine = Mock()
        result_mock = 'WiLL'
        mock_engine.create_engine.return_value = result_mock
        mock.return_value = mock_engine
        result = schemas.getSchemas()


        assert len(result) > 0


    def testar(self):

        result = schemas.getSchemas()
        #print(result)
        assert len(result) > 0





