from Request.ImdbRequest import ImdbRequest

from Request.Response import Response
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

class TestRequest(unittest.TestCase):

    @patch('Request.ImdbRequest')
    def test_response_request(self,mock_requests):
        
        mock_responses = [MagicMock(),MagicMock()]
        mock_responses[0].json.return_value = {'results': [{'id': 12}]}
        mock_responses[1].status_code = 200
        mock_responses[1].json.return_value = {'title':'Inception'}

        mock_requests.side_effects = mock_responses

        self.assertIsInstance(ImdbRequest.get_info('Inception'),Response)

