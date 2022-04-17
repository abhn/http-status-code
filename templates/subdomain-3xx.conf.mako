
%for return_code in http_status_codes:


if ($subdomain = "${return_code}") {
  return ${return_code} https://www.google.com;
}

%endfor
