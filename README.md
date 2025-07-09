# Star Wars People API Integration Task

### Goal

Build a small FastAPI-based microservice that integrates with the [Star Wars API (SWAPI)](https://swapi.info) and returns a list of all character names.

---

### What You Need to Do

1. **Implement the logic in `services.py`:**

   - Use the SWAPI people endpoint
   - Collect all names and return them as a JSON list in this format:

     ```json
     {
       "names": ["Luke Skywalker", "Darth Vader", "..."]
     }
     ```

2. **Add Unit Tests in `tests/test_main.py`:**

   - Use `pytest` and `pytest-httpx`
   - At least one test should check that the `/people` endpoint works as expected

3. **Containerize the application:**

   - Write a `Dockerfile` for the service
   - Create a `docker-compose.yml` file that builds the image and exposes the app on port `8000`

4. **Test usage without container:**

This can be used for testing before containerization
```
uvicorn app.main:app --reload
```

---

### Example Usage

After starting the service, the following request:

```
GET http://localhost:8000/people
```

Should return:

```json
{
  "names": ["Luke Skywalker", "Darth Vader", "..."]
}
```

---

### Requirements

- Async HTTP calls (using e.g. `httpx`)
- Proper error handling if external API fails
- Unit tests that pass
- Docker setup that runs the app and allows testing
- Avoid hardcoding
