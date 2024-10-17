import uuid


def test_create_collection(client, sample_data) -> None:
    test_app, test_user = sample_data
    response = client.post(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections",
        json={"name": "test_collection", "metadata": {}},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_collection"
    assert data["metadata"] == {}
    assert "id" in data


def test_get_collection_by_id(client, sample_data) -> None:
    test_app, test_user = sample_data
    # Make the collection
    response = client.post(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections",
        json={"name": "test_collection", "metadata": {}},
    )
    assert response.status_code == 200
    data = response.json()
    # Get the collection
    response = client.get(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections/{data['id']}"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_collection"
    assert data["metadata"] == {}
    assert "id" in data


def test_get_collection_by_name(client, sample_data) -> None:
    test_app, test_user = sample_data
    # Make the collection
    response = client.post(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections",
        json={"name": "test_collection", "metadata": {}},
    )
    assert response.status_code == 200
    data = response.json()
    # Get the collection
    response = client.get(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections/name/test_collection"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_collection"
    assert data["metadata"] == {}
    assert "id" in data


def test_update_collection(client, sample_data) -> None:
    test_app, test_user = sample_data
    # Make the collection
    response = client.post(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections",
        json={"name": "test_collection", "metadata": {}},
    )
    assert response.status_code == 200
    data = response.json()
    # Update the collection
    response = client.put(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections/{data['id']}",
        json={"name": "test_collection_updated", "metadata": {"new_key": "new_value"}},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_collection_updated"
    assert data["metadata"] == {"new_key": "new_value"}
    assert "id" in data


def test_delete_collection(client, sample_data) -> None:
    test_app, test_user = sample_data
    # Make the collection
    response = client.post(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections",
        json={"name": "test_collection", "metadata": {}},
    )
    assert response.status_code == 200
    data = response.json()
    # Delete the collection
    response = client.delete(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections/{data['id']}"
    )
    assert response.status_code == 200
    response = client.get(
        f"/apps/{test_app.public_id}/users/{test_user.public_id}/collections/{data['id']}"
    )
    assert response.status_code == 404
