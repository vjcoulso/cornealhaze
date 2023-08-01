# cornealhaze
Calculates corneal haze from a set of In vivo corneal confocal microscope images
General Procedure

Open Fiji/ ImageJ
Go to file—>Import—>Image Sequence
Dir: Select your folder and click open
Import image sequence from HRT or similar, Click Ok
Go to file
Save as: Tiff
Save it as movie.tiff
Copy and paste haze.py file in the folder along with movie.tiff

For MAC:

Open terminal
write: cd /folderaddress
press enter
(Check by pressing pwd and enter)
On terminal write: python3 haze.py movie.tif
Press enter
Now your folder should have created haze.png and filename files
Change the filename with your sample name followed by .csv
Now a sheet with values should have been created which you can save as an excel file
