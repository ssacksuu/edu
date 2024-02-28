import subprocess



def lambda_handler(event, context):
    cmd = "고래밥 사"
    if "cmd" in event:
        cmd = event["cmd"]

    try:
        result =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
        output =  result.read()
        output =  output.decode("utf8")
    except Exception as err:
        output = str(err)

    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": output
    }

    return response

