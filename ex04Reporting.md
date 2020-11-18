# Covid virus report and forecasts

### Project scope

1. Create a new directory for the project, e.g. `proj1` containing folders:   
    - data, img, forms, setup

2. Download virus and population data.
3. Perform data analysis:
    - infection history table and graph - fit the regression curve
    - forecast table and graph based on the regression curve for the next 6 months
    - save the results to the `data` and `img` folders

4. Prepare the report form and the `css` sheet file - save in the `forms` folder
5. Prepare a `json` file/files containing organizational data (report date, author, department, country, etc ...
6. Write a script that automatically creates a report

---

# Frame of report form

>Warning!

>The form form contains example fields - you should ensure that you insert a variable number of data, e.g. use a `for` loop!


<!DOCTYPE html>
<html>
    <head>
            <title>{{ Title }}</title>
            <link rel="stylesheet" href="myCss.css">
    </head>
    
    <body>
        <div>
        <h1>General information</h1>

        Data of report:  {{}}

        Country: {{}}

        Author: {{}}

        Faculty: {{}}

        </div>


        <div>
        Results


        Actual data (table): {{}}

        Course of infections and prognosis

        Figure (hisoty of infections): {{}}

        Prognosis for 6 months:

        Table: {{}}

        Figure: {{}}

        </div>


    </body>
</html>


# Script - requirements

1. Uses the `argparse` module to handle command line arguments
2. Display simple help when given the `-h` option
3. Creates and saves the report in the form of an `html` file
4. The report is created on the basis of data (csv files and images) placed in the appropriate folders.