# HTTP Status Code
Extremely simple Docker Nginx setup that can return most HTTP status codes for testing

### Setup
- Clone the project
- Install dependencies with `pipfile install`
- Run `python subdomain-config-generator.py` to generate subdomain configs
- Run `docker build -t return-status . && docker run -d -p 8080:80 return-status` to build and start the project at port 8080
- Open `"status_code".localhost:8080` and the page will return the HTTP status code as directed.

### Supported HTTP Codes
```py
http_status_codes = {
  '1xx': [100, 101, 102, 103],
  '2xx': [200, 201, 202, 203, 204, 205, 206, 207, 208, 226],
  '3xx': [300, 301, 302, 303, 304, 307, 308],
  '4xx': [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 451],
  '5xx': [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
}
```
