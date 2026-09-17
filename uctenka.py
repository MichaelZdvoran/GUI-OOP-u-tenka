import requests

print("=== Python Receipt OCR ===")

receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt' # Receipt OCR API endpoint
imageFile = "US-1.jpg" # // Modify it to use your own file
r = requests.post(receiptOcrEndpoint, data = { \
  'api_key': 'TEST',        # Use 'TEST' for testing purpose \
  'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
  'ref_no': 'ocr_python_123', # optional caller provided ref code \
  }, \
  files = {"file": open(imageFile, "rb")})

print(r.text) # result in JSON