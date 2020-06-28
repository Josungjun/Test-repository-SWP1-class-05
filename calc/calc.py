from cgi import parse_qs
from calctemplate import html

def application(environ, start_response):
    d = parse_qs(environ["QUERY_STRING"])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    SUM = 0
    Mul = 0
     
    try:
        a, b,  = int(a), int(b) 
        SUM = a + b
        Mul = a * b
   
    except:
        SUM = "sorry we can't deal with string"
        Mul = "please only input number"

    response_body = html%{
    'SUM': SUM,
    'Mul': Mul,
    }
    start_response('200 OK',[
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
        ])

    return [response_body]
