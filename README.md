# forms

run using:
pyinstaller --onefile --windowed main.py --add-data "app/assets;app/assets" --add-data "C:\Users\Matthew Chen\anaconda3\Lib\site-packages\babel\locale-data;babel/locale-data" --hidden-import babel.numbers --hidden-import babel.dates --hidden-import babel.core --hidden-import babel.localedata --exclude-module numpy --exclude-module pandas --exclude-module scipy --exclude-module matplotlib --exclude-module pyarrow --exclude-module PyQt5