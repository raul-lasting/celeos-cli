import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import pycurl
from io import BytesIO
import global_params


def add_sigmf(sigmf_archive_path):
    # Get the current directory (same as the Python script)
    #current_dir = os.path.dirname(os.path.abspath(__file__))

    # Buffer to capture the response
    buffer = BytesIO()

    # Create a pycurl object
    c = pycurl.Curl()

    # Set the URL of the endpoint
    c.setopt(c.URL, f"{global_params.get_url()}/sigmf")
    
    # Set the HsigmfTTP method to POST
    c.setopt(c.POST, True)

    # Attach the file in form-data
    c.setopt(c.HTTPPOST, [
        ('sigmf', (c.FORM_FILE, sigmf_archive_path))
    ])

    # Set token in the headers (if required)
    token = global_params.get_token()
    header = [
        "Authorization: " + token
    ]
    c.setopt(c.HTTPHEADER, header)

    # Set where to write the response
    c.setopt(c.WRITEDATA, buffer)

    # buffer = BytesIO()
    # c.setopt(c.WRITEDATA, buffer)

    print("It may take a while, be patient!")
    
    # Perform the request
    try:
        c.perform()
    except pycurl.error as e:
        print("Pycurl error:", e)

    # Get response
    response_code = c.getinfo(c.RESPONSE_CODE)
    response_body = buffer.getvalue().decode('utf-8')
    #print(f"Response Code: {response_code}")
    #print("Response Body:", response_body)
    data_response = json.loads(response_body)
    
    if response_code != 200:
        print(data_response.get("message"))
        raise RuntimeError(f"HTTP {response_code} Error: {data_response.get('message')}")
    else:
        print(data_response.get("message"))
    
    #assert data_response.get('message') == "SigMF file already exists, please use the DELETE endpoint and then re-upload the file." or data_response.get('message') == "SigMF archive saved", 'Error with the sigmf file.'
    
    # Cleanup
    c.close()
    
if __name__ == "__main__":
    add_sigmf("path/to/sigmf_archive")