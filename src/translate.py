import boto3
 
client = boto3.client('translate', region_name= 'us-east-2')
text = "pengguna aplikasi, dan rumah mereka"
result = client.translate_text(Text=text,SourceLanguageCode="auto",TargetLanguageCode="en") 
print (result['TranslatedText'])