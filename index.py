# This file serves the root index.html for Vercel
def handler(request):
    with open('frontend/index.html', 'r') as f:
        html_content = f.read()
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html; charset=utf-8',
        },
        'body': html_content
    }