import os
import unittest

from fastapi.testclient import TestClient

import main
import schemas

client = TestClient(main.app)
auth_token = os.environ["AUTH_TOKEN"]


def assert_not_raises(expr):
    try:
        expr()
    except Exception:
        # fail the test
        assert False


unittest.TestCase.assert_not_raises = assert_not_raises


class MainTests(unittest.TestCase):
    def test_get_status(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"status": "OK"}

    def test_get_tweets_by_tag_success(self):
        tag = "earthquake"
        count = 20
        response = client.post(
            "/tweets" + f"?tags={tag}&count={count}",
            headers={"Authorization": f"Bearer {auth_token}"},
        )
        assert response.status_code == 200
        assert len(response.json()) == count
        [
            unittest.TestCase.assert_not_raises(lambda: schemas.TweetData(**x))
            for x in response.json()
        ]


if __name__ == "__main__":
    unittest.main()
