from mako.template import Template

http_status_codes = {
  '1xx': [100, 101, 102, 103],
  '2xx': [200, 201, 202, 203, 204, 205, 206, 207, 208, 226],
  '3xx': [300, 301, 302, 303, 304, 307, 308],
  '4xx': [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 451],
  '5xx': [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
}

for i in ['1xx', '2xx', '3xx', '4xx', '5xx']:
  template = Template(filename=f'templates/subdomain-{i}.conf.mako')

  with open(f'build/subdomain-{i}.conf', 'w') as f:
    f.write(template.render(http_status_codes=http_status_codes[i]))
