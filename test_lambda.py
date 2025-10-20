import json
import requests

def lambda_handler(event, context):
    try:
        # Test if requests works
        test_response = requests.get("https://httpbin.org/json")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Requests library is working!',
                'test_url': 'https://httpbin.org/json',
                'status': 'success'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Requests failed: {str(e)}'})
        }
