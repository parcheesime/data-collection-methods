from zeep import Client

# URL to the WSDL file
wsdl = 'http://www.dneonline.com/calculator.asmx?WSDL'

# Create a client at the specified WSDL URL
client = Client(wsdl)

# Access the 'Add' service operation
result = client.service.Add(intA=10, intB=20)

# Print the response received from the server
print('The result of addition is:', result)

/home/aletia/wsl_code/data-collection-methods/api_data_collection