from bs4 import BeautifulSoup
import csv
import selenium

file = open('prettified alibaba.html','r')
my_input = file.readlines()
soup = BeautifulSoup(str(my_input),'html.parser')
tables = soup.find('table')
#print(tables)

print('------------------------------extraction------------------------------')
table_data = []#stores all rows of data
# 1. Iterate through each row (<tr>) found within the table
rows = tables.find_all('tr')
for row in rows:
    row_data = []
    #inside each row contains (header cells<th>,data cells <td>)
    cells = row.find_all(['th','td'])
    #extract text from cell
    for cell in cells:
        row_data.append(cell.get_text(strip=True))
    
    if row_data:
        table_data.append(row_data)

if table_data:
    print(f"Extracted {len(table_data)} rows of data.")


    output_csv_file = 'alibaba_extracted_csv.csv'
    with open(output_csv_file,'w',newline = '',encoding = 'utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(table_data)

        print(f"Data succesfully saved to {output_csv_file}")








file.close()
