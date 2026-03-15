
def test_api_get_request(playwright):
    request = playwright.request.new_context(
        extra_http_headers={"Accept": "application/json",
                            "Authorization": "Bearer your_access_token_here",
                            "x-api-key": "reqres_984c19d5ca81413a85232d4c3225f569"}
    )
    response = request.get("https://reqres.in/api/users?page=2",
                           headers={"Accept": "application/json"})
    assert response.status == 200 # Check if the response status code is 200 (OK)
    json_response = response.json() # Parse the response as JSON
    print(json_response)
    #assert json_response["id"] == 1 # Check if the "id" field in the response is 1
    request.dispose()
