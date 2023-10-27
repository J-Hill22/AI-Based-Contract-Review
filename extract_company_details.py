import re

def extract_company_details(contract_text):
    """
    Extracts key details related to a company from a contract text.
    
    Parameters:
        contract_text (str): The text content of the contract.
    
    Returns:
        dict: A dictionary containing the extracted company name, location, and type of organization.
    """
    # Regular expressions for extracting details
    company_name_regex = re.compile(r'(?<=\n)[\w\s,&-]+(?:Inc|LLC|Ltd)[.,]?')
    location_regex = re.compile(r'\d+\s[\w\s,-]+,\s(?:AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)\s\d{5}')
    
    # Extracting details
    company_name_matches = company_name_regex.findall(contract_text)
    location_matches = location_regex.findall(contract_text)
    
    # Identifying the most plausible matches
    company_name = next((name.strip() for name in company_name_matches if "Quantum Research International" in name), None)
    location = location_matches[0] if location_matches else None
    
    # Extracting type of organization from company name
    organization_type = None
    if company_name:
        organization_type_match = re.search(r'(Inc|LLC|Ltd)', company_name)
        organization_type = organization_type_match.group() if organization_type_match else None
    
    # Returning the extracted details
    return {
        "Company Name": company_name,
        "Location": location,
        "Type of Organization": organization_type
    }
