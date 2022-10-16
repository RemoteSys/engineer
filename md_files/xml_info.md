# XMl
  
 - `xml`: eXtensible Markup Language  
 - info / tutorial: [w3schools](https://www.w3schools.com/xml/xml_whatis.asp)  
  
# Download currency codes  
  
Download the file with currency codes from the website:   
 - `https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml`  
  
 - to download, use the `requests` module, using the context manager: `with requests.sessions.Session() as session:`  
  
  
# Pre-processing currency codes  
  
Data in the downloaded file:    
 - may contain empty cells    
 - duplicate entries    
 - entries ambiguous    
  
  
**Purpose**:    
Prepare a set of several dozen rows with three columns:    
 - country name    
 - currency code    
 - continent    
  
## Scheme  
   
 - import module: `import xml.etree.ElementTree as ET`  
 - get a list of all tags in the file - write a recursive function  
 - select tags with useful information   
 - create a list: `country_codes = [[country name, currency code, continent name],...]`  
 - save the list as csv file - `csv module`  
 - edit the list in an editor or spreadsheet and select several dozen countries (e.g. 50): simple names and one unique currency code  
 - add a column and add the name of the continent in it  
 - save the file to disk  
  
  
## Create new xml file  
  
**Purpose**  
Create a new xml file with the structure:  
  
```xml  
<currency_codes>  
  
  <country>  
    <name>country name</country name>  
    <code>currency code</currency code>  
    <region>continent name</region>  
  </country>  
  
  <country>  
    <name>country name</country name>  
    <code>currency code</currency code>  
    <region>continent name</region>  
  </country>  
  
</currency_codes>  
```  
  
  
 1. Create `root` element e.g. `root = ET.Element('currency_codes')`  
 2. iterating through the list `country_codes`:  
  - `for item in country_codes`:  
  
 3. Add data to an xml file e.g.:  
  - `country = ET.SubElement(root,'country')`  
  - `name = ET.SubElement(country,'name')`  
  - `name.text = 'Poland'`  
  
  
# XML: searching for data  
  
Write three functions:  
  
 - to search for a currency code based on the name of the country  
 - showing all country names based on the name of the continent  
 - showing the names of continents in the xml database  
  
  
  
  
