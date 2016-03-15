from boto.sns import connect_to_region

from caribewave import settings


def connect():
    conn = connect_to_region(
        settings.AWS_REGION)
    return conn


def create_endpoint(token):
    """
    Create an endpoint on SNS based on token 
    and subscribe to alert topic
    """
    conn = connect()
    app_endpoint = conn.create_platform_endpoint(
        platform_application_arn=settings.SNS_APP_ID,
        token=token)
    endpoint_arn = app_endpoint['CreatePlatformEndpointResponse']['CreatePlatformEndpointResult']['EndpointArn']
    conn.subscribe(
        settings.SNS_ALERT_TOPIC,
        'application',
        endpoint_arn)


def send_message(message):
    conn = connect()
    conn.publish(message=message,
                 target_arn=settings.SNS_ALERT_TOPIC)
