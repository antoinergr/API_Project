from Request.Imdb_Request import ImdbRequest
from requests import HTTPError
import requests
from Request.Response import Response
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock


class TestRequest(unittest.TestCase):


    @patch("Request.Imdb_Request.requests")
    def test_response_request(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"results": [{"id": 12}]}


        mock_requests.get.return_value = mock_response

        self.assertIsInstance(ImdbRequest.get_movie_info("Inception"), Response)


    @patch("Request.Imdb_Request.requests")
    def test_status_code(self, mock_requests_code):

        mock_res = MagicMock()
        mock_res.status_code = 200
        mock_res.json.return_value = {"results": [{"id": 12}]}

        mock_requests_code.get.return_value = mock_res

        self.assertEqual(ImdbRequest.get_movie_info('Inception').status_code,200)


    @patch("Request.Imdb_Request.requests")
    def test_status_code_error(self, mock_requests):

        mock_requests.exceptions = requests.exceptions
        mock_response = MagicMock(status_code = 403)
        mock_response.raise_for_status.side_effect = \
        HTTPError('HTTPError')

        mock_requests.get.return_value = mock_response
        self.assertEqual(ImdbRequest.get_movie_id(Response(200,{"results": [{"id": '12'}]})),'HTTPError')
    