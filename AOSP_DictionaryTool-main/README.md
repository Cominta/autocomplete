# Binary Dictionary Tool - Build A Dictionary From Scratch

## Description
This tool generates binary dictionaries with (.dict) file extension & can be covertable to (.jet) file extension. Using Python, Perl, Sqlite and Java.

## Instructions
1. Open the project in Pycharm or any other IDE.
2. Browse for "check_frequency_generate_db.py" Open it and in the last line main method is taking filepath as input: Put file path of your "raw_data.txt" file and run it.
3. It Generates a sqlite database "EnglishDictionary.sqlite", Open it in Sqlite Browser and export the data as ".csv" file (while exporting put "|" as the separater instead of ",").
4. When a csv file is generated, open it inside any text editor lets say in sublime text and replace “ | ” with “ , f=”.
5. Save as file in different extension (rawdata.csv to rawdata.combined).
6. After that, Open the new (.combined) file in any text editor, Now remove the first line ("word, freq") & Add a header e.g: dictionary=main:en,locale=en,description=English,date=1542212847,version=01.
7. Run the following:
```bash
  java -jar dicttool_aosp.jar makedict -s <filename.combined> -d <filename.dict>
```

## Credits
[remi0s](https://github.com/remi0s/aosp-dictionary-tools)

## License
![Static Badge](https://img.shields.io/badge/MIT-License-blue)

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) license.

## Queries
[Adnan Chohan](https://github.com/adnanchohan)
<br>
Email: adnan.chohan104@gmail.com
