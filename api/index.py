def handler(request):
    """Ultra simple handler for debugging"""
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': '{"status": "ok", "message": "Ultra simple handler working"}'
    }