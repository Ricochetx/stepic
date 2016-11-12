def wsgi_application(env, start_response):
	status =  '200 OK'
	headers = [
	   ('Content-Type', 'text/plain')
	   ]
	body = env['QUERY_STRING'].split('&')
	start_response(status, headers)
	return [i + '\r\n' for i in body]