import app
import sys

def real_path(file_name):
    return app.real_path('/../' + file_name)

if __name__ == '__main__':
    try:
        app.default_settings()
        app.log('Domain Fronting running on 127.0.0.1 port 8080')
        domainfronting = app.domainfronting(('127.0.0.1', 8080), app.domainfronting_handler)
        domainfronting.whitelist_request = app.process_to_host_port(open(real_path('config/whitelist-request.txt')).readlines())
        domainfronting.frontend_domains = app.process_to_host_port(open(real_path('config/frontend-domains.txt')).readlines())
        domainfronting.buffer_size = 1024
        domainfronting.serve_forever()
    except KeyboardInterrupt:
        sys.stdout.write('        \r')
        sys.stdout.flush()
        app.log('Stopped.', color='[R1]')

