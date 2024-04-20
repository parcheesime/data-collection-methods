from zeep import Client

# URL to the WSDL file
wsdl = 'http://www.dneonline.com/calculator.asmx?WSDL'

# SOAP service WSDL (Web Services Description Language) URL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# Create a client using the WSDL
client = Client(wsdl_url)

# List all available operations
for service in client.wsdl.services.values():
    print(f"Service: {service.name}")
    for port in service.ports.values():
        operations = sorted(
            port.binding._operations.values(),
            key=lambda operation: operation.name
        )
        for operation in operations:
            print(f"  Operation: {operation.name}")
            print(f"    Input: {operation.input.signature()}")
            if operation.output:
                print(f"    Output: {operation.output.signature()}")
            print("\n")

# Print all types defined in the WSDL
types = client.wsdl.types.types
for type_obj in types:
    print(type_obj)
    
print("Elements:")
for element in client.wsdl.types.elements:
    print(f"Element QName: {element.qname}")
    # Check if the element has a 'type' and print it
    if hasattr(element, 'type') and element.type:
        print(f"Element Type: {element.type}")
    else:
        print("Element does not have a 'type' defined")
        
# iso_code = "ENG"  # Example ISO code for English

# # Call the operation
# response = client.service.LanguageName(iso_code)

# # Print the result
# print("Language Name Result:", response)

# Call the operation to list all languages
response = client.service.ListOfCurrenciesByName()

# Assuming the response contains an iterable list of currency
for currency in response:
    print(currency)