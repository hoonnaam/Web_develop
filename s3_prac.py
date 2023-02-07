import boto3


def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="AKIARCOQH6HDSAK5HDPX",
            aws_secret_access_key="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",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3
s3 = s3_connection() #함수 호출

def upload_to_s3(local_file, s3_file):
    s3.upload_file(local_file, "swcamp-imagebox", s3_file,
                   ExtraArgs={'ACL': 'public-read'})
    return f"https://s3.ap-northeast-2.amazonaws.com/swcamp-imagebox/{s3_file}"

local_file = "photos/사진1.jpeg"
s3_file = f"{local_file}"
url = upload_to_s3(local_file, s3_file)
print(f"File is uploaded at {url}")


