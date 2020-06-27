from cgi import parse_qs
from calctemplate import html

def application(environ, start_response):
    d = parse_qs(environ["QUERY_STRING"])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    SUM = "please input a , b"
    Mul = "How about input a, b"

    if '' not in [a, b] :
        a, b,  = int(a), int(b) 
        SUM = a + b
        Mul = a * b
    response_body = html%{
    'SUM': SUM,
    'Mul': Mul,
    }
    start_response('200 OK',[
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
        ])

    return [response_body]
